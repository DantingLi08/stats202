import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time

mainSite = requests.get('http://www.gostanford.com')
soup = BeautifulSoup(mainSite.text.encode('ISO-8859-1'))

dropdownFooters = soup.findAll(attrs={'class':'dropdownFooter'})

menSports = dropdownFooters[0].findAll('a')
womenSports = dropdownFooters[1].findAll('a')

menSportsWebsites = {}
for a in menSports:
    menSportsWebsites[a.contents[0]] =  'http://www.gostanford.com'+a.attrs['href']

menSportsWebsites.pop('Olympics');    # We eliminate Olympics, as this sport has no roster on the site.

stateDict = {'Ore.': 'OR', 'District of Columbia': 'DC', 'Minn.': 'MN', 'Wis.': 'WI', 'S.D.': 'SD', 'Ariz.': 'AZ', 'Ind.': 'IN', 'Idaho': 'ID', 'Kan.': 'KS', 'Calif.': 'CA', 'Md.': 'MD', 'Ky.': 'KY', 'N.H.': 'NH', 'Mont.': 'MT', 'Hawaii': 'HI', 'N.C.': 'NC', 'Ill.': 'IL', 'N.D.': 'ND', 'Colo.': 'CO', 'N.J.': 'NJ', 'Wash.': 'WA', 'Nev.': 'NV', 'Ark.': 'AR', 'Va.': 'VA', 'Conn.': 'CT', 'Neb.': 'NE', 'Alaska': 'AK', 'Vt.': 'VT', 'Ohio': 'OH', 'N.Y.': 'NY', 'Iowa': 'IA', 'Mass.': 'MA', 'Pa.': 'PA', 'La.': 'LA', 'Wyo.': 'WY', 'Tenn.': 'TN', 'N.M.': 'NM', 'Ala.': 'AL', 'Del.': 'DE', 'Ga.': 'GA', 'Mich.': 'MI', 'Mo.': 'MO', 'R.I.': 'RI', 'S.C.': 'SC', 'Okla.': 'OK', 'Fla.': 'FL', 'Miss': 'MS', 'Maine': 'ME', 'W.Va.': 'WV', 'Texas': 'TX', 'Tex.': 'TX', 'Utah': 'UT', 'Aala.': 'AL'}

def GetRoster(url):
    """Outputs a BeautifulSoup object containing the roster for this sport.

    Inputs:
    url: Address for a specific sport

    """
    sportSite = requests.get(url)
    soup = BeautifulSoup(sportSite.text.encode('ISO-8859-1'))
    a = soup.findAll('a',text='Roster')[0]
    rosterSite = requests.get('http://www.gostanford.com'+a.attrs['href'])
    return BeautifulSoup(rosterSite.text.encode('ISO-8859-1'))

def ScrapeRoster(sport, soup,stateDict):
    """Scrapes a website with a roster for the following entries: name, home state, and height.

    Input:
    sport: The sport (string).
    soup: A BeautifulSoup object containing the website.
    stateDict: Dictionary mapping AP style state names to 2-letter abbreviations.

    Output:
    entries: A list of dictionaries, each of which has information on a single player.

    """
    table = soup.find(attrs={'id':'roster-table'})    # Find the roster table element
    tbody = table.find('tbody')                       # Find the body of the table
    rows = tbody.findAll('tr')                        # Define a list of all the rows
    entries = []

    for row in rows:
        entry = { 'gender': 'male', 'sport' : sport }                    # Initialize the record for this player

        # Skip any women that show up on the roster.
        genderCol = row.find('td', attrs= { 'class': 'gender' })
        if genderCol and genderCol.contents[0].strip()=='Women':  break

        # Find a column with the name, and read the name from it.
        # The name can be by itself, or inside a link element.
        nameCol = row.find('td', attrs = { 'class': 'name' })
        if nameCol == None:   continue
        try:                    entry['name'] = nameCol.find('a').contents[0].strip()
        except AttributeError:  entry['name'] = nameCol.contents[0].strip()

        weightCol = row.find('td', attrs = { 'class': 'weight' })
        if weightCol == None:   continue
        try:
          weightRaw = weightCol.find('a').contents[0].strip()
          if weightRaw =='-':   entry['weight'] = np.nan
          else:                 entry['weight'] = int(weightRaw.split('-')[0])*12 + int(weightRaw.split('-')[1])
        except AttributeError:  entry['weight'] = weightCol.contents[0].strip()

        # Find a column with the height
        heightCol = row.find('td', attrs = { 'class': 'height' })
        # If there is no such column, let height be nan.
        if heightCol==None:
            entry['height'] = np.nan
        # Transform the height from a 'feet-inches' format to
        # the number of inches as an integer.
        else:
          heightRaw = heightCol.contents[0].strip()
          if heightRaw =='-':   entry['height'] = np.nan
          else:                 entry['height'] = int(heightRaw.split('-')[0])*12 + int(heightRaw.split('-')[1])

        # Read in the hometown, if available
        hometown = row.find('td',attrs = { 'class': 'hometown' }).contents[0].strip()
        try:                                    homestate = hometown.split(',')[1].split('(')[0].strip()
        except IndexError:                      homestate = "NA"
        if homestate in stateDict:              homestate = stateDict[homestate]
        if not homestate in stateDict.values(): homestate = "Other"
        entry['homestate'] = homestate

        entries.append(entry)

    return entries

entries = []

for sport in menSportsWebsites:
    url = menSportsWebsites[sport]
    soup = GetRoster(url)
    print("Scraping: "+sport+" ...\n")
    time.sleep(1)  # This takes a break of 1 second between requests.
    entries.extend(ScrapeRoster(sport,soup,stateDict))

data = pd.DataFrame(entries)
print(data.to_string())

# Suppose, we are only interested in players for whom we have every variable.
# Then, we can drop any rows containing a `nan`:
dataFull = data.dropna(axis=0)
print(dataFull.to_string())
dataFull.to_csv('rosters.csv')