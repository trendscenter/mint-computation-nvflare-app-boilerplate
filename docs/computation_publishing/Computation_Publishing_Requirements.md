# Computation Publishing Requirements

## 1. Demonstration

The computation must demonstrate the following:

- **Meaningful Results**:
  - Achieves statistical significance, matches expected outcomes, or aligns with domain-specific benchmarks.
  - Consistent results across different datasets.
  
- **Integration with the UI**:
  - Runs without errors in the COINSTAC GUI.
  - Correctly interacts with GUI components and produces expected outputs.

## 2. Documentation

Each computation must be thoroughly documented. The documentation should include:

- **Algorithm Description**:
  - Clear explanation of what the algorithm does and its purpose.
  - Overview of the methodology and assumptions.
  
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
  - **Data Format**:
    - Required files, directory structure, and any schema definitions.
    - Example:
      ```plaintext
      /data
        ├── subject1.csv
        ├── subject2.csv
      ```
    - Include a **link to test data** in the repository for users to test.

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

