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
Its useful to start with an overview of the basic parts of FLARE

### The NVFLARE App
In NVFLARE terminology, an `app` represents the specific computation or learning model you develop. It encapsulates the custom logic and algorithms necessary for your federated learning computation.

### The NVFLARE Project
A successful federated learning project requires setting up and managing an NVFLARE project, which includes:

- Provisioning: Initiating a project creates startup kits for various components (sites, server, and admin) necessary for your federated network.
- Deployment: Launching and connecting the server, sites, and admin components using scripts provided in the startup kits.
- Execution: Submitting a job that runs your custom app across the federated network.

### Development Environment:

NVFLARE is a python package.
NVFLARE projects can be developed both in containerized environments and on local systems, with the final deployment running in containers.
 
#### Proof of Concept (POC) Mode
NVFLARE offers a `POC` mode as an optional tool for rapid development and testing of NVFLARE apps. While POC mode simplifies the initial development process, it's important to consider the differences between the POC environment and the production environment in containers, particularly regarding file paths (data/, results/, and computation parameters). Standardizing development practices can minimize these differences, ensuring a smooth transition from POC to production.

#### NVFLARE Simulator