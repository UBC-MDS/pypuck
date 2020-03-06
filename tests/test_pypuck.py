# authors: Jarvis Nederlof
# date: 2020-03-02

"""
This script tests the pypuck functions in the pypuck module.
"""

from pypuck import pypuck
import pandas as pd
import pytest

# @pytest.mark.skip()
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
			raise TypeError("player_stats() didn't return a pd.DataFrame.")

		if len(df) != 100:
			raise ValueError("player_stats() didn't return the top 100 players.")

	# Test for various start_dates
	for start_date in [start_date, None]:
		df = pypuck.player_stats(start_date, end_date)
		if isinstance(df, pd.DataFrame) is False:
			raise TypeError("player_stats() didn't return a pd.DataFrame.")

		if len(df) != 100:
			raise ValueError("player_stats() didn't return the top 100 players.")

def test_player_stats_bad(start_date='2020-02-28', end_date='2019-10-02'):
	"""
	Test function to check that function gracefully hanldes errors
	when it is supposed to.

	Keyword Arguments:
		start_date {str} -- start_date to query (default: {'2020-02-28'})
		end_date {str} -- end_date to query (default: {'2019-10-02'})
	"""
	try:
		df = pypuck.player_stats(start_date, end_date)
	except:
		# This error is expected
		pass

	# Change start_date to bad type
	start_date = 2019
	try:
		df = pypuck.player_stats(start_date, end_date)
	except:
		# This error is expected
		pass

def check_draft(pick_number = 1, round_number = 2, year = 2000):
	"""
	Test function to check proper inputs and returns.

	Keyword Arguments:
		pick_number {int} -- pick_number to query (default: {1})
		round_number {int} -- round_number to query (default: {2})
		year {int} -- year to query (default: {2020})

	Raises:
		ValueError: A message if return value is wrong (not enough data).
	"""
    if len(pypuck.draft_pick(pick_number, round_number, year)) != 1 :
        raise ValueError('draft_pick() returned incorrect information, there can`t be more than 1 person for specified parameters')
    if len(pypuck.draft_pick(pick_number, round_number, year)) == 0 :
        try: 
            df = pypuck.draft_check(pick_number, round_number, year)
        except:
            pass

def check_drafted_person():
    draft = pypuck.draft_pick(pick_number = 1, round_number=2, year=2000)
    if draft['playerName'] != 'Ilya Nikulin':
        raise ValueError('draft_pick() returned errorness information about specified parameters')

def check_error_draft(pick_number = 'BC', round_number = 'Van', year = 2020): 
	"""
	Test function to check that it handles errorness input in draft_pick function.

	Keyword Arguments:
		pick_number {str} -- errorness pick_number to query (default: {'BC'})
		round_number {str} -- errorness round_number to query (default: {'Van'})
		year {int} -- year out of range to query (default: {2020})
	"""
    try:
        df = pypuck.draft_check(pick_number, round_number, year)
    except:
        pass


def test_attendance_good():
	"""
	Test function to check proper inputs and returns.

	Keyword Arguments:
		pick_number {int} -- pick_number to query (default: {1})
		round_number {int} -- round_number to query (default: {2})
		year {int} -- year to query (default: {2020})

	Raises:
		ValueError: A message if return value is wrong (not enough data).
	"""


	a = attendance(start_season=None, end_season=2010)
	assert isinstance(a, alt.vegalite.v3.api.HConcatChart), "The return should include two subplots "

	a = attendance(start_season=2000, end_season=None)
	assert isinstance(a, alt.vegalite.v3.api.HConcatChart), "The return should include two subplots "

	a = attendance(start_season=1980, end_season=2001)
	assert isinstance(a, alt.vegalite.v3.api.HConcatChart), "The return should include two subplots "

	a = attendance(regular=True, playoffs=False, start_season=1980, end_season=2001)
	assert isinstance(a, alt.vegalite.v3.api.Chart), "The return should be only one plot"

	a = attendance(regular=False, playoffs=True, start_season=1980, end_season=2001)
	assert isinstance(a, alt.vegalite.v3.api.Chart), "The return should be only one plot"	


def test_attendance_bad():
	"""
	Test function to check proper inputs and returns.

	Keyword Arguments:
		pick_number {int} -- pick_number to query (default: {1})
		round_number {int} -- round_number to query (default: {2})
		year {int} -- year to query (default: {2020})

	Raises:
		ValueError: A message if return value is wrong (not enough data).
	"""

	with pytest.raises(Exception) as e:
        assert attendance(start_season=2011, end_season=2010)
    assert str(e.value) == "End season should be larger than the start season"

	with pytest.raises(Exception) as e:
        assert attendance(start_season=1951, end_season=2010)
    assert str(e.value) == "Start season is out of range"

	with pytest.raises(Exception) as e:
        assert attendance(start_season=1991, end_season=2021)
    assert str(e.value) == "End season is out of range"

	with pytest.raises(Exception) as e:
        assert attendance(regular=False, playoffs=False, start_season=1980, end_season=2001)
    assert str(e.value) == " Must select at least one attendance type"

	with pytest.raises(Exception) as e:
        assert attendance(regular=True, playoffs=2, start_season=1980, end_season=2001)
    assert str(e.value) == "Only boolean value can be accepted"

	with pytest.raises(Exception) as e:
        assert attendance(regular=2, playoffs=2, start_season=1980, end_season=2001)
    assert str(e.value) == "Only boolean value can be accepted"

	with pytest.raises(Exception) as e:
        assert attendance(regular=2, playoffs=True, start_season=1980, end_season=2001)
    assert str(e.value) == "Only boolean value can be accepted"
