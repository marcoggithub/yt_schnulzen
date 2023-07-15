# encoding=utf-8
import sys
#machine learning packages
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

def tidy_and_save (apply_lst, predictions, raw_outputs):
    x = list(zip(apply_lst, predictions, raw_outputs))
    print(x)
    print(10*"-")

    tidy_output = []
    for comments, prediction, raw_outputs in x:
        #softmax to get probablities from raw_outputs
        raw_outputs = raw_outputs.reshape(1,2)
        raw_outputs = softmax(raw_outputs, axis=1)

        tidy_output.append([comments, prediction, raw_outputs[0][1]])
    
    df = pd.DataFrame(tidy_output, columns=["comments", "prediction", "probability_class_one"])
    return df

def predict_comments(filename, modelname, len_output):
    #input has to be list
    apply_df = pd.read_csv(filename, sep="\t")
    apply_lst = apply_df['comment'].tolist()
    
    #specifies output length
    print("the whole list consists of {} elements".format(len(apply_lst)))  
    if len_output == 0:
        len_output = len(apply_lst)
        apply_lst = apply_lst
    else:
        apply_lst = apply_lst[:len_output]
    print("the application list consists of {} elements".format(len(apply_lst)))
    
    # specify model used
    model = ClassificationModel('distilbert', modelname, use_cuda=False)
    print("the model {} is loaded".format(modelname))
    
    # apply model
    predictions, prediction_values = model.predict(apply_lst)    

    return apply_lst, predictions, prediction_values


if __name__ == '__main__':
    length_output = int(input("please specify length (0 = all)"))
    apply_lst, predictions, raw_outputs = predict_comments("comment_downloads/data_clean_all.tsv", "model_p82", length_output)
    df = tidy_and_save(apply_lst, predictions, raw_outputs)
    df.to_csv("classification_all_onego.tsv", sep="\t")