from setuptools import setup, find_packages

def read_req():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name = 'trello',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    install_requires = read_req(),
    entry_points='''
        [console_scripts]
        trello=trello.cli:cli
    '''
)