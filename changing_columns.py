import pandas as pd

liverpool_df = pd.read_csv('data/liverpool.csv', index_col=0)

liverpool_df.rename(columns={'position': 'Position', 'born': 'Born', 'number': 'Number', 'nationality': 'Nationality'}, inplace=True)
liverpool_df.index.name = 'Player Name'
liverpool_df.set_index('Number', inplace=True)


liverpool_df
