#pip install pandas

import pandas as pd
from pandas.core.frame import DataFrame

read_file = pd.read_excel("<your file.xlsx>")

read_file.to_csv("file.csv", index=None, header=True)

dataframe = pd.DataFrame(pd.read_csv("file.csv"))