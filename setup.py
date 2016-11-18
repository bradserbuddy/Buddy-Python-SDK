# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


dependencies = ['mprop', 'Events', 'requests', 'paho-mqtt']

if sys.version_info.major < 3:
    dependencies.append('configparser')
    dependencies.append('flufl.enum')

test_extras_require = ['python-dateutil', 'mock', 'curses-check-for-keypress']

setup(
    name='buddy-python-sdk',

    version='1.0.8',

    description='The Buddy Python SDK',

    url='https://github.com/buddyplatform/Buddy-Python-SDK',

    author='Buddy Platform, Inc.',
    author_email='support@buddy.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],

    keywords='baas paas mobile iot mqtt sdk setuptools development',

    packages=find_packages(exclude=['sample', 'tests']),

    install_requires=dependencies,

    extras_require={
        'test': test_extras_require
    }
)
