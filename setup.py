from setuptools import find_packages, setup
from typing import List

# remove -e as it will be read 
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str)-> List[str]:
    '''
    This function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name = 'ML_Project',
    version = '0.0.1',
    author = 'Zainab',
    author_email= 'zainab@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)

'''
-e . in requirements.txt will automatically trigger setup.py file
'''