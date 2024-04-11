# gwf-graph

Generates a graph visualization of the dependency graph in the gwf workflow. Optionally, the status of the targets can be included, providing insight into the workflow's current state.

## Installation

To install the `gwf-graph` plugin into your current Python or Conda environment, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/jakob1482/gwf-graph.git
    ```

2. Change into the `gwf-graph` directory:

    ```bash
    cd gwf-graph
    ```

3. Install the plugin using `pip`:

    ```bash
    pip install .
    ```

## Usage

Use the command `gwf graph` to generate a graph visualization of the dependency graph in your gwf workflow.

```console
gwf graph [OPTIONS]

  Generates a graph visualization of the target dependencies in the gwf
  workflow. Optionally, the status of the targets can be included, providing
  insight into the workflow's current state.

Options:
  -o, --output TEXT       The name (and path) of the output graph
                          visualization. Must end with a valid graphviz format
                          (e.g. png, svg, etc.). Defaults to 'workflow.png'.
  --status / --no-status  Flag to include the status (e.g., running,
                          completed, failed) of each target in the graph.
  --help                  Show this message and exit.
```