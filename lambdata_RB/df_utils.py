"""
Utility functions for working with DataFrame
"""

import pandas as pd
class df_util:
    """
    class for dataframe utility functions
    """
    TEST_DF =  pd.DataFrame([1,2,3,4,5,6])

    def __init__(self,df):
        self.df = df

    def check_null(self):
        return self.df.isnull().sum()

    def more_data(self,df1):
        self.df = pd.concat([self.df,df1],ignore_index=True)
        return

    def show_data(self,num=1):
        return self.df.head(num)
