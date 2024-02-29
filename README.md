### Build the Docker Image

First, build your Docker image with the following command:

```bash
docker build . -t nvflare-pt
```

This command builds a Docker image from the Dockerfile in the current directory, tagging it as `nvflare-pt`.

### Run the Docker Container

Execute the provided shell script to run your Docker container:

```bash
./dockerRun.sh
```

Make sure `dockerRun.sh` is executable. If not, run `chmod +x dockerRun.sh`.

**Note:** All subsequent commands should be executed within the Docker shell that opens after running the `dockerRun.sh` script.

### Set the Environment Variables

Configure the necessary environment variables for NVFlare:

```bash
export NVFLARE_POC_WORKSPACE=/workspace/poc-workspace
export PYTHONPATH=$PYTHONPATH:/workspace/app/code/:/workspace/util/
```

These variables specify the workspace directory and include paths for application and utility code.

### Copy the App Definition to the Job Folder

Use the script to copy your app definition:

```bash
./appToJob.sh
```

Ensure `appToJob.sh` is executable, akin to `dockerRun.sh`.

### Prepare the POC Workspace

Initialize the POC workspace with:

```bash
nvflare poc prepare -i project.yaml
```

This step sets up the workspace based on `project.yaml`.

### Link the Job Directory

Link the job directory to your NVFlare workspace:

```bash
nvflare poc prepare-jobs-dir -j jobs
```

### Start POC Mode

Start the POC mode to run your NVFlare project:

```bash
nvflare poc start
```

Your shell will enter Flare admin mode.

### Wait for All Components to Start

Wait until all NVFlare components have started, which typically takes less than 30 seconds. The logs will stabilize once the components are ready.

### Submit the Job

Submit your job with the following command:

```bash
submit_job job
```

### View Results

Access the results at the designated directory path, for example:

```
poc-workspace/example_project/prod_00/[site name]/[job_id]
```

Replace `[site name]` and `[job_id]` with your project's specific details.

### Writing Your Own Flare App

For custom app development within this framework, focus on modifying files in the `app/` and `test_data/` directories:

- **`app/config/`**: Contains your app's configuration. Any changes here require running `./appToJob.sh` to update the job directory.
- **`app/code/`**: Stores custom Python modules used by your app.

Ensure the folder names within `test_data` match those outlined in `project.yaml` if you want test data copied to respective sites.

This structure allows you to tailor the NVFlare application to your specific requirements, ensuring a flexible development environment.