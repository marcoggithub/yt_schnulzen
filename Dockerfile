FROM jupyter/scipy-notebook

RUN pip install joblib
RUN pip install pandas regex numpy matplotlib
RUN pip install google-api-python-client langdetect tabloo 
RUN pip install scikit-learn
RUN pip install tqdm
RUN pip install transformers==4.24.0
RUN pip install simpletransformers==0.63.11
RUN pip install torch


# on host machine:

## create image:
## -> $docker build -t {IMAGENAME} .
## -> The . at the end of the docker build command tells that Docker should look for the Dockerfile in the current directory.

## create container:
## $docker run -p 8888:8888 -v {host_dir}:/home/jovyan {IMAGENAME}
## -> this Folder should be the host_dir (e.g. /Users/qbukold/Heavy_Projects/GitHub/yt_schnulzen)

## Use container:
## Paste 2. URL given by Notebook afer docker run into Websoftware like Firefox
## -> The URL should be printed under "Or copy and paste one of these URLs:" in your Terminal
