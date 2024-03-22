from nvflare.apis.dxo import DXO, DataKind, MetaKey, from_shareable
from nvflare.apis.executor import Executor
from nvflare.apis.fl_constant import FLContextKey, ReturnCode
from nvflare.apis.fl_context import FLContext
from nvflare.apis.shareable import Shareable, make_reply
from nvflare.apis.signal import Signal
from nvflare.app_common.abstract.model import ModelLearnable
from nvflare.app_common.app_constant import AppConstants
from nvflare.security.logging import secure_format_exception
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

        print(f"\n\nExecutor received task: {task_name}\n\n")

        if task_name == "get_local_average_and_count":
            local_average_and_count = get_local_average_and_count()

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
    job_id = fl_ctx.get_job_id()
    results_dir = os.environ.get("RESULTS_DIR") or os.path.join(job_id, "results")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    with open(os.path.join(results_dir, file_name), "w") as f:
        json.dump(results, f)
