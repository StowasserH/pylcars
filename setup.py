from setuptools import setup, find_packages

setup(
    packages=find_packages(include=['pylcars', 'pylcars.*']),
    python_requires='>=3.8',
)
