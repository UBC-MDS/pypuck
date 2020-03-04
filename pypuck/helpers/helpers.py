# author: Jarvis Nederlof
# date: 2020-03-03

"""
This helper script is not designed to be used directly,
rather it is a helper called by the pypuck module.

This script cannot be run on its own and must be accessed
by first importing the module, and then calling a function
as part of the module.

Its purpose is to contain commonly used functions to check for
edge cases and in-function unit tests.

Example:
>>> from helpers import helpers
>>> helpers.check_date_format(some_date_string)
"""

from datetime import datetime

def check_date_format(date_):
	"""
	Checks that a date string is in the correct format: "YYYY-MM-DD".
	
	Arguments:
		date_ {str} -- a date formatted as a string.
	
	Raises:
		ValueError: A message showing the incorrect date format.
	"""
	try:
		datetime.strptime(date_, '%Y-%m-%d')
	except ValueError:
		raise ValueError(f"Incorrect date format {date_}, requires YYYY-MM-DD")

def check_year_format(year):
	"""
	Checks that a year string is in the correct format: "YYYY".
	
	Arguments:
		year {str} -- a string of a year in format YYYY.
	
	Raises:
		ValueError: A message showing the incorrect year format.
	"""
	try:
		datetime.strptime(str(year), '%Y')
	except ValueError:
		raise ValueError(f"Incorrect year format {year}, requires YYYY")

def check_response_code(response):
	"""
	Checks that the API response code is OK.
	
	Arguments:
		response {int} -- The API response code.
	
	Raises:
		ValueError: The API error response code and message
	"""
	codes = {200: 'OK', 400: 'Bad Request', 403: 'Forbidden',
			 404: 'Not Found', 500: 'Internal Server Error', 503: 'Service Unavailable'}
	if codes[response] != 'OK':
		raise ValueError(f"Response {response} - {codes[response]}")

def check_argument_type(arg, arg_name, _type):
	"""
	Checks that the argument input is of the correct type.
	
	Arguments:
		arg {object} -- the function argument.
		arg_name {str} -- the argument name.
		_type {type} -- a python 'type' specification.
	
	Raises:
		TypeError: A message showing the incorrect argument type.
	"""
	if isinstance(arg, _type) is False:
		raise TypeError(f"Expecting {_type} got {type(arg)} for {arg_name}")

def check_date(start_date, end_date):
	"""
	Checks that the end_date is later than the start_date.
	
	Arguments:
		start_date {str} -- The start date formatted as a string
		end_date {str} -- The end date formatted as a string
	
	Raises:
		ValueError: A message indicating the start_date is later than the end_date.
	"""
	e_date = datetime.strptime(start_date, '%Y-%m-%d')
	l_date = datetime.strptime(end_date, '%Y-%m-%d')
	if e_date > l_date:
		raise ValueError("Invalid date range - end_date earlier than start_date")
