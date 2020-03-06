# authors: Jarvis Nederlof, Manish Joshi
# date: 2020-03-02

"""
This script tests the pypuck functions in the pypuck module.
"""

from pypuck import pypuck
import pandas as pd

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
    
def test_team_stats():
	"""
	Function to test that the team_stats function appropriately returns a pd.DataFrame object
  and that the resulting dataframe has the queried data. 

	Keyword Arguments:
		start_season {str} -- start_season to query (default: {'20192020'})
		end_season {str} -- end_season to query (default: {'20192020'})

	Raises:
		ValueError: A message if return value is wrong (empty return).
	"""
	# Test for various end_dates
	df = pypuck.team_stats(start_season='19992000',end_season='20102011')
	if df.empty == True:
		raise TypeError("invalid Inputs, Season_start should be later than Season end. Valid seasons are from 1917 to 2020")
	
	# Test for number of columns and rows.
	df = pypuck.team_stats(start_season='19531954',end_season='19581959')
	if len(df) != 36:
		raise ValueError("Dataframe is wrong length - check data return")
	
	# test for the output for default is year 20192020
	df = team_stats()
	assert int(df['seasonId'].mean()) == 20192020, "A function call with default arguments should return current season"

  
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
