from setuptools import find_packages,setup #root directory will be searched for packages
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read the requirements and append each requirements in requirement_list variable.
    """
    return requirement_list

setup(

    name="sensor",
    version="0.0.1",
    author="Ashwin",
    author_email="ashwinambore23@gmail.com",
    packages = find_packages(),
    install_requires =get_requirements(), # ["pymongo==4.2.0"],
)
