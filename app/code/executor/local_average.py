import json
import os

def get_local_average_and_count():
    data_dir = os.environ.get("DATA_DIR") or "data/"
    data_file_filepath = os.path.join(data_dir, "data.json")
    
    ## read the data from the file
    ## the file can be like this [1,5,6,6,802,503,49]
    ## return the average and the count of the data
    
    with open(data_file_filepath, "r") as file:
        data = json.load(file)
        return {"average": sum(data) / len(data), "count": len(data)}