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
        # Ensure output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Execute the nvflare provision command
        logger.info('Starting provision command...')
        result = subprocess.run(provision_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Log output and errors
        logger.info(result.stdout.decode('utf-8'))
        logger.info('Provisioning completed successfully.')

    except subprocess.CalledProcessError as error:
        logger.error(f'Failed to execute provision command: {error.stderr.decode("utf-8")}')
        raise  # Propagate the error for further handling

# Example usage:
# create_startup_kits('/path/to/Project.yml', '/path/to/outputDirectory')
