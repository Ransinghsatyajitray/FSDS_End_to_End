from setuptools import find_packages, setup

from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # the setup file is itself used for installing custom packages hence removing this would help us in avoiding looping of the code.
            
    return requirements        



setup(
    name = "DiamondPricePrediction",
    version = "0.0.1",
    author = "Ransingh Satyajit Ray",
    author_email = "satyajit239@gmail.com",
    install_requires = get_requirements('requirements.txt'), # or we can do manually keep the packages in a list
    packages=find_packages()
)