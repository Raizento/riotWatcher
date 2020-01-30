import cassiopeia as cass
from cassiopeia import Summoner, Patch, Champions


cass.set_riot_api_key('')


cookie = Summoner(name='Cookienator19', region='EUW')

game = cookie.match_history[Champions(region='EUW')[56]]

print(Champions(region='EUW')["Nocturne"].id)

print(game)

#print(all_nocturne_games)
