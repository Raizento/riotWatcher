from riotwatcher import RiotWatcher, ApiError
import json

watcher = RiotWatcher('RGAPI-ef5a14f2-1eb9-47f8-ac16-fa84e63492d5')

my_region = 'euw1'

me = watcher.summoner.by_name(my_region, 'Cookienator19')



print(me['name'])
