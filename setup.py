# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-game-prototype',
    version='0.0.1',
    description='game prototypes to test some ideas',
    long_description=readme,
    author='Rémi Boivin',
    author_email='remi.boivin@epitech.eu',
    url='https://github.com/remi-boivin/python-game-prototype',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

