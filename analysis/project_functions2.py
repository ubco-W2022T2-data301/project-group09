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
    
