import requests

params = {
  'access_key': '22d125c155db910dcb8935f6738cf9dc',
  'query': 'Wroclaw'
}

api_result = requests.get('https://api.weatherstack.com/current', params)

api_response = api_result.json()

print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))