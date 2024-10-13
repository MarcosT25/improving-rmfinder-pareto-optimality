import pandas as pd

with open ('output-functions.csv') as f:
    df = pd.read_csv(f, sep=',')
    solves_to_drop = []
    for this_solve in range(len(df)):
        for comparison_solve in range(len(df)):
            if this_solve == comparison_solve or comparison_solve in solves_to_drop:
                continue
            if df.loc[this_solve]['cross'] <= df.loc[comparison_solve]['cross'] and df.loc[this_solve]['risk'] <= df.loc[comparison_solve]['risk'] and df.loc[this_solve]['atr'] <= df.loc[comparison_solve]['atr'] and df.loc[this_solve]['freq'] <= df.loc[comparison_solve]['freq']:
                solves_to_drop.append(this_solve)

    front = pd.DataFrame(columns=['fake', 'cross', 'risk', 'atr', 'freq'])
    id_relation = {}
    for i in range(len(df)):
        if i not in solves_to_drop:
            front.loc[0 if pd.isnull(front.index.max()) else front.index.max() + 1] = df.loc[i]
            id_relation[int(front.index.max())] =  i
    front.to_csv('front.csv')

rms_id = [26, 3, 21]
original_id = []
for rm in rms_id:
    original_id.append(id_relation[rm])

print(original_id)
