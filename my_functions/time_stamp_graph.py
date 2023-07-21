import matplotlib.pyplot as plt

def plot_time_stamp(df, origin_name : str, max_min : str = "5:00", save : bool = True, show_data : bool = False):
    df = df[df["origin"] == origin_name]
    df = df[df["time_stamps"] != "NA"]
    ts_list = list(df["time_stamps"])

    #flatten list
    ts_list = [item for sublist in ts_list for item in sublist]
    print("the dataset consists of {} time stamps".format(len(ts_list)))

    #round to :10
    ts_list_rounded = round_stamps_10(ts_list)

    # sort individual ts
    ts_set = list(set(ts_list_rounded))
    ts_set.sort()

    ## create list of all posible values:
    max_time = max_min.split(":")
    max_minute = int(max_time[0])
    max_second = int(max_time[1])
    range_minute = max_minute
    range_second = int(max_second/10)
    if range_second == 0:
        range_minute -= 1
        range_second = 5
        full_minute = True

    all_values = []
    for min in range(int(range_minute+1)):
        for sec in range(range_second+1):
            sec = str(sec) + "0" 
            value = ":".join([str(min), str(sec)])
            all_values.append(value)
    if full_minute == True:
        full_minute_str = ":".join([str(range_minute+1), "00"])
        all_values.append(full_minute_str)

    #count
    plot_dict = {}
    for ts in all_values:
        count = ts_list_rounded.count(ts)
        plot_dict[ts] = count
    
    #show data
    if show_data == True:
        print(*plot_dict.items(), sep="\n")

    # create x and y data
    myList = plot_dict.items()
    x, y = zip(*myList)

    ## PLOT
    fig, ax = plt.subplots()
    ax.plot(x, y, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=10)
    fig.set_figwidth(10)
    fig.set_figheight(4)
    ax.set_title(f"Number of Time Stamps per 10-Seconds - {origin_name}")
    plt.xlabel('Time in Video')
    plt.ylabel('Number of Time-Stamps')
    plt.xticks(rotation=90)
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%M:%S'))
    plt.grid()
    if save == True:
        plt.savefig(f'figures/{origin_name}-{sum(plot_dict.values())}.png')
        print(f"plot is saved unter figures/figures/{origin_name}-{sum(plot_dict.values())}.png")
    plt.show()

    return plot_dict

def round_stamps_10(ts_list) -> list:
    out_lst = []

    for ts in ts_list:
        split_list = ts.split(":")

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
            out_lst.append(rounded)
        else:
            pass

    return out_lst