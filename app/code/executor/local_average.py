import json
import os


def get_local_average_and_count(data_dir_path: str):
    data_file_filepath = os.path.join(data_dir_path, "data.json")

    print(f"\nloading data from: {data_file_filepath} \n")

    with open(data_file_filepath, "r") as file:
        data = json.load(file)
        return {"average": sum(data) / len(data), "count": len(data)}
