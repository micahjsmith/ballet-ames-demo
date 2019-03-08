from setuptools import setup, find_packages

requirements = [
    'ballet>=0.5.1',
    'Click>=6.0',
]

setup(
    author='Micah Smith',
    author_email='micahs@mit.edu',
    entry_points={
        'console_scripts': ['ames-engineer-features=ames.features:main'],
    },
    install_requires=requirements,
    name='ballet-ames-demo',
    packages=find_packages(include=['ames', 'ames.*']),
    url='https://github.com/micahjsmith/ames',
)
