# authors: Jarvis Nederlof
# date: 2020-03-02

"""
Need to add usage, etc.
"""

import requests
import pandas as pd
from pypuck.helpers import helpers

def player_stats(start_date=None, end_date=None):
    """
    Query the top 100 player's stats (sorted by total points)
    from the players summary report endpoint on the NHL.com API.

    The stats are queried on an aggregated game-by-game basis
    for a range of dates. If no date is specified the function will return
    the players stats for the current season. The stats to be
    returned are restricted to the regular season.

    The function will return the current season's stats if the arguments
    are blank (i.e. left as None).

    Parameters
    ----------
    start_date : str (default None).
      The stat start date string in 'YYYY-MM-DD' format.
    end_date : str (default None)
      The stat end date string in 'YYYY-MM-DD' format.

    Returns
    -------
    pandas.core.DataFrame
      The player's stats in a dataframe sorted by total points.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> pypuck.player_stats(start_date='2019-10-02', end_date='2020-02-28')
    PlayerName     | Goals | Assists | Points | ...
    -------------------------------------------
    Connor Mcdavid |   35  |    53   |   88   | ...
    -------------------------------------------
    ...
    """
    # Set dates to current season if none
    if start_date is None:
        start_date = '2019-10-02'
    if end_date is None:
        end_date = '2020-04-11'

    # Check that the arguments are of the correct type, in the correct format, and in the correct order
    helpers.check_argument_type(start_date, 'start_date', str)
    helpers.check_argument_type(end_date, 'end_date', str)
    helpers.check_date_format(start_date)
    helpers.check_date_format(end_date)
    helpers.check_date(start_date, end_date)

    # Specify the URL
    url = 'https://api.nhle.com/stats/rest/en/skater/summary?' +\
            'isAggregate=true&' +\
            'isGame=true&' +\
            'sort=[{"property":"points","direction":"DESC"},' +\
            '{"property":"goals","direction":"DESC"},' +\
            '{"property":"assists","direction":"DESC"}]&' +\
            'start=0&' +\
            'limit=100&' +\
            'factCayenneExp=gamesPlayed>=1&' +\
            f'cayenneExp=gameDate<="{end_date}" and gameDate>="{start_date}" and gameTypeId=2'

    # Make the API request
    page = requests.get(url)

    # Check the response code is valid - i.e. the API didn't fail
    helpers.check_response_code(page.status_code)

    # Return the top 100 players dataframe
    return pd.DataFrame(page.json()['data'])


def attendance(regular=True, playoffs=True, season=None):
    """
    Query to the Attendance API to get the NHL's seasonal and playoff attendance numbers.
       



    Parameters
    ----------
    regular : boolean (default True).
    
    playoffs : boolean (default True)
  
    season : str (default None)
  

    Returns
    -------
    altair.vegalite.v3.api.Chart
      It wil display attendance numbers in an Altair chart.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> pypuck.attendance(regular=True, playoffs=True, season='2019-02')
        
    ...
    """
    pass



def team_stats(start_season=None, end_season=None):
    """
    Get team season stats specified by start year or start year and end year.
    If no year is specified then the year 2019-2020 is default.
    If an end year is specified then the start year is also to be provided.
    year is to be provided in a 2 year format of YYYYYYYY.
    
    Parameters
    ----------
      start_season : str
        The stat start year string in 'YYYYYYYY' format.
      end_season : str
        The stat end year string in 'YYYYYYYY' format.

    Returns
    -------
    pandas.core.DataFrame
      The team's seasonal stats in a dataframe.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> start_season = '19801981'
    >>> end_season = '19891990'
    >>> pypuck.team_stats(start_season=start_season, end_season=end_season)
    Team            | Wins | Losses | OT | Points | ...
    ------------------------------------------------
    Edmonton Oilers |  34  |   23   |  5 |   73   | ...
    ------------------------------------------------
    """
    pass


def draft_pick(pick_number = 1, round_number=None, year=None):
    """
    The function returns information about draft picks for the specified parameters and stores them in a pandas data frame.
    If year is not specified then all of the draft picks for that year will be returned. If no round is specified 
    the dataframe will include all of the players with chosen pick number from every round.

    Parameters:
    ------------------------
      pick_number : int
        Desired pick number, must be in the range [1,38]. If nothing is specified, picks first draft in all rounds. 
      round_number : int
        Desired round number, must be in the range [1,25]
      year : str
        Year in which a draft took place. Must be 'YYYY' format, that contains year in a range [1963,2019]

    Returns:
    ------------------------
    draft_df : pd.DataFrame
        Drafts with specified parameters.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> pick_number = 9
    >>> round_number = 7 
    >>> year = 2000 
    >>> pypuck.draft_pick(pick_number = pick_number, round_number=round_number, year=year)

    Player            | Round_num | Pick_num | Tri_code | Year | ...
    ------------------------------------------------
    Tim Eriksson      |     7     |    9     |   LAK    | 2000 | ...
    ------------------------------------------------
    """
    pass
