import requests
from bs4 import BeautifulSoup

def parseStateSite(file):
    '''
    This parser is specific to the states and territories wiki page and will not work for a regular page
    This parses through the wikipedia table and returns a list of all of the information in each row
    '''
    plainText = file.text
    soup = BeautifulSoup(plainText,'html.parser')
    stateInfoList = []
    rows = soup.findAll('tr')
    for state in range(2,52): #only get the 50 states, nothing more. On this specific page, it starts at the 3rd row (index 2)
        stateInfo = rows[state].text.replace("\n"," ").replace(" \xa0","")#extract out junk characters
        stateInfoList.append(stateInfo)

    return stateInfoList

def parseGeneralSite(file):
    '''
    This parser is not specific and will collect everything in all table rows on a site
    '''
    plainText = file.text
    soup = BeautifulSoup(plainText,'html.parser')
    rowsList = []
    rows = soup.findAll('tr')
    for row in rows:
        rowsList.append(row.text.replace("\n"," "))

    return rowsList
        

cont = True
while cont:
    
    outfile = open('infoOutput.txt','w')

    site = input("Input a site.\nPress enter to use https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States\n")

    #if the user enters nothing, just set it to the states wiki page.
    if len(site) == 0:
        site = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

    try:
        file = requests.get(site) 

        #we run a different parser for the states wiki page to only get the states and nothing else.
        if site == "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States":
            info = parseStateSite(file)
            outfile.write("StateName, Abbr, Capital, Largest, Established, Population, TotAreaMI, TotAreaKM, LandAreaMI, LandAreaKM, WaterAreaMI, WaterAreaKM, NumReps\n\n")
            for row in info:
                outfile.write(row+'\n')

        else:
            data = parseGeneralSite(file)
            for row in data:
                outfile.write(row+'\n')
           
    except Exception as e:
        print("There was a problem getting the site")
        print(e)
        
    finally:
        outfile.close()
        print("done. Output saved to infoOutput.txt")

    choice = input("Enter another site? y/n")
    if choice.lower() != 'y':
        cont = False
