"""Developer commands."""
from invoke import task  # pylint: disable=import-error


@task
def setup(c):
    """Set up developer environment."""
    url = "https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py"
    c.run(f"curl -sSL {url} | python -")
    c.run("export PATH=$PATH:$HOME/.poetry/bin")
    c.run("poetry install")


@task
def pylint(c):
    """Lint code."""
    c.run("poetry run pylint sysx tests tasks.py")


@task
def black(c, check=False):
    """Format code.

    Args:
        check: If true, do not write changes back.
    """
    if check:
        c.run("poetry run black --check src tests tasks.py")
    else:
        c.run("poetry run black src tests tasks.py")


@task
def mypy(c):
    """Type-check code."""
    c.run("poetry run mypy src tests")
