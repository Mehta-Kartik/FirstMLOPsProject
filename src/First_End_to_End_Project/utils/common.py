import os
import yaml
from src.First_End_to_End_Project import logger  # Import custom logger
import json
import joblib
from ensure import ensure_annotations  # Type checking decorator
from box.exceptions import BoxValueError
from box import ConfigBox  # Enhanced dictionary with dot notation
from pathlib import Path
from typing import Any

@ensure_annotations  # Enforces type hints at runtime
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads YAML file and converts to ConfigBox for easy access
    Args: path_to_yaml (Path): File path to YAML
    Raises: ValueError if file empty, other exceptions if read fails
    Returns: ConfigBox object with YAML data
    """
    try:
        # Open and safely parse YAML file
        with open(path_to_yaml) as yamlfile:
            content = yaml.safe_load(yamlfile)  # Load YAML content
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Convert to ConfigBox (dot notation access)
    except BoxValueError:  # Raised by ConfigBox when empty dict
        raise ValueError("yaml file is empty")
    except Exception as e:  # Catch any other parsing errors
        raise e




@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """
    create a list of directories

    Args:
        path_to_directories(list): list of path of directories
        ignore_log(bool,optional): Ignore if multiple dirs is to be created. Defaults to 
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    """
    save json data

    Args:
        path(Path): path to json file
        data(dict): data to be saved in json file
    """

    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    
    logger.info(f"Json file saved at: {path}")

@ensure_annotations
def save_bin(data:Any,path:Path):
    """
    save binary file

    Args:
        data(Any):data to be saved as binary
        path(Path): path to binary file
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path:Path)->Any:
    """
    load binary file

    Args:
        path(Path): path to binary file
    
    Return:
        Any:object stored in the binary file
    """

    data=joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

