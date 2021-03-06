# authors: Jarvis Nederlof, Manish Joshi
# date: 2020-03-02

"""
This script tests the pypuck functions in the pypuck module.
"""

from pypuck import pypuck
import pandas as pd
import pytest


def test_player_stats_good(start_date='2019-10-02', end_date='2020-02-28'):
    """
    Test function to check proper inputs and returns.

    Keyword Arguments:
        start_date {str} -- start_date to query (default: {'2019-10-02'})
        end_date {str} -- end_date to query (default: {'2020-02-28'})

    Raises:
        TypeError: A message if return type is wrong (wrong data type).
        ValueError: A message if return value is wrong (not enough data).
    """
    # Test for various end_dates
    for end_date in [end_date, None]:
        df = pypuck.player_stats(start_date, end_date)
        if isinstance(df, pd.DataFrame) is False:
            raise TypeError("player_stats didn't return a pd.DataFrame.")

        if len(df) != 100:
            raise ValueError("player_stats didn't return the top 100 players.")

    # Test for various start_dates
    for start_date in [start_date, None]:
        df = pypuck.player_stats(start_date, end_date)
        if isinstance(df, pd.DataFrame) is False:
            raise TypeError("player_stats didn't return a pd.DataFrame.")

        if len(df) != 100:
            raise ValueError("player_stats didn't return the top 100 players.")


def test_player_stats_bad(start_date='2020-02-28', end_date='2019-10-02'):
    """
    Test function to check that function gracefully hanldes errors
    when it is supposed to.

    Keyword Arguments:
        start_date {str} -- start_date to query (default: {'2020-02-28'})
        end_date {str} -- end_date to query (default: {'2019-10-02'})
    """
    with pytest.raises(Exception) as e:
        assert pypuck.player_stats(start_date, end_date)
    assert str(e.value) == ("Invalid date range - "
                            "end_date earlier than start_date")

    # Change start_date to bad type
    start_date = 2019
    with pytest.raises(Exception) as e:
        assert pypuck.player_stats(start_date, end_date)
    assert str(e.value) == ("Expecting <class 'str'> got "
                            "<class 'int'> for start_date")


def test_team_stats():
    """
    Function to test that the team_stats function appropriately
    returns a pd.DataFrame object and that the resulting dataframe
    has the queried data.

    Raises:
        ValueError: A message if return value is wrong (empty return).
    """
    # Test for number of columns and rows.
    df = pypuck.team_stats(start_season='19531954', end_season='19581959')
    if len(df) != 36:
        raise ValueError("Dataframe is wrong length - check data return")

    # test for the output for default is year 20192020
    df = pypuck.team_stats()
    assert int(df['seasonId'].mean()) == 20192020, (
        "A function call with default arguments should return current season")


def test_team_stats_bad():
    """
    Test function to check that function gracefully hanldes errors
    when it is supposed to.
    """
    # End season earlier than start season
    start_season, end_season = '20192020', '20182019'
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == ("Invalid date range - "
                            "end_season earlier than start_season")

    # Change start_season to bad type
    start_season, end_season = 2019, '20182019'
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == ("Expecting <class 'str'> got "
                            "<class 'int'> for start_season")

    # Change end_season to bad type
    start_season, end_season = '20192020', 20192020
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == ("Expecting <class 'str'> got "
                            "<class 'int'> for end_season")

    # Change start_season to invalid date
    start_season, end_season = '20182020', '20192020'
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == (f"Incorrect season range {start_season}, requires "
                            "valid season with back to back years")

    # Change end_season to invalid date
    start_season, end_season = '20182019', '20182020'
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == (f"Incorrect season range {end_season}, requires "
                            "valid season with back to back years")

    # Change start_season to invalid date
    start_season, end_season = '2018CCCC', '20192020'
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == (f"Incorrect season format {start_season}, requires"
                            " valid YYYYYYYY")

    # Change end_season to invalid date
    start_season, end_season = '20182019', '20192O2O'
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == (f"Incorrect season format {end_season}, requires"
                            " valid YYYYYYYY")

    # Change start_season to invalid date
    start_season, end_season = '1999200', '20192020'
    with pytest.raises(Exception) as e:
        assert pypuck.team_stats(start_season, end_season)
    assert str(e.value) == (f"Incorrect season range {start_season}, requires"
                            " valid season with back to back years")


def test_draft(pick_number=1, round_number=2, year=2000):
    """
    Test function to check proper inputs and returns.

    Keyword Arguments:
        pick_number {int} -- pick_number to query (default: {1})
        round_number {int} -- round_number to query (default: {2})
        year {int} -- year to query (default: {2020})

    Raises:
        ValueError: A message if return value is wrong (not enough data).
    """
    if len(pypuck.draft_pick(pick_number, round_number, year)) != 1:
        raise ValueError('draft_pick() returned incorrect information, \
                there can`t be more than 1 person for specified parameters')


def test_drafted_person():
    """
    Test the draft function with default inputs.

    Raises:
        ValueError: A message if the returned value is wrong.
    """
    draft = pypuck.draft_pick(pick_number=1, round_number=2, year=2000)
    if draft['playerName'].values != 'Ilya Nikulin':
        raise ValueError('draft_pick() returned erroroneous information '
                         'about specified parameters')


