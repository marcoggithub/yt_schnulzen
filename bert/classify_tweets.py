# using my script to classify tweets to classify youtube comments:

from simpletransformers.classification import ClassificationModel, ClassificationArgs

# https://pypi.org/project/simpletransformers/ <- source evaluation tipps
from scipy.special import softmax

# https://github.com/ThilinaRajapakse/simpletransformers/issues/30
import pandas as pd
from sys import argv
from sys import stderr
import os
import numpy as np

from classification_functions import train_model

"""
#requirements:
#pip install simpletransformers
#pip install scipy
#pip install torch

"""

if __name__ == "__main__":
    # Split Annotation Dataset
    dataset = pd.read_csv("/home/bukold/projects/yt_schnulzen/bert/annotation_data/annotate_1000_final.tsv", sep="\t")
    dataset.rename(columns={"comment": "text", "category": "labels"}, inplace=True)
    dataset = dataset[["text", "labels"]]
    dataset = dataset[dataset["labels"] != -1]
    print(dataset["labels"].value_counts())




    train_model(input_df = dataset, train_percent = 0.8, validate_percent = 0.1, modelname="eval_model_V1")


"""
calc weights of class

    n_samples=  43400,  n_classes= 2(0&1), n_sample0= 42617, n_samples1= 783
    Weights for class 0:
    w0=  43400/(2*42617) = 0.509
    Weights for class 1:
    w1= 43400/(2*783) = 27.713

940, 2, 752, 188

w0 = 940/(1504) = 0,625
w1 = 940/(376) = 2,5


"""
