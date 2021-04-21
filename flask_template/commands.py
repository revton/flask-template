# -*- coding: utf-8 -*-
"""Click commands."""
import os
from glob import glob
from subprocess import call

import click


@click.command()
def lint():
    """Lint and check code style with black, flake8 and isort."""
    files_and_directories = _files_and_directories()
    isort_args = []
    black_args = []
    _execute_tool(
        "Fixing import order", files_and_directories, "isort", *isort_args
    )
    _execute_tool(
        "Formatting style", files_and_directories, "black", *black_args
    )
    _execute_tool("Checking code style", files_and_directories, "flake8")


@click.command()
def coverage():
    """ Run/ Report/ HTML Coverage Tests."""
    # RUN
    coverage_run_args = ["run", "--source=flask_template", "-m", "pytest", "-v"]
    _execute_tool("Checking coverage", [], "coverage", *coverage_run_args)
    # REPORT
    coverage_report_args = ["report"]
    _execute_tool("Report coverage", [], "coverage", *coverage_report_args)
    # HTML
    coverage_html_args = ["html"]
    _execute_tool("HTML coverage", [], "coverage", *coverage_html_args)


@click.command()
def radon():
    """ Checks Cyclomatic Complexity and Halstead metrics."""
    files_and_directories = _files_and_directories()
    # Cyclomatic Complexity
    radon_cc_args = ["cc", "-a", "-s", "-na"]
    _execute_tool(
        "Checking cyclomatic complexity",
        files_and_directories,
        "radon",
        *radon_cc_args,
    )
    # Halstead metrics
    radon_mi_args = ["mi"]
    _execute_tool(
        "Checking Halstead metrics",
        files_and_directories,
        "radon",
        *radon_mi_args,
    )


@click.command()
def safety():
    """ Checks your installed dependencies for known security vulnerabilitie."""
    safety_args = ["check"]
    _execute_tool("Checking installed dependencies", [], "safety", *safety_args)


@click.command()
def dynaconf_validate():
    """ Checks validation of settings parameters."""
    dynaconf_args = ["validate"]
    _execute_tool(
        "Checking validation of settings parameters",
        [],
        "dynaconf",
        *dynaconf_args,
    )


@click.command()
def behave():
    """ Run Behave Tests  """
    _execute_tool("Checking behaviour tests", [], "behave", [])


def _execute_tool(description: str, files_and_directories: list, *args: list):
    """Execute a checking tool with its arguments."""
    command_line = list(args) + files_and_directories
    click.echo(f"{description}: {' '.join(command_line)}")
    rv = call(command_line)
    if rv != 0:
        exit(rv)


def _files_and_directories() -> list:
    """ Get files and directories in your root_directory."""
    # Directory not necessary lint and check code style
    skip = ["htmlcov", "logs", "dist"]
    root_files = glob("*.py")
    root_directories = [
        name for name in next(os.walk("."))[1] if not name.startswith(".")
    ]
    files_and_directories = [
        arg for arg in root_files + root_directories if arg not in skip
    ]
    return files_and_directories
