#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
from os.path import dirname
from os.path import join

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def get_requirements(req_file):
    reqs = []
    with open(join(dirname(__file__), req_file),'r') as f:
        reqs.append(f.readline().rstrip())
    return reqs


setup(
    name='spec-synthase',
    version='0.1.0',
    license='MPL2',
    description='spec-synthase is a tool to help deal with big swagger files, by building the swagger specification files from little spec files. ',
    long_description=read('README.rst'),
    author='Allan Silva',
    author_email='a@allantavares.com.br',
    url='https://github.com/MicroarrayTecnologia/spec-synthase',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License','Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
        'Topic :: Utilities',
    ],
    entry_points={
        "console_scripts": {
            "specsynthase = specsynthase.cli:main",
        },
    },
    keywords=[
        'OpenAPI Specification', 'OAS', 'swagger', 'yaml', 'spec', 'api'
    ],
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('requirements-test.txt'),
    extras_require={
    },
)
