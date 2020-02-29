def player_stats(start_date=None, end_date=None):
	"""
	Query the top 100 player's stats (sorted by total points)
	from the players summary report endpoint on the NHL.com API.

	The stats are queried on an aggregated game-by-game basis
	for a range of dates. If no date is specified the function will return
	the players stats for the current season. The stats to be
	returned are restricted to the regular season.

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
	pass