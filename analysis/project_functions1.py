import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def import_libraries():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

def load_and_process(path):
    raw_data = pd.read_csv(path)

    # Cleaning the dataset
    data_cleaned = (raw_data.drop(['hispanic',"Unnamed: 0"],axis=1)
                .dropna(subset=['year','month','intent','police','sex','age','race','place','education'])
                .reset_index(drop=True)
    ) 

    return data_cleaned

def stats(df):
    df1 = df[['age','sex','race','education','intent']]
    return df1.groupby('education').agg({'intent':'count','age':['mean','std']})

