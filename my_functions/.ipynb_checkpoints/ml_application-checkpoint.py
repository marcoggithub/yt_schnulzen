import pandas as pd
from scipy.special import softmax
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import simpletransformers
# https://pypi.org/project/simpletransformers/ <- source evaluation tipps
from scipy.special import softmax
import os

def apply_model_in_jupyter(lst, modelname):
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    model_args = ClassificationArgs(use_multiprocessing=False, use_multiprocessing_for_evaluation=False)
    model = ClassificationModel('distilbert', modelname, use_cuda=False, args=model_args)  
    
    print("the application list consists of {} elements".format(len(lst)))
    # apply model for comments with TS
    predictions, prediction_values = model.predict(lst)
    # tidy results
    x = list(zip(lst, predictions, prediction_values))
    tidy_output = []
    for comments, prediction, raw_outputs in x:
        #softmax to get probablities from raw_outputs
        raw_outputs = raw_outputs.reshape(1,2)
        raw_outputs = softmax(raw_outputs, axis=1)
        tidy_output.append([comments, prediction, raw_outputs[0][1]])
    #save output as df
    df = pd.DataFrame(tidy_output, columns=["comments", "prediction", "probability_class_one"])
    
    return df


def grad_der_schnulzigkeit(df, origin : str):
    df_selected = df[df["origin"] == origin]
    #shuffel
    df_selected = df_selected.sample(frac=1).reset_index()
    
    #split comments with ts from rest
    df_output_no = df_selected[df_selected["time_stamps"].isnull()]
    df_output_ts = df_selected[~df_selected["time_stamps"].isnull()]
    
    # number of comments
    n_comments_no = df_output_no.shape[0]
    n_comments_ts = df_output_ts.shape[0]
    # number of class 1 (schnulze)
    n_sn_no = df_output_no[df_output_no["prediction"] == 1].shape[0]
    n_sn_ts = df_output_ts[df_output_ts["prediction"] == 1].shape[0]
    # avg strongness of class 1
    percentage_sn_no = df_output_no["probability_class_one"].mean()
    percentage_sn_ts = df_output_ts["probability_class_one"].mean()
    
    data = [['without ts', n_comments_no, n_sn_no, n_sn_no/n_comments_no, percentage_sn_no], 
            ['only ts', n_comments_ts, n_sn_ts, n_sn_ts/n_comments_ts, percentage_sn_ts]]
    df = pd.DataFrame(data, columns=['Type of Comment', 'N of Comments', 'N of Schnulzen-Comments', 'Avg. N of Schnulzen-Comments', 'Avg. Schnulzengrad'])
    
    return df
