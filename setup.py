'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''
 
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]: 
    """
    Thiss function will return list of requirements
    
    """
    requirements_lst:List[str] = [] 
    try:
        with open("requirements.txt") as file: #open the requirements.txt file
            #readlines() reads all lines from the file and returns a list of strings
            lines = file.readlines() #read all lines from the file
            # Process each line in the requirements file
            for line in lines:
                requirement = line.strip() #strip() removes any leading and trailing whitespace characters

                ## ignore empty lines and comments
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement) #append the requirement to the list
            
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")
    
setup(
    name="Network Security", #name of the project
    version="0.0.1", #version of the project
    author="Jeebesh Chandra Podder", #author of the project
    author_email="jeebeshchandrapodder@gmail.com", #author email
    packages=find_packages(), #find all packages in the project
    install_requires=get_requirements('requirements.txt') #install all requirements
)