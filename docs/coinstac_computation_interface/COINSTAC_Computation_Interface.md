### COINSTAC Computation Interface: Directory Structure

#### Overview

Defines the directory structure for COINSTAC computation runs. Computation authors should understand the role of each directory.

#### Directory Structure

```txt
/workspace
  /data
  /runKit
  /output
  /provisioning
    /input
    /output
```

#### Directory Definitions

- **`/data`:** Read-only site-specific input data for the computation.

- **`/runKit`:** Configuration files for the computation run, including `parameters.json` on the central node.

- **`/output`:** Computation outputs, including results, logs, and error reports.

- **`/provisioning/` for the provisioning process.