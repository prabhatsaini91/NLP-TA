from bs4 import BeautifulSoup
import urllib2
data = {}

page = urllib2.urlopen('http://www.bbc.com/sport/football/spanish-la-liga/results')
soup = BeautifulSoup(page, from_encoding='utf-8')

##print soup

for table in soup.find_all('table', class_='table-stats') :
	matches = []
	date_tag = table.find('caption')
	date = date_tag and ''.join(date_tag.stripped_strings)
	date = date[38:]
	
	for match in table.find_all('td', class_='match-details') :
		home_tag = match.find('span', class_='team-home')
		home = home_tag and "".join(home_tag.stripped_strings)
		score_tag = match.find('span', class_='score')
		score = score_tag and "".join(score_tag.stripped_strings)
		away_tag = match.find('span', class_='team-away')
		away = away_tag and "".join(away_tag.stripped_strings)

		if home and score and away :
			match = home + " " + score + " " + away
			matches.append(match)
			
	data[date] = matches
	
print data
