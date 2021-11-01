import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

class nbastats:

    def __init__ (self,year):
        self.year = year

    def team_per_game(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        div = soup.find('div',{'id':'div_per_game-team'})
        table = div.find('table',{'id':'per_game-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)

        df_template = []
        
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[24*i:(24*i)+24]))
    
        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
    
        return df

    def opp_per_game(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        div = soup.find('div',{'id':'div_per_game-opponent'})
        table = div.find('table',{'id':'per_game-opponent'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[24*i:(24*i)+24]))

        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df



    def team_per_100(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        div = soup.find('div',{'id':'div_per_poss-team'})
        table = div.find('table',{'id':'per_poss-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[24*i:(24*i)+24]))


        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df
    

    def opp_per_100(self):
        #Best defensive team each season (by DRtg), required table is Per 100 Poss Stats, Opponent Tab
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        div = soup.find('div',{'id':'div_per_poss-opponent'})
        table = div.find('table',{'id':'per_poss-opponent'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[24*i:(24*i)+24]))

        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df


    def team_advanced(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        div = soup.find('div',{'id':'div_advanced-team'})
        table = div.find('table',{'id':'advanced-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header = [i for i in header if i not in ('','Rk','Offense Four Factors','Defense Four Factors','\xa0')]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td',{'data-stat':'DUMMY'}):
                #row = td(text=True,dummy=False)
                #tables.append(''.join(row) if row else 'blank')
                #tables = [val for val in tables if val not in ('.','')]
                td.decompose()

            for td in tr.find_all('td'):
                row = td(text=True)
                if row:
                    tables.append(''.join(row))
                else:
                    tables.append('N/A')
                tables = [val for val in tables if val not in ('.','')]
        
        df_template = []
        
        for i in range(0,len(table.find_all('tr'))-3):
            df_template.append(list(tables[27*i:(27*i)+27]))
    
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
    
        return df
        

    def team_shooting(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        div = soup.find('div',{'id':'div_shooting-team'})
        table = div.find('table',{'id':'shooting-team'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header = [i for i in header if i not in ('','\xa0','% of FGA by Distance','FG% by Distance','% of FG Ast\'d','Dunks','Layups','Corner','Heaves','Rk')]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td',{'data-stat':'DUMMY'}):
                #row = td(text=True,dummy=False)
                #tables.append(''.join(row) if row else 'blank')
                #tables = [val for val in tables if val not in ('.','')]
                td.decompose()

            for td in tr.find_all('td'):
                row = td(text=True)
                if row:
                    tables.append(''.join(row))
                else:
                    tables.append('Not reported')
                tables = [val for val in tables if val not in ('.','')]

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[27*i:(27*i)+27]))
    
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        
        return df



    def opp_shooting(self):
        url = "https://www.basketball-reference.com/leagues/NBA_{}.html".format(self.year)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = []
        header = []
        ptag = soup.findAll('p')[2]
        champ = ptag.find('a').contents[0]
        div = soup.find('div',{'id':'div_shooting-opponent'})
        table = div.find('table',{'id':'shooting-opponent'})
        
        for tr in table.find_all('thead'):
            for th in tr.find_all('th'):
                column = th.text
                header.append(column)
        header = [i for i in header if i not in ('','\xa0','% of FGA by Distance','FG% by Distance','% of FG Ast\'d','Dunks','Layups','Corner','Heaves','Rk')]
                
        for tr in table.find_all('tbody'):
            for td in tr.find_all('td',{'data-stat':'DUMMY'}):
                #row = td(text=True,dummy=False)
                #tables.append(''.join(row) if row else 'blank')
                #tables = [val for val in tables if val not in ('.','')]
                td.decompose()

            for td in tr.find_all('td'):
                row = td(text=True)
                if row:
                    tables.append(''.join(row))
                else:
                    tables.append('Not reported')
                tables = [val for val in tables if val not in ('.','')]

        df_template = []
        for i in range(0,len(table.find_all('tr'))-2):
            df_template.append(list(tables[27*i:(27*i)+27]))
    
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))
        champ_check_list = []

        for i in df['Team']:
            if i == champ:
                champ_check = True
            else:
                champ_check = False

            champ_check_list.append(champ_check)

        df['Champ?'] = champ_check_list

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df

directory = "/Users/macowner/Documents/Predictor_csv_files/"
start, end = int(input("Type in a start year for the search: ")), int(input("Type in an end year: "))
years = range(start,end+1)
team_per_game_list = []
opp_per_game_list = []
team_per_100_list = []
opp_per_100_list = []
team_advanced_list = []

for i in years:
    team_per_game_list.append(nbastats(i).team_per_game())
    with open(directory + "{}_team_per_game.txt".format(i), "w") as f1:
        f1.write(team_per_game_list[i-start].to_csv())

    opp_per_game_list.append(nbastats(i).opp_per_game())
    with open(directory + "{}_opp_per_game.txt".format(i), "w") as f1:
        f1.write(opp_per_game_list[i-start].to_csv())

    team_per_100_list.append(nbastats(i).team_per_100())
    with open(directory + "{}_team_per_100.txt".format(i), "w") as f1:
        f1.write(team_per_100_list[i-start].to_csv())

    opp_per_100_list.append(nbastats(i).opp_per_100())
    with open(directory + "{}_opp_per_100.txt".format(i), "w") as f1:
        f1.write(opp_per_100_list[i-start].to_csv())

    team_advanced_list.append(nbastats(i).team_advanced())
    with open(directory + "{}_team_advanced.txt".format(i), "w") as f1:
        f1.write(team_advanced_list[i-start].to_csv())

    '''
    team_shooting_list.append(nbastats(i).team_shooting())
    opp_shooting_list.append(nbastats(i).opp_shooting())
    '''

