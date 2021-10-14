"""The System X CLI."""
import click


@click.group()
def cli():
    """Top-level command."""


@click.command()
def deploy():
    """Deploy the service to System X."""


cli.add_command(deploy)
