from nvflare.lighter.spec import Builder
import os
import shutil

class TestDataBuilder(Builder):
    def __init__(self, data=None):
        self.data = data

    def initialize(self, ctx):
        pass
    
    def build(self, project, ctx):
        test_data_dir = "/workspace/test_data"
        for client in project.get_participants_by_type("client", first_only=False):
            source_dir = os.path.join(test_data_dir, client.name)
            dest_dir = os.path.join(self.get_ws_dir(client, ctx), "data")
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
                
            print("copying test data from: ", source_dir, " into: ", dest_dir)
            
            if os.path.exists(source_dir) and os.path.isdir(source_dir):
                for item in os.listdir(source_dir):
                    s = os.path.join(source_dir, item)
                    d = os.path.join(dest_dir, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, dirs_exist_ok=True)
                    else:
                        shutil.copy2(s, d) 
                        
        return self.data
    
    def finalize(self, ctx):
        pass