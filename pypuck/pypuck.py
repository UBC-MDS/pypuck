# authors: Jarvis Nederlof
# date: 2020-03-02

"""
The pypuck functions are used as wrapper functions to call the NHL.com
publicly available API's.
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

    The valid dates range from the start of the 1917 season until the
    current day.

    The function will return the current season's stats if the arguments
    are blank (i.e. left as None).

    You can find the glossary pertaining to the returned
    columns by going to http://www.nhl.com/stats/glossary.

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
    assists | evGoals | evPoints | faceoffWinPct | ...
    --------------------------------------------------
       67   |    27   |    66    |    0.51641    | ...
    --------------------------------------------------
    ...
    """
    # Set dates to current season if none
    start_date = '2019-10-02' if start_date is None else start_date
    end_date = '2020-04-11' if end_date is None else end_date

    # Check that the arguments are of the correct type,
    #  in the correct format, and in the correct order
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
          f'cayenneExp=gameDate<="{end_date}" and ' +\
          f'gameDate>="{start_date}" and gameTypeId=2'

    # Make the API request
    page = requests.get(url)

    # Check the response code is valid - i.e. the API didn't fail
    helpers.check_response_code(page.status_code)

    # Return the top 100 players dataframe
    return pd.DataFrame(page.json()['data'])


def attendance(regular=True, playoffs=True,
               start_season=None, end_season=None):
    """
    Query the NHL attendance number from 1975 to 2019 from the NHL records API.
    The attendance represents annual attendance numbers for all teams.

    The user can specify to return either the regular season attendance,
    playoff attendance numbers, or both.

    The function will display a chart showing the attendance over the
    specified time period.

    Parameters
    ----------
    regular : boolean (default True).
        Whether to query seasonal regular season attendance data.
    playoffs : boolean (default True)
        Whether to query seasonal playoff attendance data.

    start_season : int (default None)
      The start season is integer ranging from 1975 to 2018.
    end_season : int (default None)
      The end season is integer ranging from 1976 to 2019.

    Returns
    -------
    altair.vegalite.v3.api.Chart
      It wil display attendance numbers in an Altair chart.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> pypuck.attendance(regular=True, playoffs=True,
                          start_season=2000, end_season=2019)
    ...
    """

    # Specify the URL
    url = 'https://records.nhl.com/site/api/attendance'

    # Make the API request
    page = requests.get(url)

    # Check the response code is valid - i.e. the API didn't fail
    helpers.check_response_code(page.status_code)

    df = pd.DataFrame(page.json()['data']).sort_values(by=['seasonId'])

    df = df.fillna(0)
    df.playoffAttendance = df.playoffAttendance.astype(int)
    df.regularAttendance = df.regularAttendance.astype(int)
    df = df.rename(columns={'regularAttendance': 'regular',
                            'playoffAttendance': 'playoff'})

    # set start season and end season to default value if none
    if pd.isnull(start_season):
        start_season = 1975

    if pd.isnull(end_season):
        end_season = 2019

    # check if a proper input is given
    helpers.check_argument_type(regular, 'regular', bool)
    helpers.check_argument_type(playoffs, 'playoffs', bool)

    if start_season not in range(1975, 2019):
        raise Exception('Start season is out of range')

    if end_season not in range(1976, 2020):
        raise Exception('End season is out of range')

    if end_season <= start_season:
        raise Exception('End season should be not be '
                        'earlier than the start season')

    start_season = int(str(start_season) + str(start_season))
    end_season = int(str(end_season) + str(end_season))
    df = df.query('seasonId >= @start_season and seasonId <= @end_season')

    if regular is True and playoffs is True:
        # plot both regular attendance and playoff attendance
        plot1 = alt.Chart(df, title="Regular Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Season"),
            alt.Y('regular:Q', title='Regular Attendance'))
        plot2 = alt.Chart(df, title="Playoff Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Season"),
            alt.Y('playoff:Q', title='Playoff Attendance'))
        plot = (plot1 | plot2)
    elif regular is True:
        # plot regular attendance if it is requested only
        plot = alt.Chart(df, title="Regular Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Season"),
            alt.Y('regular:Q', title='Regular Attendance'))
    elif playoffs is True:
        # plot playoff attendance if it is requested only
        plot = alt.Chart(df, title="Playoff Attendance").mark_bar().encode(
            alt.X('seasonId:N', title="Season"),
            alt.Y('playoff:Q', title='Playoff Attendance'))
    else:
        raise Exception('Must select at least one attendance type')
    return plot


