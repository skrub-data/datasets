import os
from setuptools import setup, find_packages

description_file = os.path.join(os.path.dirname(__file__), 'README.md')
with open(description_file) as fh:
    DESCRIPTION = fh.read()


if __name__ == '__main__':
    setup(name='datasets',
          version='0.0.1',
          author='Patricio Cerda',
          author_email='patricio.cerda@inria.fr',
          description=("Datasets for prediction with string categorical variables"),
          long_description=DESCRIPTION,
          license='BSD',
          classifiers=[
              'Environment :: Console',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: BSD License',
              'Operating System :: OS Independent',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Topic :: Scientific/Engineering',
              'Topic :: Software Development :: Libraries',
          ],
          platforms='any',
          packages=find_packages(),
          install_requires=['pandas', 'requests'],
          )
