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
    


def test_team_stats_good(start_season='20192020', end_season='20192020'):
	"""
	Test function to check proper inputs and returns.

	Keyword Arguments:
		start_date {str} -- start_date to query (default: {'20192020'})
		end_date {str} -- end_date to query (default: {'20192020'})

	Raises:
		TypeError: A message if return type is wrong (wrong data type).
		ValueError: A message if return value is wrong (not enough data).
	
	Function to test that the team_stats function appropriately returns a pd.DataFrame object and that the resulting dataframe has the queried data.

	Keyword Arguments:
		start_season {str} -- start_season to query (default: {'20192020'})
		end_season {str} -- end_season to query (default: {'20192020'})
	
	Raises:
			ValueError: A message if return value is wrong (empty return).

	"""
	# Test for various end_dates
	df = pypuck.team_stats(start_season='19992000',end_season='20102011')
	if df.empty== True:
		raise TypeError("invalid Inputs, Season_start should be later than Season end. Valid seasons are from 1917 to 2020")
	
	# Test for number of columns and rows
	df = pypuck.team_stats(start_season='19531954',end_season='19581959')
	if df.shape[0] != 36 and df.shape[1] != 24:
		raise ValueError("invalid returns")

