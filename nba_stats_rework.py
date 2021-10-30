import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import Comment
from copy import deepcopy

'''
def nested(vals, start, end):
        out = deepcopy(vals)
        out[start:end+1] = [out[start:end+1]]
        return out
'''

class nbastats:

    def __init__ (self,year):
        self.year = year
    

    def team_opp100(self):
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
        for i in range(0,30):
            df_template.append(list(tables[24*i:(24*i)+24]))

        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df

    def team_100(self):
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
        for i in range(0,30):
            df_template.append(list(tables[24*i:(24*i)+24]))

        header.remove('Rk')
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))

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
            for td in tr.find_all('td'):
                row = td.text
                tables.append(row)
                tables = [val for val in tables if val not in ('','.')]

        df_template = []
        for i in range(0,30):
            df_template.append(list(tables[27*i:(27*i)+27]))
        df = pd.DataFrame(df_template,columns=header)
        df['Team'] = df['Team'].map(lambda x:x.rstrip('*'))

        #print("table_container is_setup current" in r.text)
        #print("div_per_poss-team" in r.text)
        return df

print("Team Stats Per 100: \n",nbastats(2014).team_100(),"\n")
print("Opponent Stats Per 100: \n",nbastats(2014).team_opp100(),"\n")
print("Team Advanced Stats: \n",nbastats(2014).team_advanced(),"\n")