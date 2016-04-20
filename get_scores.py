import httplib, json, tabulate

personal_data = {'favorite_league':'Premier League','favorite_team':'Liverpool FC'}

def print_league_table(id) :
	connection = httplib.HTTPConnection('api.football-data.org')
	headers = {'X-Auth-Token':'93b03f06192f4af3ba17b52506930d79', 'X-Response-Control':'full'}
	connection.request('GET','/v1/soccerseasons/'+id+'/leagueTable',None, headers)
	league_table_json = json.loads(connection.getresponse().read().decode('utf-8'))	
	standings = league_table_json['standing']
	for item in standings :
		print item['position'], item['teamName'], item['playedGames'], item['wins'], item['draws'], item['losses'], item['points']

def main() :
	favorite_league = personal_data['favorite_league']
	favorite_team = personal_data['favorite_team']
	with open('league_details.json','r') as file_reader:
		data_json = json.load(file_reader)

	for league in data_json :
		if league['caption'] == favorite_league :
			break
	
	id = str(league['id'])
	print_league_table(id)

if __name__ == '__main__' :
	main()

