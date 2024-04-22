import json
import os

def get_local_average_and_count(data_dir_path: str, decimal_places: int = 2):
    data_file_filepath = os.path.join(data_dir_path, "data.json")

    print(f"\nloading data from: {data_file_filepath} \n")

    with open(data_file_filepath, "r") as file:
        data = json.load(file)
        average = round(sum(data) / len(data), decimal_places) 
        count = len(data)
        return {"average": average, "count": count}
