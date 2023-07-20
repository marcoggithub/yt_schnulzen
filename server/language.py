import pandas as pd
import pickle
from langdetect import detect, LangDetectException
import time
import swifter


def ident_lang(x):
    global index
    global length
    try:
        language = detect(x)
    except LangDetectException:
        language = "NA"

    # show progress

    # return language detected
    return language


df_comments = pd.read_pickle("processed_data.pkl")
df_comments.reset_index(drop=True)

## to show progress
index = 0
length = df_comments.shape[0]


df_comments["lang"] = df_comments["comment"].swifter.apply(lambda x: ident_lang(x))

df_comments.to_pickle("data/processed/{}.pkl".format("server_langdetect"))
