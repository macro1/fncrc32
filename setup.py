#!/usr/bin/env python

import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    package_data = {}
    exec(read("fncrc32.py"), package_data)
    return package_data.get('__version__')


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

setup(
    name="fncrc32",
    version=get_version(),
    author="Micah Denbraver",
    description="FileName CRC32 tool",
    license="MIT",
    url="https://github.com/macro1/fncrc32",
    py_modules=["fncrc32"],
    install_requires=["click"],
    entry_points={
        'console_scripts': [
            "fncrc32 = fncrc32:main",
        ]
    },
    tests_require=["tox"],
    cmdclass={'test': Tox},
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
    ]
)
