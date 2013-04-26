#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'douban-client',
    version = '0.0.5',
    keywords = ('Douban', 'OAuth2', 'Douban API'),
    description = 'Python client library for Douban APIs (OAuth 2.0)',
    long_description = 'See http://liluo.github.com/douban-client',
    license = 'MIT License',

    url = 'http://liluo.github.com/douban-client',
    author = 'liluo',
    author_email = 'i@liluo.org',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = ['py-oauth2>=0.0.5'],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
