#!/usr/bin/env python

from setuptools import setup

# PACKAGE METADATA
# ##################
NAME = 'cerrado'
FULLNAME = "CERRADO"
VERSION = '0.1'
DESCRIPTION = 'Colors from Cerrado'
with open("README.rst") as f:
    LONG_DESCRIPTION = ''.join(f.readlines())
AUTHOR = '''G. Marques, M. De Pra'''
AUTHOR_EMAIL = 'gabriela.antunesm@gmail.com'
MAINTAINER = 'G. Marques'
MAINTAINER_EMAIL = AUTHOR_EMAIL
URL = 'https://github.com/gantunes/cerrado'
#LICENSE = 'MIT License'

# TO BE INSTALLED
# ##################
PACKAGES = ['cerrado',
            'cerrado.data']

PACKAGE_DATA = {
   'cerrado.data': ['styles/*',
                    'pallets/*']
}

# DEPENDENCIES
# ##################
INSTALL_REQUIRES = [
    'numpy',
    'matplotlib']

PYTHON_REQUIRES = ">=3.6"

if __name__ == '__main__':
    setup(name=NAME,
          description=DESCRIPTION,
          #   long_description=LONG_DESCRIPTION,
          version=VERSION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          # license=LICENSE,
          url=URL,
          #   platforms=PLATFORMS,
          #   scripts=SCRIPTS,
          packages=PACKAGES, 
          #   ext_modules=EXT_MODULES,
          package_data=PACKAGE_DATA,
          #   classifiers=CLASSIFIERS,
          #   keywords=KEYWORDS,
          #   cmdclass=CMDCLASS,
          install_requires=INSTALL_REQUIRES,
          python_requires=PYTHON_REQUIRES,
          )
