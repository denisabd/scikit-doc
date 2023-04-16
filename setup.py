from setuptools import setup, find_packages
import os

with open('README.md', 'r') as fh:
   long_description = fh.read()
  
setup(
  name = 'skdoc',
  version = '0.0.1.5',
  author = 'Denis Abdullin, Emile Antat',
  author_email = 'denisabdullincz@gmail.com, eoea754@gmail.com',
  description = 'Automated documentation engine for scikit-learn models',
  long_description_content_type = 'text/markdown',
  long_description = long_description,
  packages = find_packages(),
  install_requires = [
   'pandas >= 1.0.0', 
   'scikit-learn >= 1.0.0', 
   'quarto', 
   'subprocess',
   'pyecharts',
   'webbrowser'],
  extras_require = {'dev': ['pytest >= 3.7']},
  keywords = ['python', 'scikit-learn', 'sklearn', 'machine learning', 'documentation'],
  classifiers = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows"
  ]
)
