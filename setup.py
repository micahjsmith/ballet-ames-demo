from setuptools import setup, find_packages

requirements = [
    'ballet @ git+https://git@github.com/HDI-Project/ballet@master',
    'Click>=6.0',
    'pip>=18.1'
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
