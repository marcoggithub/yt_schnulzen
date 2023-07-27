# using my script to classify tweets to classify youtube comments:

from simpletransformers.classification import ClassificationModel, ClassificationArgs

# https://pypi.org/project/simpletransformers/ <- source evaluation tipps
from scipy.special import softmax

# https://github.com/ThilinaRajapakse/simpletransformers/issues/30
import pandas as pd
from sys import argv
from sys import stderr
import os

def new_model():
    # Load and split Annotation Datasets
    dataset1 = pd.read_csv("bert/annotation_data/annotate_1000_final.tsv", sep="\t")
    dataset1.rename(columns={"comment": "text", "category": "labels"}, inplace=True)
    dataset1 = dataset1[["comment", "labels"]]
    dataset2 = pd.read_csv("bert/annotation_data/annotate_1242_mg&qb.csv", sep=";")
    dataset2.rename(columns={"comments": "text", "human_prediction": "labels"}, inplace=True)
    dataset2 = dataset2[["comment", "labels"]]
    dataset = pd.merge(dataset1, dataset2)

    dataset = dataset[["text", "labels"]]
    dataset = dataset[dataset["labels"] != -1]
    print(dataset["labels"].value_counts())

    train_df, eval_df = split_data(dataset, "text", categories_columnname="labels")

    train_model(dataset, modelname="final_model")
    #eval_model(eval_df, modelname="final_model")


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
