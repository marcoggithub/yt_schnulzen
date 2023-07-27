import pandas as pd
import re

def del_non_latin(pd_series) -> list:
    #find rows
    patternDel = fr"\A[^a-z]+\Z"
    i_filter = df_comments['comment'].str.contains(patternDel, regex=True, case=False)
    #keep all rows which indices do not match i_filter
    df_filtered_out = df_comments[i_filter]
    df_comments = df_comments[~i_filter]
    print(df_comments.shape)
    df_comments = df_comments.reset_index(drop=True)
    
    
    print("deleted all comments without latin characters")
    