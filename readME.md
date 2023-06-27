Alle Vorgänge lassen sich von den beiden Jupyter-Notebooks steuern. Installieren Sie also Jupyter-Notebook oder eine ähnliche Software zuerst. Öffenen Sie dann "YT-Comment-Classificator" und "YT-Download_Comments". Sie werden außerdem einige Python Packages brauchen.

# Benötigte Packages
re
json
numpy
pandas
matplotlib
csv

langdetect
simpletransformers
sys
os
=> Es werden außerdem die von uns eigens programmierten Funktionen im "my_packages"-Ordner importiert

# YT-Download_Comments
Dieses Notebook ermöglicht dem User beliebig viele Kommentare eines YT-Videos herunterzuladen. Er wird diese als .csv Datei speichern können und nach Kommentaren einer beliebigen Sprache filtern können. Außerdem können alle Emojies gelöscht werden. 
Außerdem im Notebook ist ein Funktion um sog. time-stamp-comments zu analysieren. Also Kommentare, die im Format "00:00" einen Zeitpunkt im Video referenzieren. Diese time-stamps lassen sich dann grafisch darstellen.

# YT-Comment-Classificator
Dieses Notebook ermöglich Training, Evaluation und Anwendung eines binären maschine-learning Klassifikators, basierend auf BERT. Es lässt sich eine Annotationstabelle an Kommentaren zusammenstellen, ein Modell trainieren und abspeichern, testen und auf eine neue Liste an Kommentaren anwenden.


download comments to dataframe via command "**my_video.get_comments(dev_key, number of comments, order)**"

- dev_key = Developer Key given by YouTube for the 
- my_video = video_class name from last cell
- len_output = approx number of comments
- order can be set to "relevance" or "time"