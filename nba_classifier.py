from imblearn.ensemble import BalancedRandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import accuracy_score

directory = "/Users/macowner/Documents/Predictor_csv_files/"


def classifier(start,end):
    cdf = pd.read_csv(directory + "{}_to_{}_team_stats.txt".format(start,end))
    features = cdf.drop(['G','MP','Arena','Attend.','Attend./G'],1)
    label = cdf['Champ?']
    ohe = preprocessing.OneHotEncoder()
    features = ohe.fit_transform(features)
    np.set_printoptions(threshold=np.inf)

    X_train, X_test, y_train, y_test = train_test_split(features,label,test_size=0.25,random_state=20,stratify=label)
    brfc = BalancedRandomForestClassifier()
    model = brfc.fit(X_train,y_train)
    preds = model.predict(X_test)
    return preds, ohe.inverse_transform(X_test),"Model accuracy: " + str(accuracy_score(y_test,preds)*100) + "%"

print(classifier(1990,2021))

'''
testdf_new = classifier(2022,2022)
features_new = testdf_new.drop(['G','MP','Arena','Attend.','Attend./G'],1)
label_new = testdf_new['Champ?']
'''



'''
features_new = ohe.fit_transform(features_new)
np.set_printoptions(threshold=np.inf)
model.predict(features_new)
'''

        


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