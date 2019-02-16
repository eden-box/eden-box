#! usr/bin/env python3.7

from setuptools import setup, find_packages

setup(
    name='activity_analyser',

    version='0.5.0',

    description='Fetches activities from an API and sends relevant information to a database.',

    url='<project github page URL>',  # TODO add project github URL

    author='Eden-Box',

    author_email='eden.box@outlook.com',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Nextcloud Activity API consumption Tool',

        # TODO choose project license
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',

        'Programming Language :: Python :: 3.7',

        'Natural Language :: English',
    ],

    keywords='nextcloud api activity filter python',

    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=[
        'pyyaml',
        'psycopg2',
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
    # `pip` to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'activity_analyser=activity_analyser:main',
        ],
    },

    project_urls={  # TODO add project github URL
        'Source': '<project github page URL>'
    }
)
