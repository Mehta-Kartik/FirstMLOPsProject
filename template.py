import os
from pathlib import Path
import logging

project_name="First_End_to_End_Project"

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common. py", #it will contain most common functionality that every file contains
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", ## Configuration details
    "params.yaml",# Machine Learning
    "schema.yaml",
    "main.py",
    "DockerFile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]

for file_path in list_of_files:
    filepath=Path(file_path)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directories {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")