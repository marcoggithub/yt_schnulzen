from langdetect import detect, LangDetectException
import time
import PySimpleGUI as sg
import swifter
import pandas as pd
import pickle




def ident_lang(x):
    try:
        language = detect(x)
    except LangDetectException as e:
        print(x)
        language = "NA"

    ident_lang.index += 1
    if ident_lang.index % 5000 == 0 or ident_lang.index == 1:
        print("{} von {}".format(ident_lang.index, ident_lang.length))

    #return language detected
    return language

