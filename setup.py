from setuptools import setup, find_packages
import sys, os

version = '0.1a1'

setup(name='mmmanip',
      version=version,
      description="Tools for manipulating a mailman list (subscribe, query, remove) via HTTP",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='',
      author='Ralph Bean',
      author_email='ralph.bean@gmail.com',
      url='http://github.com/ralphbean/mmmanip',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'twill',
          'ClientForm',
          'BeautifulSoup',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
