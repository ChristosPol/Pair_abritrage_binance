# Api keys loader
file = open('/Users/christos.polysopoulos/Repositories/Binance_keys.txt', "r")
a = [b.split() for b in file.readlines()]
api_key = str(a[0]).strip('[]').strip("''")
api_secret = str(a[1]).strip('[]').strip("''")
file.close()
