import json
import os
import logging
from provision.provision_run import provision_run

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def load_provision_input(provision_input_path: str) -> dict:
    try:
        with open(provision_input_path, 'r') as file:
            provision_input = json.load(file)
        logger.info(f"Run provision input loaded from {provision_input_path}")
        return provision_input
    except Exception as e:
        logger.error(f"Failed to load run provision input: {e}")
        raise

def main():
    provision_input_path = '/path/to/provision_input.json'  # Replace with the actual path

    # Load run provision input
    provision_input = load_provision_input(provision_input_path)

    # Extract arguments
    user_ids = provision_input.get('user_ids')
    path_run = provision_input.get('path_run')
    computation_parameters = provision_input.get('computation_parameters')
    fed_learn_port = provision_input.get('fed_learn_port')
    admin_port = provision_input.get('admin_port')
    host_identifier = provision_input.get('host_identifier')

    # Call the provision_run function with the loaded arguments
    provision_run(
        user_ids=user_ids,
        path_run=path_run,
        computation_parameters=computation_parameters,
        fed_learn_port=fed_learn_port,
        admin_port=admin_port,
        host_identifier=host_identifier
    )

if __name__ == '__main__':
    main()
