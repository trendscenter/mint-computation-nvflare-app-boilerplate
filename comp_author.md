The purpose of this repository is to assist computation authors in beginning the development of NVFLARE applications and COINSTAC computations. It serves as a brief guide for:

- Developing and testing NVFLARE applications.
- Ensuring these applications are compatible with the COINSTAC platform's specifications.

Included in this repository are an example application and boilerplate code, which serve as practical starting points for creating your own applications.

# NVFLARE
## Overview
NVFLARE is an open-source federated learning tool developed by NVIDIA
You can find NVIDIA's documentation and source code here:
https://nvflare.readthedocs.io/en/main/index.html
https://github.com/NVIDIA/NVFlare


Its useful to start with an overview of the basic parts of FLARE
In the vocabulary of NVFLARE an `app` is what you'll be developing. It will contain the custom code for your specific computation.
To run a federated computation using your NVFLARE `app` you'll need basic knowledge of how to setup and operate an NVFLARE `project`.
You start by `provisioning` the project which creates a set of startup kits for the sites, the server, and an admin component to use.
One the server, sites, and admin components are launched and connected by using the scripts in their respective startup kits, you can then submit a `job` which uses your custom `app`

NVFLARE is a python package. Whether you develop your application using a container or on your local system, remember that the components will run in their own containers.
NVFLARE provides a `POC` (proof of concept) mode as a optional tool for quickly developing and testing NVFLARE apps. When developing your app using POC mode, be considerate of how the production environment of containerized computations will be different - particulalry when it comes to absolute and relative paths to directories for `data/`,  `results/` and computation parameters.
There are ways we can standardize around this to make development using POC mode not require any changes when an app runs in production.
