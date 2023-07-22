# encoding=utf-8
### All my Simpletransformers apply functions
# pip install simpletransformers==0.63.9
# split_data()
# train_model()
# eval_model()


from simpletransformers.classification import ClassificationModel, ClassificationArgs

# https://pypi.org/project/simpletransformers/ <- source evaluation tipps
from scipy.special import softmax

# https://github.com/ThilinaRajapakse/simpletransformers/issues/30
import pandas as pd
from sys import argv
from sys import stderr
import os
import logging

# logging.basicConfig(level=logging.INFO)
# transformers_logger = logging.getLogger("transformers")
# transformers_logger.setLevel(logging.INFO)

# os.environ["TOKENIZERS_PARALLELISM"] = "false"


# split annotation dataset
def split_data(annotations, text_columnname: str, categories_columnname: str):
    print("splitting annotation dataset")
    # shuffle data and drop old index
    annotations = annotations.sample(frac=1, random_state=1).reset_index(drop=True)

    # create training-data <-- df
    train_df = annotations.head(int(len(annotations) * 0.8))
    selected_columns = [text_columnname, categories_columnname]
    train_df = train_df[selected_columns]

    # create eval-data <-- df
    eval_df = annotations.tail(int(len(annotations) * 0.2))
    selected_columns = [text_columnname, categories_columnname]
    eval_df = eval_df[selected_columns]

    print(len(train_df))
    print(len(eval_df))

    return train_df, eval_df


## create and save model
def train_model(train_df, evaluation_df=None, modelname="my_model"):
    # toggle logging
    # from transformers.utils import logging
    # logging.set_verbosity_info()

    # TOKENIZERS_PARALLELISM=True

    # Optional model configuration
    model_args = ClassificationArgs(
        num_train_epochs=3,
        train_batch_size=32,
        overwrite_output_dir=True,
        use_multiprocessing=False,
        use_multiprocessing_for_evaluation=False,
    )

    '''
    With this configuration, the training will terminate if the mcc score
    of the model on the test data does not improve upon the best mcc score
    by at least 0.01 for 5 consecutive evaluations. 
    An evaluation will occur once for every 1000 training steps.
    
    '''

    # model_args.use_early_stopping = True
    # model_args.early_stopping_delta = 0.01
    # model_args.early_stopping_metric = "mcc"
    # model_args.early_stopping_metric_minimize = False
    # model_args.early_stopping_patience = 5
    # model_args.evaluate_during_training_steps = 10
    # model_args.evaluate_during_training=True
    # model_args.evaluate_during_training_verbose=True
    # model_args.eval_batch_size = 8
    

    model = ClassificationModel(
        "distilbert",
        "distilbert-base-uncased",
        use_cuda=False,
        args=model_args,
        weight=[0.625, 2.5],
    )
    # --> set cuda to True, if available

    # start training#
    model.train_model(train_df, eval_df=evaluation_df)

    # save model
    model.model.save_pretrained(modelname)
    model.tokenizer.save_pretrained(modelname)
    model.config.save_pretrained(f"{modelname}/")


### evaluate model
# evaluate model
def eval_model(eval_df, modelname):
    # reload model (if needed)
    model_args = ClassificationArgs(use_multiprocessing_for_evaluation=False)
    model = ClassificationModel(
        "distilbert", modelname, use_cuda=False, args=model_args
    )

    # start evaluation
    print("Starting Evaluation:")
    result, model_outputs, wrong_predictions = model.eval_model(eval_df)

    # print results
    print("Results:")
    for i in result:
        print(i, result[i])

    # tp = true positives
    # tn = true negatives
    # fp = false positives
    # fn = false negaives
    # auroc = precision
    # auprc = average precison

    # print all wrong preductions (if wanted)
    # for n, dic in enumerate(wrong_predictions):
    #    print("Annotation Label:", dic.label)
    #    print(dic.text_a)
    #    print(10*'+')