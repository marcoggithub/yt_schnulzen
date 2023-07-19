from langdetect import detect
import time
import PySimpleGUI as sg


def ident_lang(x):
    try:
        language = detect(x)
    except:
        language = "NA"
    
    #show progress
    ident_lang.index += 1
    sg.one_line_progress_meter('Language Detection', ident_lang.index, ident_lang.length, 'interrupt kernel to stop', no_button=True )
    #return language detected
    return language

