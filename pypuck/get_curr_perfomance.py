import requests
import json
import pandas as pd

def get_curr_perfomance(team_id):
    """
    This function sends an API request to the NHL.com website and gets basic statistics for specified team.

    Parameters:
    ------------------------
    team_id : int
        Team id you want to extract information about.

    Returns:
    ------------------------
    stats_df : pd.DataFrame
        The players stats in a dataframe.

    Examples
    --------
    >>> from pypuck import pypuck
    >>> team_id = 'Connor McDavid'
    >>> pypuck.player_stats(team_id=team_id)
    """
    r = requests.get("http://statsapi.web.nhl.com/api/v1/teams/{}/stats".format(team_id)).json()
    team = r['stats'][0]

    #Getting stats from api call
    dicts = {key: team[key] for key in team.keys() 
                               & {'splits'}} 
    
    stats = dicts.get('splits')[0]
    
    #Printing simple stats
    tot = stats['stat']['gamesPlayed']
    ratio = stats['stat']['wins']/stats['stat']['gamesPlayed']
    points = stats['stat']['pts']
    

    print('Total amount of games played:', tot)
    print('Ratio of wins: %0.3f'%(ratio))
    print('Points acquired:', points)

    #Saving stats in DataFrame

    stats_df = pd.DataFrame.from_dict(stats['stat'], orient = 'index', columns = [team_id])
    return stats_df  