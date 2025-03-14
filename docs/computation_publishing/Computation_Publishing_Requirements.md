# Computation Module Publishing Requirements

## Technical Requirements for Dev Team Approval

To gain approval from the development team, the computation module must meet the following technical requirements:

- **Successful Execution**
  - The module must run successfully with three or more sites on the public platform using the provided test data.

- **Computation Description Document**
  - A clear and comprehensive document must be provided, including:
    - **Algorithm Description** – Explanation of the methodology used.
    - **Limitations** – Any constraints or known issues with the algorithm.
    - **Input Data Specification**:
      - Structure of the **data directory**.
      - Specification for **`parameters.json`**.
    - **Output Format Description** – Clear definition of expected outputs.
    - **Minimum Hardware & Space Requirements** – System requirements for execution.
    - **Basic Dataset Validator** – A tool or script to validate input data format.

- **GitHub Repository**
  - The module must be hosted in a **publicly accessible repository**.
  - The repository should include:
    - A **buildable, working image**.
    - **Test data** for validation. (3 or more sites)
    - The **computation description document**.
    - Automated workflows or scripts to **run test data**.

---

## PI Approval Requirements

Principal Investigators (PIs) are responsible for defining and enforcing additional requirements specific to their computation module. In addition to the general technical requirements, PIs must:

- Document their specific requirements within the computation module’s repository.
- Ensure the module meets the following suggested criteria:

  - **Accuracy & Meaningfulness of Results**
    - Verify that the module produces **valid and meaningful** computational results.
  
  - **Compatibility with Intended Datasets**
    - Confirm that the **data format specification** aligns with intended use cases.
    - Test against **multiple dataset variations** conforming to the specified format.
    - Utilize **real-world datasets** as examples.

  - **Dataset Validator Approval**
    - Approve the basic dataset validator to ensure correct input data formatting.

  - **Additional PI-Specific Requirements**
    - Define any **module-specific** criteria beyond the generic requirements.

---

## Tracking and Documenting Validation Checks

A **master validation document** must be maintained within the computation module’s repository to track approval status. This document should:

- List all **requirement items** along with their approval status.
- Maintain **timestamps and logs**, including the **identity of the approver**, for each validated requirement.
- Ensure clarity and traceability, as computation module code and documentation may evolve, potentially invalidating prior approvals.
