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


def check_season_format(season):
    """
    Checks that a season string is in the correct format: "YYYYYYYY.
    Arguments:
        year {str} -- a string of a year in format YYYYYYYY.
    Raises:
        ValueError: A message showing the incorrect year format.
    """
    season_start, season_end = season[:4], season[-4:]
    for _season in [season_start, season_end]:
        try:
            datetime.strptime(str(_season), '%Y')
        except ValueError:
            raise ValueError(f"Incorrect season format {season}, requires "
                             "valid YYYYYYYY")
    if (int(season_end) - int(season_start)) not in [0, 1]:
        raise ValueError(f"Incorrect season range {season}, requires "
                         "valid season with back to back years")


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


def check_response_code(response):
    """
    Checks that the API response code is OK.

    Arguments:
        response {int} -- The API response code.

    Raises:
        ValueError: The API error response code and message
    """
    codes = {200: 'OK', 400: 'Bad Request', 403: 'Forbidden',
             404: 'Not Found', 500: 'Internal Server Error',
             503: 'Service Unavailable'}
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
        ValueError: A message indicating the start_date is > than the end_date.
    """
    e_date = datetime.strptime(start_date, '%Y-%m-%d')
    l_date = datetime.strptime(end_date, '%Y-%m-%d')
    if e_date > l_date:
        raise ValueError("Invalid date range - "
                         "end_date earlier than start_date")


def check_seasons(start_season, end_season):
    """
    Checks that the end_season is later than the start_season.

    Arguments:
        start_season {str} -- The start season formatted as a string
        end_season {str} -- The end season formatted as a string

    Raises:
        ValueError: A message indicating the
        start_season is >= than the end_season.
    """
    if int(start_season[-4:]) > int(end_season[-4:]):
        raise ValueError("Invalid date range - "
                         "end_season earlier than start_season")
