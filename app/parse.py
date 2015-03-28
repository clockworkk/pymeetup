import json, urllib, httplib


headers = {
				'X-Parse-Application-Id':'KNZvn9YyTZ4c0EQIp37V5oQZgdiLl6aaBEYbGyJ6',
				'X-Parse-REST-API-Key':'Mt4ZvPH9u2s4pVRo7VlCZR1gPFF6GsmCLBONyKKR',
	}


def parseCommunication(parameters, todo, end_url):
	try:
		connection = httplib.HTTPSConnection('api.parse.com', 443)
		params = urllib.urlencode(parameters)
		connection.connect()
		connection.request(todo, end_url % params, '', headers)
		response = json.loads(connection.getresponse().read())
		response['status'] = True
	except:
		response = {'status' : False}

	return response


def parseLogin(info):
	'''
	GET : /1/login?%s parameters
	'''
	todo = 'GET'
	end_url = '/1/login?%s'

	login = parseCommunication(info)

	if login['status']:
		return login 


