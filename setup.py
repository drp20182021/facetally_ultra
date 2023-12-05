from setuptools import setup, find_packages

# setup
with open("requirements.txt", "r") as file:
    lines = file.readlines()
reqs = [each.strip() for each in lines]

setup(name="facetally", install_requires=reqs, packages=find_packages())
