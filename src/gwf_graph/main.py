import click
import plotly.graph_objects as go
import regex as re
import graphviz
from graphviz import Digraph, FORMATS
from gwf import Workflow
from gwf.core import (
    CachedFilesystem,
    Context,
    get_spec_hashes,
    Graph,
    Status,
    Target,
)
from gwf.backends import create_backend
from gwf.scheduling import get_status_map
from gwf_utilization import accounting, main


STATUS_COLORS = {
    Status.CANCELLED: "#E0C1EF",
    Status.FAILED: "#FFB2B2",
    Status.COMPLETED: "#B2FFB2",
    Status.RUNNING: "#B2EBFF",
    Status.SUBMITTED: "#FFFFB2",
    Status.SHOULDRUN: "#D8D8D8",
}


def validate_output_format(
    context: click.Context, param: click.Parameter, filename: str
):
    """
    Validates that the output format is supported by graphviz.

    Args:
        context (click.Context): The click context.
        param (click.Parameter): The click parameter.
        value (str): The output format.

    Returns:
        str: The output format if it is valid.

    Raises:
        click.BadParameter: If the output format is not valid.
    """
    if filename:
        extension_match = re.match(r".*\.([a-z]+)$", filename)
        if extension_match and extension_match.group(1) in FORMATS:
            return filename
    raise click.BadParameter("Output format must be one of: " + ", ".join(FORMATS))


def create_graph(
    targets: dict[str, Target],
    dependents: dict[set],
    status_map: dict[Target, Status],
    output: str,
):
    """
    Creates a graph visualization of the dependency graph in the gwf workflow.

    Args:
        dependents (dict): A dictionary with dependent targets as keys and sets of dependency targets
                           as values.
        status_map (dict): A dictionary with targets as keys and statuses as values.
        output (str): The name (and path) of the output graph visualization. Must end with a
                      valid graphviz format (e.g. png, svg, etc.).
    """
    output_name, output_format = output.rsplit(".", 1)
    graph = Digraph(comment="Workflow", format=output_format)

    for name, target in targets.items():
        status = status_map.get(target, Status.SHOULDRUN)
        color = STATUS_COLORS.get(status, Status.SHOULDRUN)
        graph.node(
            name,
            style="rounded,filled",
            shape="rectangle",
            fillcolor=color,
        )

    for target, dependencies in dependents.items():
        for dependency in dependencies:
            graph.edge(str(target), str(dependency))

    graph.render(output_name)


# @TODO: Add target resource utilization to the graph using the gwf-utilization plugin.
@click.command()
@click.option(
    "-o",
    "--output",
    default="dependency-graph.png",
    callback=validate_output_format,
    help="The name (and path) of the output graph visualization. Must end with a valid graphviz format (e.g. png, svg, etc.), as the output format is inferred from the filename. Defaults to 'dependency-graph.png'.",
)
@click.option(
    "--status/--no-status",
    default=False,
    help="Flag to include the status (e.g., running, completed, failed) of each target in the graph.",
)
@click.pass_obj
def graph(context: Context, output, status):
    """
    Generates a graph visualization of the dependency graph in the gwf workflow. Optionally,
    the status of the targets can be included, providing insight into the workflow's current state.
    \f

    Args:
        context (gwf.core.Context): The context object from gwf.
        output (str): The name (and path) of the output graph visualization. Must end with a
                      valid graphviz format (e.g. png, svg, etc.). Defaults to 'dependency-graph.png'.
        status (bool): If true, the status of the targets will be included in the visualization.
                       Defaults to False.
    """
    workflow = Workflow.from_context(ctx=context)
    fs = CachedFilesystem()
    graph = Graph.from_targets(targets=workflow.targets, fs=fs)
    status_map = dict()

    if status:
        spec_hashes = get_spec_hashes(
            working_dir=context.working_dir, config=context.config
        )
        backend = create_backend(
            name=context.backend,
            working_dir=context.working_dir,
            config=context.config,
        )
        status_map = get_status_map(
            graph=graph, fs=fs, backend=backend, spec_hashes=spec_hashes
        )

    create_graph(
        targets=graph.targets,
        dependents=graph.dependents,
        status_map=status_map,
        output=output,
    )
