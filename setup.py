#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "acpi",
    version = "1.0.0",
    url = 'https://github.com/ondrejsika/python-acpi',
    license = 'MIT',
    description = "Python acpi parser library",
    author = 'Ondrej Sika',
    author_email = 'ondrejsika@ondrejsika.com',
    py_modules = ("acpi", ),
    install_requires = (),
    include_package_data = True,
)