from setuptools import find_packages,setup
from typing import List

HYPEN = '-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPEN in requirements:
            requirements.remove(HYPEN)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Lalit More',
    author_email='lalitmore2005@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)