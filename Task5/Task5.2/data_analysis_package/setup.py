from setuptools import setup, find_packages

setup(
    name='data_analysis_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'scipy',
    ],
    description='A data analysis package for cleaning, visualization, and statistics.',
    author='Your Name',
)
