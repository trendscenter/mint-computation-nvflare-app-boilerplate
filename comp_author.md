The purpose of this repository is to assist computation authors in beginning the development of NVFLARE applications and COINSTAC computations. It serves as a brief guide for:

- Developing and testing NVFLARE applications.
- Ensuring these applications are compatible with the COINSTAC platform's specifications.

Included in this repository are an example application and boilerplate code, which serve as practical starting points for creating your own applications.

# NVFLARE

NVFLARE is an open-source federated learning tool developed by NVIDIA
You can find NVIDIA's documentation and source code here:
- https://nvflare.readthedocs.io/en/main/index.html
- https://github.com/NVIDIA/NVFlare

## Overview
An NVFLARE Application is the specific computation or learning model you develop. It encapsulates the custom logic and algorithms necessary for your federated learning computation. See the `app/` folder in this repository.

You can choose to develop inside a container or on your local host system.

NVFLARE provides tools for you to develop and test your application:
NVFLARE Simulator
NVFLARE POC mode

These tools automate the steps to running a federated computation
- Provisioning: Initiating a project creates startup kits for various components (sites, server, and admin) necessary for your federated network.
- Deployment: Launching and connecting the server, sites, and admin components using scripts provided in the startup kits.
- Execution: Submitting a job that runs your custom app across the federated network.

Try running the app in Simulator and POC mode, then try modifying the app code.
Use the following programming guide for developing applications:
https://nvflare.readthedocs.io/en/2.4.0/programming_guide.html

### Developing in a container
If you choose to develop in a container you can use the following command to build a dev docker image
```
docker build -t nvflare-pt -f Dockerfile-dev .
```
You can launch the container by running `./dockerRun.sh`
 
#### Proof of Concept (POC) Mode
https://nvflare.readthedocs.io/en/2.4.0/user_guide/nvflare_cli/poc_command.html#poc-command
The POC command allows users to try out the features of NVFlare in a proof of concept deployment on a single machine.

# Using POC mode
The following commands allow you to run the app in POC mode
- If you've made any changes to the app, run `./appToJob.sh` to transfer the changes into the job directory
```
nvflare poc prepare -i project.yaml
nvflare poc prepare-jobs-dir -j jobs
nvflare poc start
```
Once the previous command completes your command line will be in the admin shell. From there you can submit your job with the following command:
```
submit_job job
```

#### NVFLARE Simulator
https://nvflare.readthedocs.io/en/2.4.0/user_guide/nvflare_cli/fl_simulator.html

## Using NVFLARE Simulator
- As with POC mode, if you've made any changes to the app, run `./appToJob.sh` to transfer the changes into the job directory
The following commands allow you to run the app in POC mode
```
nvflare simulator -c site1,site2 ./jobs/job
```

# COINSTAC requirements
Ideally your app code will work identically in development and production environments. The main differences between Simulator, POC mode and the production environment are the paths to the directories your application will use.
Here are the current conventions/requirements we will use to keep parity between development and production directory paths. The conventions may change in the future as we learn more.
When developing in Simulator or POC mode, `./test_data` at the root of this repository will contain the source data your computation will consume. `./test_results` will be the director each site puts their results.
In production mode the sites will run in containers, the data and results folders on the host machine will be mounted to the container (currently as `/workspace/data/` and `/workspace/results`) and the paths to those directories will be environment variables `DATA_DIR` and `RESULTS_DIR`

The following is a snippet from the boilerplate average computation shows this convention being implemented.
```
# app\code\executor\average_executor.py
def get_data_dir_path(fl_ctx: FLContext):
    # Directly return the path from environment variable if available
    if "DATA_DIR" in os.environ:
        return os.environ["DATA_DIR"]

    # Construct the path using site_name if environment variable is not set
    site_name = fl_ctx.get_prop(FLContextKey.CLIENT_NAME)
    data_dir_path = os.path.join(os.getcwd(), "../../../test_data", site_name)

    return data_dir_path
```