def test_error_draft(pick_number='BC', round_number='Van', year=2020):
    """
    Test function to check that it handles erroneoss inputs
    to the function.

    Keyword Arguments:
        pick_number {str} -- erroneoss pick_number to query (default: {'BC'})
        round_number {str} --
            erroneoss round_number to query (default: {'Van'})
        year {int} -- year out of range to query (default: {2020})
    """
    # Test that the pick number type is correct
    with pytest.raises(Exception) as e:
        assert pypuck.draft_pick(pick_number, round_number, year)
    assert str(e.value) == ("Expecting <class 'int'> got <class 'str'> "
                            "for pick_number")
    # Test that the round number type is correct
    with pytest.raises(Exception) as e:
        pick_number = 1
        assert pypuck.draft_pick(pick_number, round_number, year)
    assert str(e.value) == ("Expecting <class 'int'> got <class 'str'> "
                            "for round_number")
    # Test that the round number can't be 0.
    with pytest.raises(Exception) as e:
        pick_number = 1
        round_number = 0
        assert pypuck.draft_pick(pick_number, round_number, year)
    assert str(e.value) == "Number of round is out of avaliable range"
    # Test that the year is correct type
    with pytest.raises(Exception) as e:
        pick_number = 1
        round_number = 1
        year = '2020'
        assert pypuck.draft_pick(pick_number, round_number, year)
    assert str(e.value) == "Expecting <class 'int'> got <class 'str'> for year"


def test_default_draft(pick_number=1):
    """
    Test function to check that draft_pick function returns
    correct information with default parameters.

    Keyword Arguments:
        pick_number {int} -- default pick_number to query (default: {'1'})
    """
    draft = pypuck.draft_pick(pick_number=1)
    if draft.shape != (554, 5):
        raise ValueError('draft_pick() returned erroneous '
                         'information about specified parameters')


def test_year_pick_draft(pick_number=1, year=2010):
    """
    Test function to check that draft_pick function returns correct
    information with specidied parameters.

    Keyword Arguments:
        pick_number {int} -- default pick_number to query (default: {'1'})
        year {int} -- year to query (default: {2010})
    """
    draft = pypuck.draft_pick(pick_number=1, year=2010)
    if draft.shape != (7, 5):
        raise ValueError('draft_pick() returned erroneous '
                         'information about specified parameters')


def test_round_pick_draft(pick_number=1, round_number=7):
    """
    Test function to check that draft_pick function returns
    correct information with specified parameters.

    Keyword Arguments:
        pick_number {int} -- default pick_number to query (default: {'1'})
        round_number {int} -- round_number to query (default: {'7'})
    """
    draft = pypuck.draft_pick(pick_number=1, round_number=7)
    if draft.shape != (50, 5):
        raise ValueError('draft_pick() returned erroneous '
                         'information about specified parameters')


def test_attendance_good():
    """
    Test function to check proper inputs and returns.

    Raises:
        ValueError: A message if input/output is not proper.
    """
    # check if the number of plots returned is correct
    a = pypuck.attendance(regular=True, playoffs=False,
                          start_season=None, end_season=2010)
    assert a._schema['$ref'] == '#/definitions/TopLevelUnitSpec', (
        "The return should be only one plot")

    a = pypuck.attendance(start_season=2000, end_season=None)
    assert a._schema['$ref'] == '#/definitions/TopLevelHConcatSpec', (
        "The return should include two subplots")

    a = pypuck.attendance(regular=True, playoffs=False,
                          start_season=1980, end_season=2001)
    assert a._schema['$ref'] == '#/definitions/TopLevelUnitSpec', (
        "The return should  be only one plot")

    a = pypuck.attendance(regular=True, playoffs=False,
                          start_season=1980, end_season=2001)
    assert a._schema['$ref'] == '#/definitions/TopLevelUnitSpec', (
        "The return should be only one plot")

    a = pypuck.attendance(regular=False, playoffs=True,
                          start_season=1980, end_season=2001)
    assert a._schema['$ref'] == '#/definitions/TopLevelUnitSpec', (
        "The return should be only one plot")


def test_attendance_bad():
    """
    Test function to check proper inputs and returns.

    Raises:
        ValueError: A message if input/ouput is not proper.
    """
    # check whether an error will be raised if end season
    #  is earlier than start season.
    with pytest.raises(Exception) as e:
        assert pypuck.attendance(start_season=2011, end_season=2010)
    assert str(e.value) == (
        'End season should be not be earlier than the start season')
    # check whether an error will be raised if start season is out of range.
    with pytest.raises(Exception) as e:
        assert pypuck.attendance(start_season=1951, end_season=2010)
    assert str(e.value) == "Start season is out of range"
    # check whether an error will be raised if end season is out of range.
    with pytest.raises(Exception) as e:
        assert pypuck.attendance(start_season=1991, end_season=2021)
    assert str(e.value) == "End season is out of range"
    # check whether an error will be raised if both
    #  regular and playoffs are set to False
    with pytest.raises(Exception) as e:
        assert pypuck.attendance(regular=False, playoffs=False,
                                 start_season=1980, end_season=2001)
    assert str(e.value) == "Must select at least one attendance type"
    # check whether an error will be raised if playoffs is not boolean value.
    with pytest.raises(Exception) as e:
        assert pypuck.attendance(regular=True, playoffs=2,
                                 start_season=1980, end_season=2001)
    assert str(e.value) == (
        "Expecting <class 'bool'> got <class 'int'> for playoffs")
    # check an error will be raised if regular is not boolean value
    with pytest.raises(Exception) as e:
        assert pypuck.attendance(regular=2, playoffs=True,
                                 start_season=1980, end_season=2001)
    assert str(e.value) == (
        "Expecting <class 'bool'> got <class 'int'> for regular")
