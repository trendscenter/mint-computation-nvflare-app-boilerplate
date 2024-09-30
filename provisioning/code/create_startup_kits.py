import subprocess
import logging
import os

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def create_startup_kits(project_file_path: str, output_directory: str) -> None:
    provision_command = [
        'nvflare',
        'provision',
        '-p', project_file_path,
        '-w', output_directory,
    ]

    try:
        # Log the paths for the project file and output directory
        logger.info(f'Project file path: {project_file_path}')
        logger.info(f'Output directory: {output_directory}')

        # Ensure output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Log that the provision command is starting
        logger.info('Starting provision command...')

        # Use subprocess.Popen for real-time output logging
        process = subprocess.Popen(
            provision_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Capture and log output line by line
        for stdout_line in iter(process.stdout.readline, ""):
            logger.info(stdout_line.strip())

        # Wait for the process to complete and get the return code
        process.stdout.close()
        return_code = process.wait()

        if return_code != 0:
            stderr_output = process.stderr.read()
            logger.error(f'Provision command failed with return code {return_code}: {stderr_output}')
            raise subprocess.CalledProcessError(return_code, provision_command, output=stderr_output)
        
        logger.info('Provisioning completed successfully.')

    except subprocess.CalledProcessError as error:
        logger.error(f'Failed to execute provision command: {error}')
        raise  # Propagate the error for further handling

# Example usage:
# create_startup_kits('/path/to/Project.yml', '/path/to/outputDirectory')
