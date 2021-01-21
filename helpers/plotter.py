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
    if argument == "num_dec":
        df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.max().unstack().plot.barh()
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
    if argument == "num_dec":
        mean = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('mean').unstack().values.tolist()[0]
        minval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('min').unstack().values.tolist()[0]
        maxval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('max').unstack().values.tolist()[0]
    if argument == "num_per":
        mean = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('mean').unstack().values.tolist()[0]
        minval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('min').unstack().values.tolist()[0]
        maxval = df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('max').unstack().values.tolist()[0]

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
    plt.ylabel("Spreading Factor")
    plt.xlabel(xlabel)
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_grouped_single(df1, df2, argument, templates, file_name, xlabel):
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
    if argument == "num_dec":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('mean').unstack().values.tolist()[0]
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('min').unstack().values.tolist()[0]
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('max').unstack().values.tolist()[0]
    if argument == "num_per":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('mean').unstack().values.tolist()[0]
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('min').unstack().values.tolist()[0]
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('max').unstack().values.tolist()[0]

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
    plt.barh(sf, mean, barwidth, xerr=errors, capsize=6, label="mean=200[ms]")

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
    if argument == "num_dec":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('mean').unstack().values.tolist()[0]
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('min').unstack().values.tolist()[0]
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.agg('max').unstack().values.tolist()[0]
    if argument == "num_per":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('mean').unstack().values.tolist()[0]
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('min').unstack().values.tolist()[0]
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template', 'sf']).num_per.agg('max').unstack().values.tolist()[0]


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
    sf = [7+barwidth, 8+barwidth, 9+barwidth,
          10+barwidth, 11+barwidth, 12+barwidth]

    plt.barh(sf, mean, barwidth, xerr=errors, capsize=6, label="mean=1000[ms]")

    yticks = [7+barwidth/2, 8+barwidth/2, 9+barwidth /
              2, 10+barwidth/2, 11+barwidth/2, 12+barwidth/2]
    ylabels = [7, 8, 9, 10, 11, 12]
    plt.yticks(yticks, labels=ylabels)
    plt.ylabel("Spreading Factor")
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
    if argument == "num_dec":
        df[df['template'].isin(templates)].groupby(
            ['template']).num_right.max().plot.barh(color=colors)
    if argument == "num_dec":
        df[df['template'].isin(templates)].groupby(
            ['template']).num_per.max().plot.barh(color=colors)

    plt.yticks(ticks=np.arange(6), labels=("1", "2", "3", "4", "5", "6"))
    plt.ylabel("Number of sending Tx")
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
    if argument == "num_dec":
        mean = df[df['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('mean').values.tolist()
        minval = df[df['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('min').values.tolist()
        maxval = df[df['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('max').values.tolist()
    if argument == "num_per":
        mean = df[df['template'].isin(templates)].groupby(
            ['template']).num_per.agg('mean').values.tolist()
        minval = df[df['template'].isin(templates)].groupby(
            ['template']).num_per.agg('min').values.tolist()
        maxval = df[df['template'].isin(templates)].groupby(
            ['template']).num_per.agg('max').values.tolist()
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
    for i in range(1, len(mean)+1):
        yval.append(i)

    colors = ['tab:blue', 'tab:orange', 'tab:green',
              'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(yval, mean, xerr=errors, capsize=6, label=yval, color=colors)
    plt.yticks(yval)
    plt.ylabel("Number of sending Tx")
    plt.xlabel(xlabel)
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_grouped_nruns_multi(df1, df2, argument, templates, file_name, xlabel):
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
    if argument == "num_dec":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('mean').values.tolist()
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('min').values.tolist()
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('max').values.tolist()
    if argument == "num_per":
        mean = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_per.agg('mean').values.tolist()
        minval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_per.agg('min').values.tolist()
        maxval = df1[df1['template'].isin(templates)].groupby(
            ['template']).num_per.agg('max').values.tolist()
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
    for i in range(1, len(mean)+1):
        yval.append(i)
        ylabels = yval

    # colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(yval, mean, bar_width, xerr=errors,
             capsize=6, label="mean=200[ms]")

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
    if argument == "num_dec":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('mean').values.tolist()
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('min').values.tolist()
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_dec.agg('max').values.tolist()
    if argument == "num_dec":
        mean = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_per.agg('mean').values.tolist()
        minval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_per.agg('min').values.tolist()
        maxval = df2[df2['template'].isin(templates)].groupby(
            ['template']).num_per.agg('max').values.tolist()
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
    for i in range(1, len(mean)+1):
        yval.append(i+bar_width)
        yticks.append(i+bar_width/2)

    # colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(yval, mean, bar_width, xerr=errors,
             capsize=6, label="mean=1000[ms]")

    plt.yticks(yticks, labels=ylabels)
    plt.ylabel("Number of sending Tx")
    plt.xlabel(xlabel)
    plt.legend()
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def main():
    """Main function
    """
    # print("Welcome to the plotter..")
    # mk_dir()
    # print("Going to plot all single values")
    templates = ["lora_sim_chain"]
    file_name = "../results/profiled_single_low_mean.csv"
    df_single = pd.read_csv(file_name)
    # plot_single(df_single, "sf", templates, "s_time_low", "Execution time [s]")
    # plot_single(df_single, "s_num_right_low", templates, "sf_num_right",
    #             "Number of correctly decoded messages")
    # plot_single(df_single, "num_dec", templates,
    #             "s_num_dec_low", "Number of decoded messages")
    # #high mean values
    # file_name = "../results/profiled_single_high_mean.csv"
    # df_single = pd.read_csv(file_name)
    # plot_single(df_single, "sf", templates, "s_time_high", "Execution time [s]")
    # plot_single(df_single, "s_num_right_high", templates, "sf_num_right",
    #             "Number of correctly decoded messages")
    # plot_single(df_single, "num_dec", templates,
    #             "s_num_dec_high", "Number of decoded messages")
    #
    # #dynamic results
    # file_name = "../results/profiled_single_dyn.csv"
    # df_single_dyn = pd.read_csv(file_name)
    # plot_single(df_single_dyn, "mean_num", "lora_sim_multi1",
    #             "s_mean_num", "Total number of correctly decoded messages")
    # plot_single(df_single_dyn, "frame_period_num", "lora_sim_multi1",
    #             "s_frame_period_num", "Total number of correctly decoded messages")
    # plot_single(df_single_dyn, "cr_num", "lora_sim_multi1",
    #             "s_cr_num", "Total number of correctly decoded messages")
    # plot_single(df_single_dyn, "has_crc_num", "lora_sim_multi1",
    #             "s_has_crc_num", "Total number of correctly decoded messages")
    # plot_single(df_single_dyn, "mean_time", "lora_sim_multi1",
    #             "s_mean_time", "Execution time [s]")
    # plot_single(df_single_dyn, "frame_period_time", "lora_sim_multi1",
    #             "s_frame_period_time", "Execution time [s]")
    # plot_single(df_single_dyn, "cr_time", "lora_sim_multi1",
    #             "s_cr_time", "Execution time [s]")
    # plot_single(df_single_dyn, "has_crc_time", "lora_sim_multi1",
    #             "s_has_crc_time", "Execution time [s]")
    #
    # #low values
    file_name = "../results/profiled_single_runs_low_mean.csv"
    df_single_low_n = pd.read_csv(file_name)
    # plot_single_nruns(df_single_low_n, "sf", templates,
    #                   "nsruns_time_low", "Execution time [s]")
    # plot_single_nruns(df_single_low_n, "num_right", templates,
    #                   "nsruns_nright_low", "Number of correctly decoded messages")
    # plot_single_nruns(df_single_low_n, "num_dec", templates,
    #                   "nsruns_ndec_low", "Number of decoded messages")
    #
    # #high values
    file_name = "../results/profiled_single_runs_mean_high.csv"
    df_single_high_n = pd.read_csv(file_name)
    # plot_single_nruns(df_single_high_n, "sf", templates,
    #                   "nsruns_time_high", "Execution time [s]")
    # plot_single_nruns(df_single_high_n, "num_right", templates,
    #                   "nsruns_nright_high", "Number of correctly decoded messages")
    # plot_single_nruns(df_single_high_n, "num_dec", templates,
    #                   "nsruns_ndec_high", "Number of decoded messages")

    plot_grouped_single(df_single_low_n, df_single_high_n, "sf", templates,
                        "nsruns_time_grouped", "Execution time [s]")
    plot_grouped_single(df_single_low_n, df_single_high_n, "num_right", templates,
                        "nsruns_nright_grouped", "Number of correctly decoded messages")
    plot_grouped_single(df_single_low_n, df_single_high_n, "num_dec", templates,
                        "nsruns_ndec_grouped", "Number of decoded messages")

    #
    templates = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3",
                 "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    #
    # # print("Going to plot all single values")
    # file_name = "../results/profiled_multi_low_mean.csv"
    # df_multi = pd.read_csv(file_name)
    # plot_multi(df_multi, "sf", templates,
    #            "m_time_low", "Execution time [s]")
    # plot_multi(df_multi, "num_right", templates,
    #            "m_num_right_low", "Number of rightly decoded messages")
    # plot_multi(df_multi, "num_dec", templates,
    #            "m_num_dec_low", "Number of decoded messages")
    #
    # file_name = "../results/profiled_multi_high_mean.csv"
    # df_multi = pd.read_csv(file_name)
    # plot_multi(df_multi, "sf", templates,
    #            "m_time_high", "Execution time [s]")
    # plot_multi(df_multi, "num_right", templates,
    #            "m_num_right_high", "Number of rightly decoded messages")
    # plot_multi(df_multi, "num_dec", templates,
    #            "m_num_dec_high", "Number of decoded messages")

    file_name = "../results/profiled_multi_runs_low_mean.csv"
    df_multi_n_low = pd.read_csv(file_name)
    # plot_multi_nruns(df_multi_n_low, "sf", templates,
    #            "nmruns_time_low", "Execution time [s]")
    # plot_multi_nruns(df_multi_n_low, "num_right", templates,
    #            "nmruns_num_right_low", "Number of correctly decoded messages")
    # plot_multi_nruns(df_multi_n_low, "num_dec", templates,
    #            "nmruns_num_dec_low", "Number of decoded messages")
    # plot_multi_nruns(df_multi_n_low, "load", templates,
    #            "nmruns_load_low", "Average 1-min load")

    file_name = "../results/profiled_multi_runs_mean_high.csv"
    df_multi_n_high = pd.read_csv(file_name)
    # plot_multi_nruns(df_multi_n_high, "sf", templates,
    #            "nmruns_time_high", "Execution time [s]")
    # plot_multi_nruns(df_multi_n_high, "num_right", templates,
    #            "nmruns_num_right_high", "Number of correctly decoded messages")
    # plot_multi_nruns(df_multi_n_high, "num_dec", templates,
    #            "nmruns_num_dec_high", "Number of decoded messages")
    # plot_multi_nruns(df_multi_n_high, "load", templates,
    #            "nmruns_load_high", "Average 1-min load")

    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "sf", templates,
                             "nmruns_time_grouped", "Execution time [s]")
    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "num_right", templates,
                             "nmruns_num_right_grouped", "Number of correctly decoded messages")
    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "num_dec", templates,
                             "nmruns_num_dec_grouped", "Number of decoded messages")
    plot_grouped_nruns_multi(df_multi_n_low, df_multi_n_high, "load", templates,
                             "nmruns_load_grouped",  "Average 1-min load")


main()
