# gwf-graph

**Under development.**

Generates a graph visualization of the dependency graph in the gwf workflow. Optionally, the status of the targets can be included, providing insight into the workflow's current state.

<style>
  .status-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 0px 24px;
    list-style-type: none;
    padding: 0;
    margin: 0 4px;
  }
  .status-item {
    display: flex;
    align-items: center;
  }
  .bullet {
    font-size: 24px;
    margin-right: 12px;
  }
</style>
<ul class="status-grid">
  <li class="status-item"><span class="bullet" style="color:#E0C1EF">&#9632;</span>CANCELLED</li>
  <li class="status-item"><span class="bullet" style="color:#FFB2B2">&#9632;</span>FAILED</li>
  <li class="status-item"><span class="bullet" style="color:#B2FFB2">&#9632;</span>COMPLETED</li>
  <li class="status-item"><span class="bullet" style="color:#B2EBFF">&#9632;</span>RUNNING</li>
  <li class="status-item"><span class="bullet" style="color:#FFFFB2">&#9632;</span>SUBMITTED</li>
  <li class="status-item"><span class="bullet" style="color:#D8D8D8">&#9632;</span>SHOULDRUN</li>
</ul>

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
