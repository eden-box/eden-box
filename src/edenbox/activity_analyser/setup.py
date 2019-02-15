#! usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='activity_analyser',

    version='0.1.0',

    description='Fetches activities from an API and sends relevant information to a database.',

    url='<project github page URL>',  # TODO add project github URL

    author='Eden-Box',

    author_email='eden.box@outlook.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: API consumer Tool',

        # TODO choose project license
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
    ],

    keywords='log parser python',

    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=[
        'PyYAML',
        'Psycopg2',
        'aiohttp',
        'xmltodict',
        'python-dateutil'
    ],

    tests_require=[
        'pytest',
        'mock',
        'pytest-mock',
        'pytest-asyncio',
        'xmltodict'
    ],

    extras_require={
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    entry_points={
        'console_scripts': [
            'run=run:main',
        ],
    },

    project_urls={  # TODO add project github URL
        'Source': '<project github page URL>'
    }
)
