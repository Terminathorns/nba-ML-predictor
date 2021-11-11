import pandas as pd
import nba_stats_rework as nsr


directory = "/Users/macowner/Documents/Predictor_csv_files/"

def file_writer(start,end):
        years = range(start,end+1)
        tpg = []
        opg = []
        tp100 = []
        op100 = []
        tadv = []
        tdf = []

        for i in years:
            '''
            tpg.append(nsr.nbastats(i).team_per_game())
            opg.append(nsr.nbastats(i).opp_per_game())

            opg[i-start] = opg[i-start].set_index('Team')
            opg[i-start] = opg[i-start].reindex(index=tpg[i-start]['Team'])
            opg[i-start] = opg[i-start].reset_index()
            '''
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

file_writer(1990,2005)
file_writer(2006,2006)