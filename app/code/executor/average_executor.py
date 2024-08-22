from nvflare.apis.executor import Executor
from nvflare.apis.fl_constant import FLContextKey
from nvflare.apis.fl_context import FLContext
from nvflare.apis.shareable import Shareable
from nvflare.apis.signal import Signal
from coinstac_utils.paths import get_data_directory_path, get_output_directory_path

from .local_average import get_local_average_and_count
import json
import os

class AverageExecutor(Executor):
    def execute(
        self,
        task_name: str,
        shareable: Shareable,
        fl_ctx: FLContext,
        abort_signal: Signal,
    ) -> Shareable:

        if task_name == "get_local_average_and_count":
            data_dir_path = get_data_directory_path(fl_ctx)
            computation_parameters = fl_ctx.get_peer_context().get_prop("COMPUTATION_PARAMETERS")
            decimal_places = computation_parameters["decimal_places"]
            local_average_and_count = get_local_average_and_count(
                data_dir_path, decimal_places)

            # save local average to local results file
            save_results_to_file(
                local_average_and_count,
                "local_average.json",
                fl_ctx
            )

            outgoing_shareable = Shareable()
            outgoing_shareable["result"] = local_average_and_count
            return outgoing_shareable

        if task_name == "accept_global_average":
            # save global average to local results file
            result = {"global_average": shareable.get("global_average", {})}
            save_results_to_file(
                result,
                "global_average.json",
                fl_ctx
            )
            return Shareable()


def save_results_to_file(results: dict, file_name: str, fl_ctx: FLContext):
    output_dir = get_output_directory_path(fl_ctx)
    print(f"\nSaving results to: {output_dir}\n")
    with open(os.path.join(output_dir, file_name), "w") as f:
        json.dump(results, f)

