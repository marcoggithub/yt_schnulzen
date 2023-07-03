# encoding=utf-8
import sys
#machine learning packages
from simpletransformers.classification import ClassificationModel, ClassificationArgs
# https://pypi.org/project/simpletransformers/ <- source evaluation tipps
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
    apply_lst = apply_lst[:5]
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

    return output


output = predict_comments("comment_downloads/data_combined_53221_V2.tsv", "model_p82")
print(output)




'''





#list_of_filters = [["Ed_Sheeran-Thinking_Out_Loud", True], ["Tom_Odell-Another_Love", True], ["Kelly_Clarkson-Because_Of_You", True], ["Bruno_Mars-When_I_Was_Your_Man", True], ["John_Legend-All_of_Me", False]]


# load model
model = ClassificationModel('distilbert','model_p82', use_cuda=False)
#apply model

com_lst = []
pred_lst = []

for i, comment in enumerate(apply_lst):
    single_lst = []
    single_lst.append(comment)
    comment = single_lst
    print(i)
    predictions, raw_outputs = model.predict(comment)
    com_lst.append(comment)
    pred_lst.append(predictions)

print(20*"-")
print(filename, origin, time_stamp)

# output and save predictions
final = []
for i, comment in enumerate(com_lst):
  comment_row = (comment, str(pred_lst[i]))
  final.append(comment_row)

df = pd.DataFrame(final, columns =['txt', 'prediction'])

print("1 = schnulzig; 0 = nicht-schnulzig")
counts = df["prediction"].value_counts()
print(counts)
try:
    perc = counts.iloc[1]/(counts.iloc[0]+counts.iloc[1])
except:
    perc = 0
perc = '{:,.2%}'.format(perc)
print(f"{perc} der Kommentare wurden als schnulzig klassifiziert.")


filename = 'output.tsv'
df.to_csv(filename, sep='\t')
print(f"results saved in {filename}")

'''