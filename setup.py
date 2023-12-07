# /usr/bin/python3
"""Setup script for djangocms-catalog-books."""
from distutils.command.build import build

from setuptools import setup


class CustomBuild(build):
    sub_commands = [("compile_catalog", lambda x: True)] + build.sub_commands


setup(cmdclass={"build": CustomBuild})
