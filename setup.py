#!/usr/bin/env python

import io
from setuptools import setup

with io.open('README.rst', encoding='utf-8') as f:
    README = f.read()

setup(
    name='Flask-Walrus',
    version='0.0.1',
    url='https://github.com/jajohnsen/flask-walrus',
    author='John Arne Johnsen',
    author_email='chileohopen@gmail.com',
    maintainer='John Arne Johnsen',
    maintainer_email='chileohopen@gmail.com',
    download_url='https://github.com/jajohnsen/flask-walrus/releases',
    description='Walrus (redis) extension for Flask Applications',
    long_description=README,
    packages=['flask_redis'],
    package_data={'': ['LICENSE']},
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.0',
        'redis>=2.7.6',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
