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
    if argument == "num_right":
        df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_right.max().unstack().plot.barh()
    if argument == "num_dec":
        df[df['template'].isin(templates)].groupby(
            ['template', 'sf']).num_dec.max().unstack().plot.barh()

    plt.yticks(ticks=np.arange(2), labels=("blocks", "chain"))
    # ax = plt.axes()
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
    #           ncol=3, fancybox=True, shadow=True)
    plt.ylabel("Implementation")
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
    file_name = "time_n_runs"
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

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    yval = np.arange(len(mean))
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(yval, mean, xerr=errors, capsize=6, label=yval, color=colors)
    plt.yticks(yval)
    plt.ylabel("Number of sending Tx")
    plt.xlabel(xlabel)
    file_name = "nright_multi_n_runs"
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
    df_single = pd.read_csv(file_name)
    plot_single(df_single, "sf", templates, "sf_time", "Execution time [s]")
    plot_single(df_single, "num_right", templates, "sf_num_right",
                "Number of rightfully decoded messages")
    plot_single(df_single, "num_dec", templates,
                "sf_num_dec", "Number of decoded messages")

    file_name = "../results/profiled_single_runs.csv"
    df_single_n = pd.read_csv(file_name)
    plot_single_nruns(df_single_n, "sf", templates,
                      "time_n_runs", "Execution time [s]")
    plot_single_nruns(df_single_n, "num_right", templates,
                      "time_n_right", "Number of rightfully decoded messages")
    plot_single_nruns(df_single_n, "num_dec", templates,
                      "time_n_dec", "Number of decoded messages")

    templates = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3",
                 "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]

    # print("Going to plot all single values")
    file_name = "../results/profiled_multi.csv"
    df_multi = pd.read_csv(file_name)
    plot_multi(df_multi, "sf", templates,
               "sf_time_multi", "Execution time [s]")
    plot_multi(df_multi, "num_right", templates,
               "sf_num_right_multi", "Number of rightly decoded messages")
    plot_multi(df_multi, "num_dec", templates,
               "sf_num_dec_multi", "Number of decoded messages]")

    file_name = "../results/profiled_multi_runs.csv"
    df_multi_n = pd.read_csv(file_name)
    plot_multi_nruns(df_multi_n, "sf", templates,
               "sf_time_multi", "Execution time [s]")
    plot_multi_nruns(df_multi_n, "num_right", templates,
               "sf_num_right_multi", "Number of rightly decoded messages")
    plot_multi_nruns(df_multi_n, "num_dec", templates,
               "sf_num_dec_multi", "Number of decoded messages]")

main()
