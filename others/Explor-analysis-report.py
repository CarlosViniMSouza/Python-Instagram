# In Jupyter Notebook : !pip install -U pandas-profiling

# Input for Google Drive :
from google.colab import drive
drive.mount('/content/drive')

# Import Libraries :
import pandas as pd
from pandas_profiling as pp
from sklearn.datasets import load_iris

# Import the DataBase :
iris = load_iris()
dataframe = pd.DataFrame(data = iris.data, columns = iris.feature_names)
dataframe.head()

# Doing Report :
report = pp.ProfileReport(dataframe)
report.to_notebook_iframe()

# Export in HTML :
report.to_file(output_file = "Report_Iris.html")