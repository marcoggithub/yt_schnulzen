import re

def extract_ts(comment : str, max_video_min : int = 10) -> list:
    ts = re.findall(rf"\d?\d:\d\d", comment)
    
    if ts != []:
        if check_if_true_ts(comment) == True:
            print(ts)

            return ts
        else: 
            return "NA"
    else:
        return "NA"


def check_if_true_ts(comment : str) -> bool:
    '''
    Romans 10:9
    23:23   -Hermosa elección-  xkissss.Uno
    01:08 a.m
    João 14:6
    '''
    critical_words = ["am", "pm", "a\.\s?m\.", "p\.\s?m\.", 'Genesis', 'Exodus', 'Leviticus',
                        'Deuteronomy', 'Joshua', 'Judges', 'Ruth',
                        'Samuel', 'Samuel', 'Kings', 'Kings',
                        'Chronicles', 'Chronicles', 'Ezra',
                        'Nehemiah', 'Tobit', 'Judith', 'Esther',
                        "Luke", 'Maccabees', 'Maccabees',
                        'Job', 'Psalms', 'Proverbs',
                        'Ecclesiastes', 'Song of Songs',
                        'Wisdom', 'Sirach', 'Isaiah',
                        'Jeremiah', 'Lamentations',
                        'Baruch', 'Ezekiel',
                        'Daniel', 'Hosea Joel',
                        'Amos', 'Obadiah',
                        'Jonah', 'Micah',
                        'Nahum', 'Habakkuk',
                        'Zephaniah', 'Haggai',
                        'Zechariah', 'Malachi',
                        'New Testament', 'Matthew',
                        #'Mark',
                        'Luke', 'John',
                        'Acts', 'Romans', 'Corinthians',
                        'Corinthians', 'Galatians', 'Ephesians',
                        'Philippians', 'Colossians', 'Thessalonians',
                        'Thessalonians', 'Timothy', 'Timothy',
                        'Titus', 'Philemon', 'Hebrews',
                        'James', 'Peter', 'Peter',
                        'John', 'John', 'John',
                        'Jude', 'Revelation']
    critical_words_regex = '|'.join(critical_words)
    ts_regex = r'\d{1}:\d{2}'

    pattern = re.compile("({ts}\s+({cw}))|(({cw})\s+{ts})".format(ts = ts_regex, cw = critical_words_regex),
                         flags=re.IGNORECASE)
    
    x = re.search(pattern, comment)
    
    if x != None:
        return False
    else:
        return True




