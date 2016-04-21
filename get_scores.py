import httplib, json
from tabulate import tabulate

connection = httplib.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token':'93b03f06192f4af3ba17b52506930d79', 'X-Response-Control':'minified'}

def get_team_and_league_id(personal_data) :
	with open('league_details.json','r') as file_reader:
		data_json = json.load(file_reader)
	for league in data_json :
		if league['caption'] == personal_data['favorite_league'] :
			break
	league_id = str(league['id'])
	file_name = 'Leagues/'+str(league['id'])+'.json'
	with open(file_name,'r') as file_reader :
		data_json = json.load(file_reader)
	teams = data_json['teams']
	for team in teams :
		if team['name'] == personal_data['favorite_team'] or team['shortName'] == personal_data['favorite_team'] :
			break
	team_id = str(team['id'])
	return (league_id,team_id)

def print_league_table(league_id) :
	table = []
	connection.request('GET','/v1/soccerseasons/'+league_id+'/leagueTable',None, headers)
	league_table_json = json.loads(connection.getresponse().read().decode('utf-8'))	
	standings = league_table_json['standing']
	for item in standings :
		table.append([item['position'], item['teamName'], item['playedGames'], item['wins'], item['draws'], item['losses'], item['points']])
		
	print tabulate(table,headers=["Rank","Team Name","Played","Wins","Draws","Losses","Points"])	
	
def fixtures_league(league_id) :
	connection.request('GET','/v1/soccerseasons/'+league_id+'/fixtures',None, headers)
	fixtures_json = json.loads(connection.getresponse().read().decode('utf-8'))
	
	fixtures = fixtures_json['fixtures']
	for fixture in fixtures :
		result = fixture['result']
		date = fixture['date']
		print fixture['homeTeamName'], result['goalsHomeTeam'],' - ',result['goalsAwayTeam'], fixture['awayTeamName']

def fixtures_team(team_id) :
	connection.request('GET','/v1/teams/'+team_id+'/fixtures',None,headers)
	fixtures_json = json.loads(connection.getresponse().read().decode('utf-8'))

	fixtures = fixtures_json['fixtures']
	for fixture in fixtures :
		result = fixture['result']
		data = fixture['date']
		print fixture['homeTeamName'], result['goalsHomeTeam'],' - ',result['goalsAwayTeam'], fixture['awayTeamName']

def main() :
	personal_data = {'favorite_league':'La Liga','favorite_team':'Real Madrid'}
	league_id, team_id = get_team_and_league_id(personal_data)

	fixtures_team(team_id)

if __name__ == '__main__' :
	main()