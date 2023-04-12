import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def importLibraries():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    
def load_and_process(path):
    data = pd.read_csv(path)

    ''' Processing Dataset
        -Removing unused columns (Hispanic, Police)
        -Removing any non-suicide records
        -Resetting Index
        -Removing the 'index' column that we don't need
        -Dropping all NaN values from the dataset
    '''
    df_cleaned = (data.drop(columns = [data.columns[0], 'hispanic', 'police'])
              .loc[data.intent == "Suicide"]
              .reset_index()
              .drop(columns = 'index')
              .dropna()
             )

    return df_cleaned

def load_for_dashboard(path):
    data = pd.read_csv(path)
    
    
    df_cleaned = (data.drop(columns = [data.columns[0], 'hispanic', 'police'])
              .loc[data.intent == "Suicide"]
              .reset_index()
              .drop(columns = 'index')
              .dropna()
             )
    
    