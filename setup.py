#!/usr/bin/env python
#-*- coding:utf-8 -*-

# THE ORIGINAL WORK BELONGS TO HELLMAN
# https://github.com/hellman/libnum
# I've just ported it to python3 since the project looked inactive


from setuptools import setup
import libnum


setup(name='libnum',
      version=libnum.__version__,
      author='jafar akhondali',
      author_email='jafar.akhondali@yahoo.com',
      license='MIT',

      url='https://github.com/JafarAkhondali/python3-libnum',
      description='python3 comptaible fork for libnum - Some number theoretic functions.',
      long_description=libnum.__doc__,

      packages=['libnum', 'libnum.lib.chains'],
      provides=['libnum'],

      keywords='number prime gcd lcm modular invmod elliptic',
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   'Topic :: Security :: Cryptography',
                  ],
      )
