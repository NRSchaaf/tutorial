from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n", "") for req in requirements] # replaces /n from each line in requirements.txt
        
        if HYPEN_E_DOT in requirements: 
            requirements.remove(HYPEN_E_DOT)   # removes -e . which marks end of requriements.txt file

setup(
    name='injury_data_regression',
    version='0.0.1',
    author='Nathan Schaaf',
    author_email='nathan.rocky.schaaf@gmail.com',
    packages=find_packages(),
    description='Description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NRSchaaf/injury_data_regression.git',
    license='none',
    #classifiers=[
    #    'Development Status :: 3 - Alpha',
    #    'Intended Audience :: Developers',
    #    'License :: OSI Approved :: MIT License',
    #    'Programming Language :: Python :: 3',
    #    'Programming Language :: Python :: 3.6',
    #    'Programming Language :: Python :: 3.7',
    #    'Programming Language :: Python :: 3.8',
    #    'Programming Language :: Python :: 3.9',
    #], 
   
    install_requires=get_requirements('requirements.txt')
    
    #python_requires='>=3.6',
)