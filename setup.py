#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="sqlalchemy-aurora-data-api",
    version="0.0.1",
    url='https://github.com/chanzuckerberg/sqlalchemy-aurora-data-api',
    license='Apache Software License',
    author='Andrey Kislyuk',
    author_email='akislyuk@chanzuckerberg.com',
    description='An AWS Aurora Serverless Data API dialect for SQLAlchemy',
    long_description=open('README.rst').read(),
    install_requires=[
        'sqlalchemy',
        'aurora-data-api'
    ],
    extras_require={
    },
    packages=find_packages(exclude=['test']),
    entry_points={
        'sqlalchemy.dialects': [
            'mysql.auroradataapi = sqlalchemy_aurora_data_api:AuroraMySQLDataAPIDialect',
            'postgresql.auroradataapi = sqlalchemy_aurora_data_api:AuroraPostgresDataAPIDialect'
        ]
    },
    platforms=['MacOS X', 'Posix'],
    test_suite='test',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
