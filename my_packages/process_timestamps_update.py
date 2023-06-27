import re
import pandas as pd


def delete_seconds(stamp):
    time_without_sec = []
    for x in stamp:
        x = x.split(":")
        x = x[0]
        time_without_sec.append(int(x))
    return time_without_sec


def stamp_to_second(stamp):
    list_sec_in_vid = []
    for x in stamp:
        x = x.split(":")
        minuten = int(x[0]) * 60
        sekunden = int(x[1])
        sec_in_vid = minuten + sekunden
        list_sec_in_vid.append(str(sec_in_vid))
    return list_sec_in_vid


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


def get_time(list_of_comments):
    list_of_times = []
    for text in list_of_comments:
        text = str(text)
        x = re.search(r"(?:([0-5]?[0-9]):)?([0-5]?[0-9]):([0-5][0-9])", text)
        if x is not None:
            str_with_time = x.group()
            list_of_times.append(str_with_time)
        else:
            pass
    return list_of_times


def round_stamps_10(stamps):
    out = []
    for txt in stamps:
        split_list = txt.split(":")
        if len(split_list) == 2:
            minutes, seconds = split_list
            seconds = int(seconds) / 10
            seconds = round(seconds)
            seconds = seconds * 10
            if seconds == 60:
                seconds = "00"
                minutes = int(minutes) + 1
            elif seconds == 0:
                seconds = '00'
            tpl = (str(minutes), str(seconds))
            rounded = ':'.join(tpl)
            out.append(rounded)
        else:
            pass
    return out

def plot_time_stamps(comment_list):
    extracted_time_stamps = get_time(comment_list)
    round_stamps_10_list = round_stamps_10(extracted_time_stamps)
    stamps_with_false_comma = []
    for stamp in round_stamps_10_list:
        sp = stamp.split(":")
        false_comma = ".".join(sp)
        stamps_with_false_comma.append(float(false_comma))

    set_of_stamps = list(set(stamps_with_false_comma))
    set_of_stamps.sort()

    plot_dict = {}
    for stamp in set_of_stamps:
        count = stamps_with_false_comma.count(stamp)
        plot_dict[stamp] = count

    keys = []
    values = []
    for key in plot_dict:
        key_string = str(key)
        sp = key_string.split(".")
        new_key = ":".join(sp)
        new_key = new_key+"0"
        keys.append(new_key)
        values.append(plot_dict[key])
    new_dict = dict(zip(keys, values))

    return new_dict

