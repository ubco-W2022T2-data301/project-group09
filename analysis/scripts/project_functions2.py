import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def import_lib():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
        
    

def load(path):
    raw_data = pd.read_csv(path)    
    
    df = (raw_data.drop(['Unnamed: 0', 'hispanic', 'place','police'],axis=1)
        .loc[raw_data.intent == "Homicide"]
        .reset_index()                   
    )      
           
    return df

def load1(path):
    raw_data = pd.read_csv(path)
    df1 = (raw_data.drop(['Unnamed: 0', 'hispanic', 'place', 'police', 'education'],axis=1)
        .loc[raw_data.intent == "Homicide"]
        .reset_index()                    
    )      
           
    return df1

    
    
