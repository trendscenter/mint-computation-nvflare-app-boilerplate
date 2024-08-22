import json
import logging
from nvflare.apis.impl.controller import Controller, Task, ClientTask
from nvflare.apis.fl_context import FLContext
from nvflare.apis.signal import Signal
from nvflare.apis.shareable import Shareable
from coinstac_utils.paths import get_parameters_file_path

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AverageWorkflow(Controller):
    TASK_NAME_GET_LOCAL_AVERAGE_AND_COUNT = "get_local_average_and_count"
    TASK_NAME_ACCEPT_GLOBAL_AVERAGE = "accept_global_average"

    def __init__(
        self,
        aggregator_id="aggregator",
        min_clients: int = 2,
        wait_time_after_min_received: int = 10,
        task_timeout: int = 0,
    ):
        super().__init__()
        self.aggregator_id = aggregator_id
        self.aggregator = None
        self._task_timeout = task_timeout
        self._min_clients = min_clients
        self._wait_time_after_min_received = wait_time_after_min_received

    def start_controller(self, fl_ctx: FLContext) -> None:
        self.aggregator = self._engine.get_component(self.aggregator_id)

    def stop_controller(self, fl_ctx: FLContext):
        # necessary abstract method to implement
        pass

    def control_flow(self, abort_signal: Signal, fl_ctx: FLContext) -> None:
        fl_ctx.set_prop(key="CURRENT_ROUND", value=0)

        # Load and validate computation parameters directly
        parameters_file_path = get_parameters_file_path(fl_ctx)
        computation_parameters = load_computation_parameters(parameters_file_path)
        validate_parameters(computation_parameters)
        fl_ctx.set_prop(
            key="COMPUTATION_PARAMETERS",
            value=computation_parameters,
            private=False,
            sticky=True
        )


        get_local_average_task = Task(
            name=self.TASK_NAME_GET_LOCAL_AVERAGE_AND_COUNT,
            data=Shareable(),
            props={},
            timeout=self._task_timeout,
            result_received_cb=self._accept_site_result
        )
        self.broadcast_and_wait(
            task=get_local_average_task,
            min_responses=self._min_clients,
            wait_time_after_min_received=self._wait_time_after_min_received,
            fl_ctx=fl_ctx,
            abort_signal=abort_signal,
        )

        # Aggregate results and log
        aggr_shareable = self.aggregator.aggregate(fl_ctx)
        result = {"global_average": aggr_shareable.get("global_average", {})}
        logger.info(f"Aggregated result:\n{json.dumps(result, indent=4)}")


        accept_global_average_task = Task(
            name=self.TASK_NAME_ACCEPT_GLOBAL_AVERAGE,
            data=aggr_shareable,
            props={},
            timeout=self._task_timeout,
            result_received_cb=self._accept_site_result
        )
        self.broadcast_and_wait(
            task=accept_global_average_task,
            min_responses=self._min_clients,
            wait_time_after_min_received=self._wait_time_after_min_received,
            fl_ctx=fl_ctx,
            abort_signal=abort_signal,
        )

    def _accept_site_result(self, client_task: ClientTask, fl_ctx: FLContext) -> bool:
        return self.aggregator.accept(client_task.result, fl_ctx)

    def process_result_of_unknown_task(self, task: Task, fl_ctx: FLContext) -> None:
        pass


def load_computation_parameters(parameters_file_path: str) -> dict:
    with open(parameters_file_path, "r") as file:
        return json.load(file)


def validate_parameters(parameters: dict) -> None:
    if 'decimal_places' not in parameters:
        raise ValueError("Validation Error: The key 'decimal_places' is missing in the parameters.")
    if not isinstance(parameters['decimal_places'], (int, float)):
        raise ValueError("Validation Error: The value of 'decimal_places' must be a number.")
