#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='mdorrst',
    version='0.1.0',
    description="Tell appart Markdown and reStructuredText.",
    long_description=readme + '\n\n' + history,
    author="Julien Palard",
    author_email='julien@palard.fr',
    url='https://github.com/JulienPalard/mdorrst',
    packages=[
        'mdorrst',
    ],
    package_dir={'mdorrst':
                 'mdorrst'},
    entry_points={
        'console_scripts': [
            'mdorrst=mdorrst.mdorrst:run'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='mdorrst',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
