from riotwatcher import RiotWatcher, ApiError
import json

watcher = RiotWatcher('')

my_region = 'euw1'

me = watcher.summoner.by_name(my_region, 'Toaster11')

print(me['id'])

a
