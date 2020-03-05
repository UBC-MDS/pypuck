# authors: Jarvis Nederlof
# date: 2020-03-02

"""
Need to add usage, etc.
"""

import requests
import pandas as pd
import altair as alt
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
    start_date = '2019-10-02' if start_date is None else start_date
    end_date = '2020-04-11' if end_date is None else end_date

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


def attendance(regular=True, playoffs=True, start_season=None, end_season=None):
    """
    Query to the Attendance API to get the NHL's seasonal and playoff attendance numbers.
       
    Parameters
    ----------
    regular : boolean (default True).
    
    playoffs : boolean (default True)

    start_season : str (default None)
      The stat start date string in 'YYYY' format.
    end_seaon : str (default None)
      The stat end date string in 'YYYY' format.
  
    Returns
    -------
    altair.vegalite.v3.api.Chart
      It wil display attendance numbers in an Altair chart.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> pypuck.attendance(regular=True, playoffs=True, start_season=2000, end_season=2019)
        
    ...
    """
    
    # Specify the URL
    url= 'https://records.nhl.com/site/api/attendance'

    # Make the API request
    page = requests.get(url)

    df = pd.DataFrame(page.json()['data']).sort_values(by=['seasonId'])

    # Check the response code is valid - i.e. the API didn't fail
    helpers.check_response_code(page.status_code)

    df= df.fillna(0)
    df.playoffAttendance = df.playoffAttendance.astype(int)
    df.regularAttendance = df.regularAttendance.astype(int)
    df = df.rename(columns={'regularAttendance': 'regular',
                       'playoffAttendance': 'playoff'})
  
    # set start seaon and end season to default value if none
    if pd.isnull(start_season):
        start_season = 1975    

    if pd.isnull(end_season):
        end_season = 2019    
            
    # check if a proper input is given
    if type(regular) != bool:
      raise Exception('Only boolean value can be accepted')

    if type(playoffs) != bool:
      raise Exception('Only boolean value can be accepted')

    if start_season not in range (1975,2019):
      raise Exception('Start season is out of range')

    if end_season not in range (1976,2020):
      raise Exception('End season is out of range') 

    if end_season <= start_season):
      raise Exception('End season should be not be earlier than the start season') 

        
    start_season = int(str(start_season) + str(start_season))
    end_season = int(str(end_season) + str(end_season))
    df = df.query('seasonId >= @start_season and seasonId <= @end_season')
    
    
    if regular == True and playoffs == True:
        # plot both regular attendance and playoff attendance if both are requested
        
        plot1 = alt.Chart(df, title="Regular Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Seaon"),
            alt.Y('regular:Q', title = 'Regular Attendance'),
     
          
        )
        
        plot2 = alt.Chart(df, title="Playoff Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Seaon"),
            alt.Y('playoff:Q', title = 'Playoff Attendance'),
        
        )
        
        plot = (plot1 | plot2)
            
    elif regular == True:
        # plot regular attendance if it is requested only
        
        plot = alt.Chart(df, title="Regular Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Seaon"),
            alt.Y('regular:Q', title = 'Regular Attendance')
          
        )
    elif playoffs == True:
       # plot playoff attendance if it is requested only     
        plot = alt.Chart(df, title="Playoff Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Seaon"),
            alt.Y('playoff:Q', title = 'Playoff Attendance')
        )
    else:
        raise Exception('Must select at least one attendance type')
    return plot  









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
    If year is not specified, then all of the draft picks for all year will be returned. If no round is specified 
    the data frame will include all players with chosen pick number from every round.
    There are cases when even though user entered valid parameters, output would be empty 
    if a pick number didn't exist in a specified round, assert error would be raised.  

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
    #Checking if input is proper
    assert pick_number in range(1,38), 'Number of pick is out of avaliable range'
    if round_number : assert round_number in range(1, 25), 'Number of round is out of avaliable range'
    if year : assert year in range (1963,2019), 'Year is out if avaliable range'    
    
    api = requests.get("https://records.nhl.com/site/api/draft").json()
    stats = pd.DataFrame(api['data'])
        
    if round_number and year:
        query = "pickInRound == @pick_number and roundNumber == @round_number and draftYear == @year"
    elif round_number:
        query = "pickInRound == @pick_number and roundNumber == @round_number"
    elif year:
        query = "pickInRound == @pick_number and draftYear == @year"
    else:
        query = "pickInRound == @pick_number"
    
    df = stats.query(query)[['playerName', 'pickInRound', 'roundNumber', 'triCode', 'draftYear']]
    #Checking if output is valid
    assert df.empty == False, 'Specified pick number didn`t exist in specified round or year'
    return df
