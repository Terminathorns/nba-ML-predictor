from imblearn.ensemble import BalancedRandomForestClassifier
import pandas as pd
from pandas.core.arrays.sparse import dtype
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import os
import nba_stats_rework as nsr
import numpy as np
from sklearn.metrics import accuracy_score

directory = "/Users/macowner/Documents/Predictor_csv_files/"

def file_loader(start,end):
    years = range(start,end+1)
    tp100 = []
    op100 = []
    tadv = []
    tdf = []
    '''
    for i in years:
        team_per_game_list.append(nsr.nbastats(i).team_per_game())
        with open(directory + "{}_team_per_game.txt".format(i), "w") as f1:
            f1.write(team_per_game_list[i-start].to_csv())

        opp_per_game_list.append(nsr.nbastats(i).opp_per_game())
        with open(directory + "{}_opp_per_game.txt".format(i), "w") as f1:
            f1.write(opp_per_game_list[i-start].to_csv())

        team_per_100_list.append(nsr.nbastats(i).team_per_100())
        with open(directory + "{}_team_per_100.txt".format(i), "w") as f1:
            f1.write(team_per_100_list[i-start].to_csv())

        opp_per_100_list.append(nsr.nbastats(i).opp_per_100())
        with open(directory + "{}_opp_per_100.txt".format(i), "w") as f1:
            f1.write(opp_per_100_list[i-start].to_csv())

        team_advanced_list.append(nsr.nbastats(i).team_advanced())
        with open(directory + "{}_team_advanced.txt".format(i), "w") as f1:
            f1.write(team_advanced_list[i-start].to_csv())
            '''
    for i in years:
        tp100.append(nsr.nbastats(i).team_per_100())
        op100.append(nsr.nbastats(i).opp_per_100())
        
        op100[i-start] = op100[i-start].set_index('Team')
        op100[i-start] = op100[i-start].reindex(index=tp100[i-start]['Team'])
        op100[i-start] = op100[i-start].reset_index()
        tadv.append(nsr.nbastats(i).team_advanced())
        tadv[i-start] = tadv[i-start].set_index('Team')
        tadv[i-start] = tadv[i-start].reindex(index=tp100[i-start]['Team'])
        tadv[i-start] = tadv[i-start].reset_index()
        tdf.append(pd.concat([tp100[i-start],op100[i-start],tadv[i-start]],axis=1).drop_duplicates())
        tdf[i-start] = tdf[i-start].loc[:,~tdf[i-start].columns.duplicated()]
    
    tdf_dataset = pd.concat([i for i in tdf],axis=0)
    with open(directory + "{}_to_{}_team_stats.txt".format(start,end), "w") as f1:
        f1.write(tdf_dataset.to_csv())
'''
file_loader(1990,2021)

'''
def classifier(start,end):
    tp100 = []
    op100 = []
    tadv = []
    cdf = pd.read_csv(directory + "{}_to_{}_team_stats.txt".format(start,end))
    return cdf

testdf = classifier(1990,2021)

features = testdf.drop(['G','MP','Arena','Attend.','Attend./G'],1)
label = testdf['Champ?']

ohe = preprocessing.OneHotEncoder()
features = ohe.fit_transform(features)
np.set_printoptions(threshold=np.inf)

X_train, X_test, y_train, y_test = train_test_split(features,label,test_size=0.27,random_state=7,stratify=label)
brfc = BalancedRandomForestClassifier()
model = brfc.fit(X_train,y_train)
print(model.feature_importances_)
preds = brfc.predict(X_test)
print(ohe.inverse_transform(X_test))
print(X_test)
print(preds)
print(np.shape(features))
print("Model accuracy: " + str(accuracy_score(y_test,preds)*100) + "%")



        


'''
directory = "/Users/macowner/Documents/Predictor_csv_files/"

team_per_game_list = []
opp_per_game_list = []
team_per_100_list = []
opp_per_100_list = []

for filename in os.listdir(directory):
    filename = os.path.join(directory,filename)
    if "team_per_game" in filename:
        team_per_game_list.append(pd.read_csv(filename))

tpg_dataset = pd.concat(team_per_game_list,ignore_index=True)
print(tpg_dataset)
'''