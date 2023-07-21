# encoding=utf-8

### All my Simpletransformers apply functions
# pip install simpletransformers==0.63.9
# apply model in one go or iteratively, save text, class and probablility for class 1


from simpletransformers.classification import ClassificationModel, ClassificationArgs
# https://pypi.org/project/simpletransformers/ <- source evaluation tipps
from scipy.special import softmax
#https://github.com/ThilinaRajapakse/simpletransformers/issues/30 
import pandas as pd
from sys import argv
from sys import stderr
import os

import logging
#logging.basicConfig(level=logging.INFO)
#transformers_logger = logging.getLogger("transformers")
#transformers_logger.setLevel(logging.INFO)
os.environ["TOKENIZERS_PARALLELISM"] = "false"

### APPLY EXISTING MODEL ###
def tidy_prediction_output (apply_lst, predictions, raw_outputs):
    x = list(zip(apply_lst, predictions, raw_outputs))
    tidy_output = []
    for comments, prediction, raw_outputs in x:
        #softmax to get probablities from raw_outputs
        raw_outputs = raw_outputs.reshape(1,2)
        raw_outputs = softmax(raw_outputs, axis=1)
        tidy_output.append([comments, prediction, raw_outputs[0][1]])
    df = pd.DataFrame(tidy_output, columns=["comments", "prediction", "probability_class_one"])

    return df

def predict_comments(filename, column_name, modelname, len_output):
    #input has to be list
    apply_df = pd.read_csv(filename, sep="\t", lineterminator="\n")
    apply_lst = apply_df[column_name].tolist()
    #specifies output length
    print("the whole list consists of {} elements".format(len(apply_lst)))  
    if len_output == 0:
        len_output = len(apply_lst)
        apply_lst = apply_lst
    else:
        apply_lst = apply_lst[:len_output]
    print("the application list consists of {} elements".format(len(apply_lst)))
    
    # specify model used
    # may need: use_multiprocessing = False
    model_args = ClassificationArgs(use_multiprocessing=False, use_multiprocessing_for_evaluation=False)
    model = ClassificationModel('distilbert', modelname, use_cuda=False, args=model_args)
    print("the model {} is loaded".format(modelname))
    # apply model
    predictions, prediction_values = model.predict(apply_lst)    

    return apply_lst, predictions, prediction_values



def apply_model(filename : str, columnname : str, modelname : str, outputfilename : str, length_output = 0):
    apply_lst, predictions, raw_outputs = predict_comments(filename, columnname, modelname, length_output)
    df = tidy_prediction_output(apply_lst, predictions, raw_outputs)
    df.to_csv(outputfilename, sep="\t")

    return df

