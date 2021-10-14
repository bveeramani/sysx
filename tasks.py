"""Developer commands."""
from invoke import task  # pylint: disable=import-error


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


@task
def pytest(c):
    """Run tests."""
    c.run("poetry run pytest tests")


@task
def bandit(c):
    """Check for security issues."""
    c.run("poetry run bandit -r src")