def team_stats(start_season="20192020", end_season="20192020"):
    """
    Get team season stats specified by start year or start year and end year.
    If no year is specified then the year 2019-2020 is default.
    If an end year is specified then the start year is also to be provided.
    year is to be provided in a 2 year format of YYYYYYYY.

    The valid seasons range from the 1917 season until the
    current season.

    You can find the glossary pertaining to the returned
    columns by going to http://www.nhl.com/stats/glossary.

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
    faceoffWinPct | gamesPlayed | goalsAgainst | goalsAgainstPerGame | ...
    -----------------------------------------------------------------------
       0.481361   |      82     |     251      |        3.06097      | ...
    -----------------------------------------------------------------------
    ...
    """
    # Check that the arguments are of the correct type (i.e. str)
    helpers.check_argument_type(start_season, 'start_season', str)
    helpers.check_argument_type(end_season, 'end_season', str)
    helpers.check_season_format(start_season)
    helpers.check_season_format(end_season)
    helpers.check_seasons(start_season, end_season)

    base_url = 'https://api.nhle.com/stats/rest/en/team/summary?'
    arguments = 'cayenneExp=gameTypeId=2' +\
                f' and seasonId<={end_season}' +\
                f' and seasonId>={start_season}'

    # Make the api request
    page = requests.get(base_url + arguments)

    # Check the response code is valid - i.e. the API didn't fail
    helpers.check_response_code(page.status_code)

    df = pd.DataFrame(page.json()['data'])

    return df


def draft_pick(pick_number=1, round_number=None, year=None):
    """
    The function returns information about draft picks for the specified
    parameters and stores them in a pandas data frame.

    If year is not specified, then all of the draft picks
    for all year will be returned.

    If no round is specified the data frame will include all players
    with chosen pick number from every round.

    There are cases when even though user entered valid parameters,
    the output would be empty if a pick number didn't exist
    in a specified round, an assert error would be raised.

    Parameters
    ----------
    pick_number : int (default 1).
      Desired pick number, must be in the range [1,38].
      If nothing is specified, picks first draft in all rounds.
    round_number : int (default None).
      Desired round number, must be in the range [1,25]
    year : int (default None).
      Year in which a draft took place. Must be YYYY format,
      that contains year in a range [1963,2019].

    Returns
    -------
    pandas.core.DataFrame
      Drafts with specified parameters.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> pick_number = 9
    >>> round_number = 7
    >>> year = 2000
    >>> pypuck.draft_pick(pick_number = pick_number,
                          round_number=round_number, year=year)

    Player            | Round_num | Pick_num | Tri_code | Year | ...
    ------------------------------------------------
    Tim Eriksson      |     7     |    9     |   LAK    | 2000 | ...
    ------------------------------------------------
    """
    # Check that the arguments are of the correct type (i.e. int) and value
    helpers.check_argument_type(pick_number, 'pick_number', int)
    assert pick_number in range(1, 38), (
        'Number of pick is out of avaliable range')
    if round_number is not None:
        helpers.check_argument_type(round_number, 'round_number', int)
        assert round_number in range(1, 25), (
            'Number of round is out of avaliable range')
    if year is not None:
        helpers.check_argument_type(year, 'year', int)
        assert year in range(1963, 2019), 'Year is out if avaliable range'

    api = requests.get("https://records.nhl.com/site/api/draft").json()
    stats = pd.DataFrame(api['data'])

    if round_number and year:
        query = "pickInRound == @pick_number and " +\
                "roundNumber == @round_number and draftYear == @year"
    elif round_number:
        query = "pickInRound == @pick_number and roundNumber == @round_number"
    elif year:
        query = "pickInRound == @pick_number and draftYear == @year"
    else:
        query = "pickInRound == @pick_number"

    df = stats.query(query)[['playerName', 'pickInRound',
                             'roundNumber', 'triCode', 'draftYear']]
    # Checking if output is valid
    assert df.empty is False, (
        'Specified pick number didn`t exist in specified round or year')
    return df
