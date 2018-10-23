from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='config_parser',
      version=version,
      description="config parser tool",
      long_description="""\
config parser tool""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='config parser',
      author='liuguanglu',
      author_email='liuguanglu@xiaomi.com',
      url='None',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      py_modules=['config_parser'],
      zip_safe=False,
      install_requires=[
          "pyyaml"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
