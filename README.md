## pypuck

#### DSCI 524 Group 6
#### By: Jarvis Nederlof, Polina Romanchenko, Zhong Xugang, Joshi Manish

![](https://github.com/jnederlo/pypuck/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/jnederlo/pypuck/branch/master/graph/badge.svg)](https://codecov.io/gh/jnederlo/pypuck) ![Release](https://github.com/jnederlo/pypuck/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pypuck/badge/?version=latest)](https://pypuck.readthedocs.io/en/latest/?badge=latest)

: Functions to access the publicly available but undocumented NHL.com API

### Purpose & Scope
The pypuck package is designed to allow users ability to get both relevant and historical statistics for NHL. As of now the package has limited functionality that can further be extended based on feedback.     

### Installation:

```
pip install -i https://test.pypi.org/simple/ pypuck
```

### Features
In this package you can find these four main functions:

- **get_curr_params**  - function that allows user to get relevant statistics for the current season for a specified team id.

### Python Ecosystem
There are varieties of nhl themed packages created for different purposes. Some of the packages that have similar functionality include [Hockey-scraper](https://github.com/HarryShomer/Hockey-Scraper), [nhlscrapi](https://pythonhosted.org/nhlscrapi/) and [nhl-score-api](https://github.com/peruukki/nhl-score-api). Our function provides functionality in a simple package and serves as a learning tool for package building.  


### Dependencies
- Python 3.7.4 and Python packages:
      - requests==2.22.0
      - pandas==0.25.2
      - numpy==1.17.2

### Usage
- TODO


### Documentation
The official documentation is hosted on Read the Docs: <https://pypuck.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
