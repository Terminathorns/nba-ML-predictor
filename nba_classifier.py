from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.model_selection import cross_val_score
from numpy.lib.function_base import average
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
curr_df = file_loader(2022,2022)


features = testdf.drop(columns=['Champ?']) #Drop extraneous columns
label = testdf['Champ?'] #Target variable
team = features['Team']
team = team.values.reshape((len(team),1))
ohe = preprocessing.OneHotEncoder(handle_unknown='ignore')
features = ohe.fit_transform(features)

np.set_printoptions(threshold=np.inf)


X_train, X_test, y_train, y_test = train_test_split(features,label,test_size=0.20,random_state=3)
brfc = BalancedRandomForestClassifier(n_estimators=1000)
model = brfc.fit(X_train,y_train)
preds = model.predict(X_test)


team_test = ohe.inverse_transform(X_test)[:,1]
team_test = team_test.reshape((len(team_test),1))
compare = np.concatenate((team_test,model.predict_proba(X_test)),axis=1)
print(compare)


#print(preds,"Model accuracy: " + str(accuracy_score(y_test,preds)*100) + "%") #Print out predictions and accuracy
#Create new dataframe for this season's stats, create a dataframe of zero's and N/A's for categorical variables

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

champ_index = np.argmax(compare_curr[:,2])
champ_team = compare_curr[champ_index,0]
print("This year's NBA champion is predicted to be the " + str(champ_team) + " with a " + str(compare_curr[champ_index,2] * 100) + "% chance of winning.")
print("Model accuracy: " + str(accuracy_score(y_test,preds) * 100) + "%")

cvscores = cross_val_score(model, features, label, cv=5)
print(cvscores)
print(cvscores.mean(),cvscores.std())
