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

def predict_comments(filename, modelname):

    # input has to be list
    apply_df = pd.read_csv(filename, sep="\t")
    apply_lst = apply_df['comment'].tolist()
    apply_lst = apply_lst[:1]
    print("the application list consists of {} elements".format(len(apply_lst)))
    
    # specify model used
    model = ClassificationModel('distilbert', modelname, use_cuda=False)
    print("the model {} is loaded".format(modelname))

    #main loop
    output = []
    for i, comment in enumerate(apply_lst):
        output_iteration = []
        input = [comment]
        print(i)
        predictions, prediction_values = model.predict(input)
        output_iteration.append(comment)
        output_iteration.append(predictions)
        output_iteration.append(prediction_values)
        output.append(output_iteration)

        if i == len(apply_lst):
            return output

    return output

if __name__ == '__main__':
    output = predict_comments("comment_downloads/data_clean_all.tsv", "model_p82")

    tidy_output = []
    for comments, prediction, raw_outputs in output:
        #softmax to get probablities from raw_outputs
        tidy_output.append([comments, prediction[0], softmax(raw_outputs, axis=1)[0][1]])
    
    df = pd.DataFrame(tidy_output, columns=["comments", "prediction", "probability_class_one"])
    df.to_csv("classification_all.tsv", sep="\t")