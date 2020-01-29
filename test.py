from riotwatcher import RiotWatcher, ApiError
import json

watcher = RiotWatcher('')

my_region = 'euw1'

me = watcher.summoner.by_name(my_region, 'Cookienator19')

id = me['puuid']

my_ranked_stats = watcher.league.positions_by_summoner(my_region, me['id'])
