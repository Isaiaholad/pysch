#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'pysc',
    version = '0.1',
    description = '',
    py_modules =['pysc'],
    package_dir = {'pysc': 'pysc'},
    package_data = {},
    packages = find_packages(),
    scripts = ['pysc.py'],
    install_requires = ['paramiko', 'pykeepass', 'pyyaml', 'click'],
)

# python keepass ssh connection manager
# pkscm pysch pyshch pysshch pysch
