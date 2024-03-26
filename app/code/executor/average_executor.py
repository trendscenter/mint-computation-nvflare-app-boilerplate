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
            data_dir_path = get_data_dir_path(fl_ctx)
            local_average_and_count = get_local_average_and_count(
                data_dir_path)

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
    results_dir = get_results_dir_path(fl_ctx)
    print(f"\nSaving results to: {results_dir}\n")
    with open(os.path.join(results_dir, file_name), "w") as f:
        json.dump(results, f)


def get_results_dir_path(fl_ctx: FLContext):
    # Directly return the path from environment variable if available
    if "RESULTS_DIR" in os.environ:
        return os.environ["RESULTS_DIR"]

    # Construct the path using job_id and site_name if environment variable is not set
    job_id = fl_ctx.get_job_id()
    site_name = fl_ctx.get_prop(FLContextKey.CLIENT_NAME)
    results_dir = os.path.join(
        os.getcwd(), "../../../test_results", job_id, site_name)

    # Ensure the directory exists
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    return results_dir


def get_data_dir_path(fl_ctx: FLContext):
    # Directly return the path from environment variable if available
    if "DATA_DIR" in os.environ:
        return os.environ["DATA_DIR"]

    # Construct the path using site_name if environment variable is not set
    site_name = fl_ctx.get_prop(FLContextKey.CLIENT_NAME)
    data_dir_path = os.path.join(os.getcwd(), "../../../test_data", site_name)

    return data_dir_path
