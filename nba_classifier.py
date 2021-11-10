from imblearn.ensemble import BalancedRandomForestClassifier
from numpy.lib.function_base import average
from sklearn.ensemble import RandomForestClassifier
from pandas.core.reshape.melt import lreshape
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import accuracy_score

directory = "/Users/macowner/Documents/Predictor_csv_files/"


def file_loader(start,end):
    cdf = pd.read_csv(directory + "{}_to_{}_team_stats.txt".format(start,end))
    return cdf

testdf = file_loader(1990,2021) #Train and test dataset
testdf_new = file_loader(2016,2016)#Dataset to apply model to
curr_df = file_loader(2022,2022)
wdf = file_loader(2016,2016)


features = testdf.drop(columns=['Champ?']) #Drop extraneous columns
label = testdf['Champ?'] #Target variable
team = features['Team']
team = team.values.reshape((len(team),1))
ohe = preprocessing.OneHotEncoder(handle_unknown='ignore')
features = ohe.fit_transform(features)

np.set_printoptions(threshold=np.inf)


X_train, X_test, y_train, y_test = train_test_split(features,label,test_size=0.20,random_state=22)
brfc = BalancedRandomForestClassifier(n_estimators=1900)
model = brfc.fit(X_train,y_train)
preds = model.predict(X_test)

print("Model accuracy: " + str(accuracy_score(y_test,preds) * 100) + "%")

team_test = ohe.inverse_transform(X_test)[:,1]
team_test = team_test.reshape((len(team_test),1))
compare = np.concatenate((team_test,model.predict_proba(X_test)),axis=1)
print(compare)

    



#print(preds,"Model accuracy: " + str(accuracy_score(y_test,preds)*100) + "%") #Print out predictions and accuracy
#Create new dataframe for this season's stats, create a dataframe of zero's and N/A's for categorical variables

'''
features_new = testdf_new.drop(columns = ['Arena','Attend.','Attend./G'])
#features_new['Champ?'] = pd.get_dummies(features_new['Champ?'])
print(features_new['Champ?'])
team_new = features_new['Team']
team_new = team_new.values.reshape((len(team_new),1))
features_new = ohe.transform(features_new)
print(np.shape(team_new))
print(model.predict(features_new))
compare_new = np.concatenate((team_new,model.predict_proba(features_new)),axis=1)
print(compare_new)
'''

features_curr = curr_df.drop(columns = ['Champ?'])
#features_curr = curr_df.loc[:, curr_df.columns != 'Champ?']
#features_new['Champ?'] = pd.get_dummies(features_new['Champ?'])
team_curr = features_curr['Team']
team_curr = team_curr.values.reshape((len(team_curr),1))
features_curr = ohe.transform(features_curr)
print(np.shape(team_curr))
print(model.predict(features_curr))
compare_curr = np.concatenate((team_curr,model.predict_proba(features_curr)),axis=1)
print(compare_curr)


'''
w_new = wdf.drop(columns = ['G','MP','Arena','Attend.','Attend./G'])
w_team = w_new['Team']
w_team = w_team.values.reshape((len(w_new['Team']),1))
w_new = ohe.transform(w_new)
print(np.shape(w_team))
print(np.shape(model.predict_proba(w_new)))
w_compare = np.concatenate((w_team,model.predict_proba(w_new)),axis=1)
print(w_compare)
#print(model.predict_proba(features_new), team_new)
'''