# gwf-graph

**Under development.**

Generates a graph visualization of the dependency graph in the gwf workflow. Optionally, the status of the targets can be included, providing insight into the workflow's current state.

<img src="https://raw.githubusercontent.com/jakob1482/gwf-graph/master/assets/status_colors/cancelled.svg" width="12px">&nbsp; CANCELLED<br>
<img src="https://raw.githubusercontent.com/jakob1482/gwf-graph/master/assets/status_colors/failed.svg" width="12px">&nbsp; FAILED<br>
<img src="https://raw.githubusercontent.com/jakob1482/gwf-graph/master/assets/status_colors/completed.svg" width="12px">&nbsp; COMPLETED<br>
<img src="https://raw.githubusercontent.com/jakob1482/gwf-graph/master/assets/status_colors/running.svg" width="12px">&nbsp; RUNNING<br>
<img src="https://raw.githubusercontent.com/jakob1482/gwf-graph/master/assets/status_colors/submitted.svg" width="12px">&nbsp; SUBMITTED<br>
<img src="https://raw.githubusercontent.com/jakob1482/gwf-graph/master/assets/status_colors/shouldrun.svg" width="12px">&nbsp; SHOULDRUN

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

```{: .console .no-copy}
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
