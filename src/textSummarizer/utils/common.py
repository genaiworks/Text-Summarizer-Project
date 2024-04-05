import os
from box.exceptions import  BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """Read a YAML file and return a ConfigBox object.
    Parameters
    ----------
    path : Path
        Path to the YAML file.
    Returns
    -------
    ConfigBox
        A ConfigBox object.
    Raises
    ------
    BoxValueError
        If the YAML file cannot be read.
    """
    with open(path, "r") as f:
        try:
            content = yaml.safe_load(f)
            logger.info(f"Read YAML file: {path}")
            return ConfigBox(content)
        except yaml.YAMLError as e:
            raise BoxValueError(f"Cannot read YAML file: {e}")
        
@ensure_annotations
def create_directories(path_to_directorier: list, verbose=True):
    """ create list of directories
    Args:
        path_to_directorier (list): list of paths of directories to be created.
    """
    for path in path_to_directorier:
        if not os.path.exists(path):
            os.makedirs(path)   
            if verbose:
                logger.info(f"Created directory: {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file.
    Parameters
    ----------
    path : Path
        Path to the file.
    Returns
    -------
    str
        The size of the file.
    Raises
    ------
    BoxValueError
        If the file cannot be read.
    """
    try:
        size = os.path.getsize(path)
        return f"{size} bytes"
    except OSError as e:
        raise BoxValueError(f"Cannot read file: {e}") from e


