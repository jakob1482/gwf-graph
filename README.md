# gwf-graph

**Under development.**

Generates a graph visualization of the dependency graph in the gwf workflow. Optionally, the status of the targets can be included, providing insight into the workflow's current state.

<code style="color:#E0C1EF;font-size:24px">&#9632;</code> CANCELLED<br>
<code style="color:#FFB2B2;font-size:24px">&#9632;</code> FAILED<br>
<code style="color:#B2FFB2;font-size:24px">&#9632;</code> COMPLETED<br>
<code style="color:#B2EBFF;font-size:24px">&#9632;</code> RUNNING<br>
<code style="color:#FFFFB2;font-size:24px">&#9632;</code> SUBMITTED<br>
<code style="color:#D8D8D8;font-size:24px">&#9632;</code> SHOULDRUN

## Installation

Ensure the necessary dependencies `gwf` and `gwf-utilization` are installed into your Conda environment before installing the `gwf-graph` plugin. If these are not installed yet, follow the first step; otherwise, proceed directly yo the second step.

1. **Install dependencies**
    ```bash
    # Install 'gwf' and 'gwf-utilization' using Conda
    conda install gwf micknudsen::gwf-utilization
    ```

2. **Install the plugin**
    ```bash
    # Install 'gwf-graph' directly from the GitHub repository
    pip install -U git+https://github.com/jakob1482/gwf-graph.git@master
    ```

## Usage 

```console no-copy
Usage: gwf graph [OPTIONS]

  Generates a graph visualization of the dependency graph in the gwf workflow.
  Optionally, the status of the targets can be included, providing insight
  into the workflow's current state.

Options:
  -o, --output TEXT       The name (and path) of the output graph
                          visualization. Must end with a valid graphviz format
                          (e.g. png, svg, etc.). Defaults to 'workflow.png'.
  --status / --no-status  Flag to include the status (e.g., running,
                          completed, failed) of each target in the graph.
  --help                  Show this message and exit.
```
