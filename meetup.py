from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def main():

	#Requesting Authorization
	header = {'Accept': 'application/json'}
	url = 'https://secure.meetup.com/oauth2/authorize?client_id=KEY&redirect_uri=https://localhost:3000&response_type=anonymous_code'
	response = requests.get(url=url, headers=header)
	json_response = response.json()
	authorizaiton_code = (json_response['code'])
	print("AUTHORIZATION CODE: ", authorizaiton_code, '\n')

	#Requestin Access Token
	url2 = 'https://secure.meetup.com/oauth2/access?client_id=KEY&client_secret=KEY2&grant_type=anonymous_code&redirect_uri=https://localhost:3000&code={}'.format(authorizaiton_code)
	response2 = requests.post(url=url2, headers=header)
	json_response_2 = response2.json()
	access_token = (json_response_2['access_token'])
	print("SECOND JSON: ", json_response_2, '\n')

	#Request Access Token Using Your Credentials
	url3 = 'https://api.meetup.com/sessions?&email=EMAIL&password=PASSWORD'
	header3 = {'Authorization': 'Bearer {}'.format(access_token)}
	response3 = requests.post(url=url3, headers=header3)
	json_response_3 = response3.json()
	print("THIRD JSON: ", json_response_3)
	oauth_token = (json_response_3['oauth_token'])
	print("OATH TOKEN: ", oauth_token)

	#GET UPCOMING EVENTS
	header4 = {'Authorization': 'Bearer {}'.format(oauth_token)}
	url4 = 'https://api.meetup.com/find/upcoming_events?page=10000'
	response4 = requests.get(url=url4, headers=header4)
	f = open("events.txt", "w")
	f.write(str(response4.json()))
	f.close()
	return "Hello"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000)
