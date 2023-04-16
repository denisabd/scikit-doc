from setuptools import setup
import os

with open('README.md', 'r') as fh:
   long_description = fh.read()
  
setup(
  name = 'skdoc',
  version = '0.0.1.2',
  author = ['Denis Abdullin', 'Emile Antat'],
  author_email = 'denisabdullincz@gmail.com',
  description = 'Automated documentation engine for scikit-learn models',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  py_modules = ['placeholder'
    ],
  package_dir = {'': 'src'},
  install_requires = ['pandas >= 1.0.0', 'scikit-learn >= 1.0.0', 'quarto', 'papermill >= 2.0.0'],
  extras_require = {'dev': ['pytest >= 3.7']},
  keywords = ['python', 'scikit-learn', 'sklearn', 'machine learning', 'documentation'],
  classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Operating System :: OS Independent"
  ]
)
