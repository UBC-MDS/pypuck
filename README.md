<img src="img/pypuck_logo.png" width="150" align = "right">

# PyPuck

![](https://github.com/UBC-MDS/pypuck/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pypuck/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pypuck) ![Release](https://github.com/UBC-MDS/pypuck/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/pypuck/badge/?version=latest)](https://pypuck.readthedocs.io/en/latest/?badge=latest)

: Functions to access the publicly available but undocumented NHL.com API so that you can will all the money in the hockey pool...

### Purpose & Scope
The pypuck package is designed to allow users ability to get both relevant and historical statistics for NHL. As of now the package has limited functionality that can further be extended based on feedback.     

### Installation:

```
pip install -i https://test.pypi.org/simple/ pypuck
```

### Features

- `player_stats(start_date=None, end_date=None)`:
	- The `player_stats()` function makes an API call to the player summary endpoint on the NHL.com API. The function returns the top 100 player stats for a given date range as sorted by total points.
- `team_stats(start_season=None, end_season=None)`:
	- The `team_stats()` function makes an API call to the team summary endpoint on the NHL.com API. The function returns team seasonal stats for given seasons sorted by total team points.
- `draft_pick(pick_number=None, round_number=None, year=None)`:
	- The `draft_pick(pick_number=None, round_number=None, year=None)` function makes an API call to the drafts summary on the NHL.com API. The function returns information about draft picks for the specified arguments and stores them in a pandas data frame. 

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
