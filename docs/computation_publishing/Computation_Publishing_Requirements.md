# Computation Publishing Requirements

## 1. Demonstration

The computation must demonstrate the following:

- **Work in a non-federated environment**:
  - The computation must work outside of coinstac in a non-federated environment

- **Meaningful Results**:
  - Achieves statistical significance, matches expected outcomes, or aligns with domain-specific benchmarks.
  - Consistent results across different datasets.
  - The results must be similar/comparable to non-federated environment
  - All the options in the algorithm must be tested and shown to work
  
- **Integration with the UI**:
  - Runs without errors in the COINSTAC GUI.
  - Correctly interacts with GUI components and produces expected outputs.
 
- **Error handling**:
  - Algorithm related errors must be communicated in human readable format to the end users
  - Errors include but not limited to :
    - software issues like starting Matlab, SPM, AFNi etc.
    - Incompatible datasets (null values , incompatible data sizes (nifti file resolutions etc.)
    - Algorithm unable to converge to a solution
    - Minimum required number of datasets not met
  
- **Testing**:
  COMPATIBILITY
  - The computation should be tested to work in windows, linux, mac OS's with x86_64, 64 bit architectures
  STRESS TESTING
  - The computation should be stress tested to scale.
  - Ex: Regressions, pre-processing should be clearly outline how much RAM is required for #datasets
  - Limitations should be outlined

    
## 2. Documentation

Each computation must be thoroughly documented. The documentation should include:

- **Algorithm Description**:
  - Clear explanation of what the algorithm does and its purpose.
  - Overview of the methodology and assumptions.
  - Documentation of communication between local and remote nodes as in https://github.com/trendscenter/mint-computation-nvflare-app-boilerplate/edit/main/docs/computation_publishing/Computation_Publishing_Requirements.md


- **Minimum hardware requirements and space requirements**:
  - Hardware requirements. Ex: The computation runs serially and each scan takes approximately 10 mins to run on a system with 2.3 GHz,i5 equivalent processor and 8GB RAM.
  - Space requirements: Each scan output directory takes about 150MB space after running this algorithm.



- **Input Specification**:
  - **Parameters (`parameters.json`)**:
    - Detailed description of each parameter (name, type, allowable values).
    - Example:
      ```json
      {
        "learning_rate": 0.01,
        "num_epochs": 100,
        "batch_size": 32
      }
      ```
    -If the results are heavily dependent on fine tuning the parameters this has to be mentioned in the algorithm description and must be displayed in the computation notes
    
  - **Data Format**:
    - Required files, directory structure, and any schema definitions.
    - Example:
      ```plaintext
      /data
        ├── subject1.csv
        ├── subject2.csv
      ```
    - Include a **link to test data** in the repository for users to test.
    - What type of data does the algorithm consume, modailty: smri,fmri,dti, type of mri data (12 ch /32ch) etc.
      
- **Limitations of the algorithm**:
  - Under what conditions does the algorithm work, ex: can only consume smri data, nifti format. Only include data formats that have been tested, do not assume otherwise.
  - How many minimum datasets are required for the algorithm? 
  - What are the constraints, ex for Linear regression: Data has to be independent. If multicollinearity exists in the data, then the error has to be clearly communicated
These details must be included in the computation notes in the UI. 
  
- **Output Description**:
  - Detailed description of outputs and their format.
  - Example:
    ```json
    {
      "accuracy": 0.95,
      "loss": 0.05,
      "confusion_matrix": [...]
    }
    ```

## 3. The Repository

The repository should adhere to the following requirements:

- **Public Access**:
  - The repository must be publicly accessible to ensure transparency and collaboration.
  
- **Main Branch**:
  - The main branch must always be up-to-date and capable of:
    - **Building a working image**.
    - **Running the test data** without errors.
  
- **Contents**:
  - The repository must include:
    - **Test data**: A dataset that demonstrates the computation’s functionality.
    - **Computation documentation**: Full documentation, including algorithm description, input/output specifications, and examples.

## 4. Requirements for Publishing to the COINSTAC Platform

When publishing the computation to the COINSTAC platform, the following must be included:

- **Image Download URL**:
  - A direct link to download the image, locked to a specific version.
  
- **Image Build Source**:
  - A link to the GitHub repository, pointing to the **specific commit** used to build the image.

- **Computation Documentation**:
  - The same documentation as described in the "Documentation" section, ensuring everything is clearly outlined for users.

