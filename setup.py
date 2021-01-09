#!/usr/bin/env python

from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    requirements=requirements_file.readlines()

setup(
    name='example-docker-flask',
    author='Chris Lesiw',
    author_email='Christopher.Lesiw@icims.com',
    version='0.1.0',
    description='',
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest',
            'pytest_mock'
        ]
    },
    packages=find_packages()
)
