import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def mk_dir():
    """Makes output directories
    """

    print("Generting output structure")
    if not os.path.exists('figures'):
        os.makedirs('figures')
    if not os.path.exists('figures/eps'):
        os.makedirs('figures/eps')
    if not os.path.exists('figures/png'):
        os.makedirs('figures/png')


def plot_single(df, argument, templates, file_name, xlabel):
    plt.rcParams["figure.figsize"] = (7, 4)
    if argument == "sf":
        df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).time.max().unstack().plot.barh()
        plt.yticks(ticks=np.arange(2), labels=("blocks", "chain"))
    if argument == "num_right":
        df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.max().unstack().plot.barh()
        plt.yticks(ticks=np.arange(2), labels=("blocks", "chain"))
    if argument == "num_per":
        df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.max().unstack().plot.barh()
        plt.yticks(ticks=np.arange(2), labels=("blocks", "chain"))
    if argument == "data_rate":
        df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.max().unstack().plot.barh()
        plt.yticks(ticks=np.arange(2), labels=("blocks", "chain"))

    if argument == "mean_num":
        df.groupby(
            ['template', 'mean']).num_right.mean().unstack().plot.barh()
        plt.yticks(visible=False)
    if argument == "frame_period_num":
        df.groupby(
            ['template', 'frame_period']).num_right.sum().unstack().plot.barh()
        plt.yticks(visible=False)
    if argument == "cr_num":
        df.groupby(
            ['template', 'cr']).num_right.sum().unstack().plot.barh()
        plt.yticks(visible=False)
    if argument == "has_crc_num":
        df.groupby(
            ['template', 'has_crc']).num_right.sum().unstack().plot.barh()
        plt.yticks(visible=False)

    if argument == "mean_time":
        df.groupby(
            ['template', 'mean']).time.mean().unstack().plot.barh()
        plt.yticks(visible=False)
    if argument == "frame_period_time":
        df.groupby(
            ['template', 'frame_period']).time.mean().unstack().plot.barh()
        plt.yticks(visible=False)
    if argument == "cr_time":
        df.groupby(
            ['template', 'cr']).time.mean().unstack().plot.barh()
        plt.yticks(visible=False)
    if argument == "has_crc_time":
        df.groupby(
            ['template', 'has_crc']).time.mean().unstack().plot.barh()
        plt.yticks(visible=False)

    # ax = plt.axes()
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
    #           ncol=3, fancybox=True, shadow=True)
    plt.ylabel("")
    plt.xlabel(xlabel)
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_single_nruns(df, argument, templates, file_name, xlabel):
    plt.rcParams["figure.figsize"] = (7, 4)

    if argument == "sf":
        mean = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('mean').unstack().values.tolist()[0]
        minval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('min').unstack().values.tolist()[0]
        maxval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('max').unstack().values.tolist()[0]
    if argument == "num_right":
        mean = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('mean').unstack().values.tolist()[0]
        minval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('min').unstack().values.tolist()[0]
        maxval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('max').unstack().values.tolist()[0]
    if argument == "num_per":
        mean = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('mean').unstack().values.tolist()[0]
        minval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('min').unstack().values.tolist()[0]
        maxval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('max').unstack().values.tolist()[0]
    if argument == "data_rate":
        mean = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('mean').unstack().values.tolist()[0]
        minval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('min').unstack().values.tolist()[0]
        maxval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('max').unstack().values.tolist()[0]

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    # fig, ax = plt.subplots()
    sf = [7, 8, 9, 10, 11, 12]
    colors = ['tab:blue', 'tab:orange', 'tab:green',
              'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(sf, mean, xerr=errors, capsize=6, label=sf, color=colors)
    plt.yticks(sf)
    plt.ylabel("$SF$")
    plt.xlabel(xlabel)
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_grouped_single(df1, df2, argument, templates, file_name, xlabel, label_high, label_low):
    plt.rcParams["figure.figsize"] = (8, 6)
    barwidth = 0.4
    if argument == "sf":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('mean').unstack().values.tolist()[0]
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('min').unstack().values.tolist()[0]
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('max').unstack().values.tolist()[0]
    if argument == "num_right":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('mean').unstack().values.tolist()[0]
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('min').unstack().values.tolist()[0]
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('max').unstack().values.tolist()[0]
    if argument == "num_per":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('mean').unstack().values.tolist()[0]
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('min').unstack().values.tolist()[0]
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('max').unstack().values.tolist()[0]
    if argument == "data_rate":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('mean').unstack().values.tolist()[0]
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('min').unstack().values.tolist()[0]
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('max').unstack().values.tolist()[0]

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    # fig, ax = plt.subplots()
    sf = [7, 8, 9, 10, 11, 12]
    colors = ['tab:blue', 'tab:orange', 'tab:green',
              'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(sf, mean, barwidth, xerr=errors, capsize=6, label=label_low)

    if argument == "sf":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('mean').unstack().values.tolist()[0]
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('min').unstack().values.tolist()[0]
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).time.agg('max').unstack().values.tolist()[0]
    if argument == "num_right":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('mean').unstack().values.tolist()[0]
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('min').unstack().values.tolist()[0]
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.agg('max').unstack().values.tolist()[0]
    if argument == "num_per":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('mean').unstack().values.tolist()[0]
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('min').unstack().values.tolist()[0]
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('max').unstack().values.tolist()[0]
    if argument == "data_rate":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('mean').unstack().values.tolist()[0]
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('min').unstack().values.tolist()[0]
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).data_rate.agg('max').unstack().values.tolist()[0]

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    # fig, ax = plt.subplots()
    sf = [7 + barwidth, 8 + barwidth, 9 + barwidth,
          10 + barwidth, 11 + barwidth, 12 + barwidth]

    plt.barh(sf, mean, barwidth, xerr=errors, capsize=6, label=label_high)

    yticks = [7 + barwidth / 2, 8 + barwidth / 2, 9 + barwidth /
              2, 10 + barwidth / 2, 11 + barwidth / 2, 12 + barwidth / 2]
    ylabels = [7, 8, 9, 10, 11, 12]
    plt.yticks(yticks, labels=ylabels)
    plt.ylabel("$SF$")
    plt.xlabel(xlabel)
    plt.legend()
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_multi(df, argument, templates, file_name, xlabel):
    plt.rcParams["figure.figsize"] = (7, 4)

    colors = ['tab:blue', 'tab:orange', 'tab:green',
              'tab:red', 'tab:purple', 'tab:brown']

    if argument == "sf":
        df[df['template'].isin(templates)].groupby(
            ['template']).time.max().plot.barh(color=colors)
    if argument == "num_right":
        df[df['template'].isin(templates)].groupby(
            ['template']).num_right.max().plot.barh(color=colors)
    if argument == "num_per":
        df[df['template'].isin(templates)].groupby(
            ['template']).num_right.max().plot.barh(color=colors)
    if argument == "data_rate":
        df[df['template'].isin(templates)].groupby(
            ['template']).data_rate.max().plot.barh(color=colors)

    plt.yticks(ticks=np.arange(6), labels=("1", "2", "3", "4", "5", "6"))
    plt.ylabel("$N_{Tx}$")
    plt.xlabel(xlabel)
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_multi_nruns(df, argument, templates, file_name, xlabel):
    plt.rcParams["figure.figsize"] = (7, 4)
    colors = ['tab:blue', 'tab:orange', 'tab:green',
              'tab:red', 'tab:purple', 'tab:brown']

    if argument == "sf":
        mean = df[df['template'].isin(templates)].groupby(
            ['template']).time.agg('mean').values.tolist()
        minval = df[df['template'].isin(templates)].groupby(
            ['template']).time.agg('min').values.tolist()
        maxval = df[df['template'].isin(templates)].groupby(
            ['template']).time.agg('max').values.tolist()
    if argument == "num_right":
        mean = df[df['template'].isin(templates)].groupby(
            ['template']).num_right.agg('mean').values.tolist()
        minval = df[df['template'].isin(templates)].groupby(
            ['template']).num_right.agg('min').values.tolist()
        maxval = df[df['template'].isin(templates)].groupby(
            ['template']).num_right.agg('max').values.tolist()
    if argument == "num_per":
        mean = df[df['template'].isin(templates)].groupby(
            ['template']).num_per.agg('mean').values.tolist()
        minval = df[df['template'].isin(templates)].groupby(
            ['template']).num_per.agg('min').values.tolist()
        maxval = df[df['template'].isin(templates)].groupby(
            ['template']).num_per.agg('max').values.tolist()
    if argument == "data_rate":
        mean = df[df['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('mean').values.tolist()
        minval = df[df['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('min').values.tolist()
        maxval = df[df['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('max').values.tolist()
    if argument == "load":
        mean = df[df['template'].isin(templates)].groupby(
            ['template']).load.agg('mean').values.tolist()
        minval = df[df['template'].isin(templates)].groupby(
            ['template']).load.agg('min').values.tolist()
        maxval = df[df['template'].isin(templates)].groupby(
            ['template']).load.agg('max').values.tolist()

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    yval = []
    for i in range(1, len(mean) + 1):
        yval.append(i)

    colors = ['tab:blue', 'tab:orange', 'tab:green',
              'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(yval, mean, xerr=errors, capsize=6, label=yval, color=colors)
    plt.yticks(yval)
    plt.ylabel("$N_{Tx}$")
    plt.xlabel(xlabel)
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_grouped_nruns_multi(df1, df2, argument, templates, file_name, xlabel, label_high, label_low):
    plt.rcParams["figure.figsize"] = (7, 6)
    colors = ['tab:blue', 'tab:orange', 'tab:green',
              'tab:red', 'tab:purple', 'tab:brown']

    bar_width = 0.4

    # do first df
    if argument == "sf":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template']).time.agg('mean').values.tolist()
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template']).time.agg('min').values.tolist()
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template']).time.agg('max').values.tolist()
    if argument == "num_right":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_right.agg('mean').values.tolist()
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_right.agg('min').values.tolist()
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_right.agg('max').values.tolist()
    if argument == "num_per":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_per.agg('mean').values.tolist()
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_per.agg('min').values.tolist()
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_per.agg('max').values.tolist()
    if argument == "data_rate":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('mean').values.tolist()
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('min').values.tolist()
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('max').values.tolist()
    if argument == "load":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template']).load.agg('mean').values.tolist()
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template']).load.agg('min').values.tolist()
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template']).load.agg('max').values.tolist()

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    yval = []
    for i in range(1, len(mean) + 1):
        yval.append(i)
        ylabels = yval

    # colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(yval, mean, bar_width, xerr=errors,
             capsize=6, label=label_low)

    # do second df
    if argument == "sf":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template']).time.agg('mean').values.tolist()
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template']).time.agg('min').values.tolist()
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template']).time.agg('max').values.tolist()
    if argument == "num_right":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_right.agg('mean').values.tolist()
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_right.agg('min').values.tolist()
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_right.agg('max').values.tolist()
    if argument == "num_per":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_per.agg('mean').values.tolist()
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_per.agg('min').values.tolist()
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_per.agg('max').values.tolist()
    if argument == "data_rate":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('mean').values.tolist()
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('min').values.tolist()
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template']).data_rate.agg('max').values.tolist()
    if argument == "load":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template']).load.agg('mean').values.tolist()
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template']).load.agg('min').values.tolist()
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template']).load.agg('max').values.tolist()

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    yval = []
    yticks = []
    for i in range(1, len(mean) + 1):
        yval.append(i + bar_width)
        yticks.append(i + bar_width / 2)

    # colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(yval, mean, bar_width, xerr=errors,
             capsize=6, label=label_high)

    plt.yticks(yticks, labels=ylabels)
    plt.ylabel("$N_{Tx}$")
    plt.xlabel(xlabel)
    plt.legend()
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def main():
    """Main function
    """
    print("Welcome to the plotter..")
    mk_dir()
    print("Going to plot all single values")
    templates = ["lora_sim_chain"]
    file_name = "../results/profiled_single.csv"
    df = pd.read_csv(file_name)
    # low values
    df_single = df.loc[df['mean'] == 200]
    string_time = "Execution time [s]"
    string_right = "Number of correctly decoded messages"
    string_percentage = "$\eta \, [\%]$"
    string_data_rate = "Throughput [bytes/s]"
    string_load = "Average 1-min load"
    label_high = "$t_{wait}=1000$ [ms]"
    label_low = "$t_{wait}=200$ [ms]"

    plot_single(df_single, "sf", templates, "s_time_low", string_time)
    plot_single(df_single, "s_num_right_low", templates, "sf_num_right",
                string_right)
    plot_single(df_single, "num_per", templates,
                "s_num_per_low", string_percentage)
    plot_single(df_single, "data_rate", templates,
                "s_data_rate_low", string_data_rate)

    # high values
    df_single = df.loc[df['mean'] == 1000]
    plot_single(df_single, "sf", templates, "s_time_high", string_time)
    plot_single(df_single, "s_num_right_high", templates, "sf_num_right",
                string_right)
    plot_single(df_single, "num_per", templates,
                "s_num_per_high", string_percentage)
    plot_single(df_single, "data_rate", templates,
                "s_data_rate_high", string_data_rate)

    # dynamic results
    file_name = "../results/profiled_single_dyn.csv"
    df_single_dyn = pd.read_csv(file_name)
    plot_single(df_single_dyn, "mean_num", "lora_sim_multi1",
                "s_mean_num", "Total number of correctly decoded messages")
    plot_single(df_single_dyn, "frame_period_num", "lora_sim_multi1",
                "s_frame_period_num", "Total number of correctly decoded messages")
    plot_single(df_single_dyn, "cr_num", "lora_sim_multi1",
                "s_cr_num", "Total number of correctly decoded messages")
    plot_single(df_single_dyn, "has_crc_num", "lora_sim_multi1",
                "s_has_crc_num", "Total number of correctly decoded messages")
    plot_single(df_single_dyn, "mean_time", "lora_sim_multi1",
                "s_mean_time", string_time)
    plot_single(df_single_dyn, "frame_period_time", "lora_sim_multi1",
                "s_frame_period_time", string_time)
    plot_single(df_single_dyn, "cr_time", "lora_sim_multi1",
                "s_cr_time", string_time)
    plot_single(df_single_dyn, "has_crc_time", "lora_sim_multi1",
                "s_has_crc_time", string_time)
    #
    # #low values
    file_name = "../results/profiled_single_runs.csv"
    df = pd.read_csv(file_name)
    df_single_low_n = df.loc[df['mean'] == 200]
    df_single_high_n = df.loc[df['mean'] == 1000]
    plot_single_nruns(df_single_low_n, "sf", templates,
                      "nsruns_time_low", string_time)
    plot_single_nruns(df_single_low_n, "num_right", templates,
                      "nsruns_nright_low", string_right)
    plot_single_nruns(df_single_low_n, "num_per", templates,
                      "nsruns_num_per_low", string_percentage)
    plot_single_nruns(df_single_low_n, "data_rate", templates,
                      "nsruns_data_rate_low", string_data_rate)
    # #high values

    plot_single_nruns(df_single_high_n, "sf", templates,
                      "nsruns_time_high", string_time)
    plot_single_nruns(df_single_high_n, "num_right", templates,
                      "nsruns_nright_high", string_right)
    plot_single_nruns(df_single_high_n, "num_per", templates,
                      "nsruns_num_per_high", string_percentage)
    plot_single_nruns(df_single_high_n, "data_rate", templates,
                      "nsruns_data_rate_high", string_data_rate)
    # grouped plots
    plot_grouped_single(df_single_low_n, df_single_high_n, "sf", templates,
                        "nsruns_time_grouped", string_time, label_high, label_low)
    plot_grouped_single(df_single_low_n, df_single_high_n, "num_right", templates,
                        "nsruns_nright_grouped", string_right, label_high, label_low)
    plot_grouped_single(df_single_low_n, df_single_high_n, "num_per", templates,
                        "nsruns_num_per_grouped", string_percentage, label_high, label_low)
    plot_grouped_single(df_single_low_n, df_single_high_n, "data_rate", templates,
                        "nsruns_ndata_rate_grouped", string_data_rate, label_high, label_low)
    # 100 frames
    # #low values
    file_name = "../results/profiled_single_runs_frames100.csv"
    df = pd.read_csv(file_name)
    df_single_low_n = df.loc[df['mean'] == 200]
    df_single_high_n = df.loc[df['mean'] == 1000]
    plot_single_nruns(df_single_low_n, "sf", templates,
                      "nsruns_time_low_frames", string_time)
    plot_single_nruns(df_single_low_n, "num_right", templates,
                      "nsruns_nright_low_frames", string_right)
    plot_single_nruns(df_single_low_n, "num_per", templates,
                      "nsruns_num_per_low_frames", string_percentage)
    plot_single_nruns(df_single_low_n, "data_rate", templates,
                      "nsruns_data_rate_low_frames", string_data_rate)
    # #high values

    plot_single_nruns(df_single_high_n, "sf", templates,
                      "nsruns_time_high_frames", string_time)
    plot_single_nruns(df_single_high_n, "num_right", templates,
                      "nsruns_nright_high_frames", string_right)
    plot_single_nruns(df_single_high_n, "num_per", templates,
                      "nsruns_num_per_high_frames", string_percentage)
    plot_single_nruns(df_single_high_n, "data_rate", templates,
                      "nsruns_data_rate_high_frames", string_data_rate)
    # grouped plots
    plot_grouped_single(df_single_low_n, df_single_high_n, "sf", templates,
                        "nsruns_time_grouped_frames", string_time, label_high, label_low)
    plot_grouped_single(df_single_low_n, df_single_high_n, "num_right", templates,
                        "nsruns_nright_grouped_frames", string_right, label_high, label_low)
    plot_grouped_single(df_single_low_n, df_single_high_n, "num_per", templates,
                        "nsruns_num_per_grouped_frames", string_percentage, label_high, label_low)
    plot_grouped_single(df_single_low_n, df_single_high_n, "data_rate", templates,
                        "nsruns_ndata_rate_grouped_frames", string_data_rate, label_high, label_low)

    templates = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3",
                 "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]

    print("Going to plot all single values")
    file_name = "../results/profiled_multi.csv"
    df = pd.read_csv(file_name)
    df_multi = df.loc[df['mean'] == 200]

    plot_multi(df_multi, "sf", templates,
               "m_time_low", string_time)
    plot_multi(df_multi, "num_right", templates,
               "m_num_right_low", "Number of rightly decoded messages")
    plot_multi(df_multi, "num_per", templates,
               "m_num_per_low", string_percentage)

    df_multi = df.loc[df['mean'] == 1000]
    plot_multi(df_multi, "sf", templates,
               "m_time_high", string_time)
    plot_multi(df_multi, "num_right", templates,
               "m_num_right_high", "Number of rightly decoded messages")
    plot_multi(df_multi, "num_per", templates,
               "m_num_per_high", string_percentage)
    plot_multi(df_multi, "data_rate", templates,
               "m_data_rate_high", string_data_rate)

    file_name = "../results/profiled_multi_runs.csv"
    df = pd.read_csv(file_name)
    df_multi_n_low = df.loc[df['mean'] == 200]
    df_multi_n_high = df.loc[df['mean'] == 1000]

    plot_multi_nruns(df_multi_n_low, "sf", templates,
                     "nmruns_time_low", string_time)
    plot_multi_nruns(df_multi_n_low, "num_right", templates,
                     "nmruns_num_right_low", string_right)
    plot_multi_nruns(df_multi_n_low, "num_per", templates,
                     "nmruns_num_per_low", string_percentage)
    plot_multi_nruns(df_multi_n_low, "load", templates,
                     "nmruns_load_low", string_load)
    plot_multi_nruns(df_multi_n_low, "data_rate", templates,
                     "nmruns_data_rate_low", string_data_rate)

    plot_multi_nruns(df_multi_n_high, "sf", templates,
                     "nmruns_time_high", string_time)
    plot_multi_nruns(df_multi_n_high, "num_right", templates,
                     "nmruns_num_right_high", string_right)
    plot_multi_nruns(df_multi_n_high, "num_per", templates,
                     "nmruns_num_per_high", string_percentage)
    plot_multi_nruns(df_multi_n_high, "load", templates,
                     "nmruns_load_high", string_load)
    plot_multi_nruns(df_multi_n_high, "data_rate", templates,
                     "nmruns_data_rate_high", string_data_rate)

    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "sf", templates,
                             "nmruns_time_grouped", string_time, label_high, label_low)
    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "num_right", templates,
                             "nmruns_num_right_grouped", string_right, label_high, label_low)
    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "num_per", templates,
                             "nmruns_num_per_grouped", string_percentage, label_high, label_low)
    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "load", templates,
                             "nmruns_load_grouped", string_load, label_high, label_low)
    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "data_rate", templates,
                             "nmruns_data_rate_grouped", string_data_rate, label_high, label_low)


main()
