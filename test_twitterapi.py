from TwitterAPI import TwitterAPI

with open("config/config.txt", "r") as file:
    data = file.readlines()
    
consumer_key = data[7]
consumer_secret = data[8]
access_token_key = data[9]
access_token_secret = data[10]

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

r = api.request('statuses/update', {'status': 'I need to go flying soon!'})
if r.status_code == 200:
    print("Success!")
else:
    print(r.status_code)