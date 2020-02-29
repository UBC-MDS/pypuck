def season_stats(start_season=None, end_season = None):
    """
    Get a seasons stats specified by start year or start year and end year.
    If no year is specified then the year 2019-2020 is default.
    If an end year is specified then the start year is also to be provided.
    year is to be provided in a 2 year format of YYYYYYYY 
	
    Parameters
    ----------
	    start_season : str
	      The stat start year string in 'YYYYYYYY' format.
	    end_date : str
	      The stat end year string in 'YYYYYYYY' format.

    Returns
    -------
    pandas.core.DataFrame
    The season stats in a dataframe.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> start_season = '19801981'
    >>> end_season = '19891990'
    >>> pypuck.season_stats(start_season=start_season, end_season=end_season)
    Team            | Wins | Losses | OT | Points | ...
    ------------------------------------------------
    Edmonton Oilers |  34  |   23   |  5 |   73   | ...
    ------------------------------------------------
    """