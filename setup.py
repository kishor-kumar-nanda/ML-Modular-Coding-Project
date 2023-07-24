from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "ML MODULAR CODING PROJECT"
VERSION = "0.0.1"
AUTHOR = "KISHOR"
DESCRIPTION = "A Machine Learning Project with modular coding"
AUTHOR_EMAIL = "kishorkumarnanda01@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
      with open(REQUIREMENTS_FILE_NAME) as f:
            requirements = f.readlines()
            requirements = [requirement_package.replace("\n","") for requirement_package in requirements]
            if HYPHEN_E_DOT in requirements:
                  requirements.remove(HYPHEN_E_DOT)
            return requirements

       

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements()
     )
