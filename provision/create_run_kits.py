import os
import shutil
import logging

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def create_run_kits(
    startup_kits_path: str,
    output_directory: str,
    computation_parameters: str,
    host_identifier: str,
    admin_name: str
) -> None:
    logger.info('Running create_run_kits command')

    try:
        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Get site directories excluding the host_identifier and adminName
        site_directories = [
            name for name in os.listdir(startup_kits_path)
            if os.path.isdir(os.path.join(startup_kits_path, name)) and name not in [host_identifier, admin_name]
        ]

        # Copy each site's startupKit to the runKits directory
        for site in site_directories:
            source_path = os.path.join(startup_kits_path, site)
            destination_path = os.path.join(output_directory, site)
            copy_directory(source_path, destination_path)

        # Create the central node runKit
        central_node_path = os.path.join(output_directory, 'centralNode')
        os.makedirs(central_node_path, exist_ok=True)

        # Copy the server's startupKit to the central node runKit
        server_startup_kit_path = os.path.join(startup_kits_path, host_identifier)
        copy_directory(server_startup_kit_path, os.path.join(central_node_path, 'server'))

        # Copy the admin's startupKit to the central node runKit
        admin_startup_kit_path = os.path.join(startup_kits_path, admin_name)
        copy_directory(admin_startup_kit_path, os.path.join(central_node_path, 'admin'))

        # Create or modify computationParameters.json within the central node's runKit
        parameters_path = os.path.join(central_node_path, 'parameters.json')
        with open(parameters_path, 'w', encoding='utf-8') as f:
            f.write(computation_parameters)

        logger.info('RunKits created successfully.')
    except Exception as error:
        logger.error('Error creating runKits:', error)
        raise  # Rethrow or handle as needed

# Helper function to copy directories recursively
def copy_directory(src: str, dest: str) -> None:
    if os.path.exists(dest):
        shutil.rmtree(dest)  # Remove existing destination directory
    shutil.copytree(src, dest)

# Example usage:
# create_run_kits('/path/to/startupKits', '/path/to/outputDirectory', '{"param": "value"}', 'example.com', 'admin@admin.com')
