import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def plot_time_nruns_multi(df):
    """PLot the execution time of multiple runs of sf

    Args:
        df ([type]): [description]
    """
    # set image size
    plt.rcParams["figure.figsize"] = (7, 4)
    template_sf = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3", "lora_sim_multi4", "lora_sim_multi5",
                   "lora_sim_multi6"]
    mean = df[df['template'].isin(template_sf)].groupby(
        ['template']).time.agg('mean').values.tolist()
    minval = df[df['template'].isin(template_sf)].groupby(
        ['template']).time.agg('min').values.tolist()
    maxval = df[df['template'].isin(template_sf)].groupby(
        ['template']).time.agg('max').values.tolist()

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
    sf = [1,2,3,4,5]
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(sf, mean, xerr=errors, capsize=6, label=sf, color=colors)
    plt.yticks(sf)
    plt.ylabel("Number of sending Tx")
    plt.xlabel("Execution time [s]")
    file_name = "time_multi_n_runs"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_nright_multi(df):
    """PLot the execution time of multiple runs of sf

    Args:
        df ([type]): [description]
    """
    # set image size
    plt.rcParams["figure.figsize"] = (7, 4)
    template_sf = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3", "lora_sim_multi4", "lora_sim_multi5",
                   "lora_sim_multi6"]
    mean = df[df['template'].isin(template_sf)].groupby(
        ['template']).num_right.agg('mean').values.tolist()
    minval = df[df['template'].isin(template_sf)].groupby(
        ['template']).num_right.agg('min').values.tolist()
    maxval = df[df['template'].isin(template_sf)].groupby(
        ['template']).num_right.agg('max').values.tolist()

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    # errors = maxval
    # fig, ax = plt.subplots()
    sf = [1,2,3,4,5]
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(sf, mean, xerr=errors, capsize=6, label=sf, color=colors)
    plt.yticks(sf)
    plt.ylabel("Number of sending Tx")
    plt.xlabel("Number of rightly decoded messages")
    file_name = "nright_multi_n_runs"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()

def plot_ndec_multi(df):
    """PLot the execution time of multiple runs of sf

    Args:
        df ([type]): [description]
    """
    # set image size
    plt.rcParams["figure.figsize"] = (7, 4)
    template_sf = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3", "lora_sim_multi4", "lora_sim_multi5",
                   "lora_sim_multi6"]
    mean = df[df['template'].isin(template_sf)].groupby(
        ['template']).num_dec.agg('mean').values.tolist()
    minval = df[df['template'].isin(template_sf)].groupby(
        ['template']).num_dec.agg('min').values.tolist()
    maxval = df[df['template'].isin(template_sf)].groupby(
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
    # errors = maxval
    # fig, ax = plt.subplots()
    sf = [1,2,3,4,5]
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(sf, mean, xerr=errors, capsize=6, label=sf, color=colors)
    plt.yticks(sf)
    plt.ylabel("Number of sending Tx")
    plt.xlabel("Number of \decoded messages")
    file_name = "ndec_multi_n_runs"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_time_nruns(df):
    """PLot the execution time of multiple runs of sf

    Args:
        df ([type]): [description]
    """
    # set image size
    plt.rcParams["figure.figsize"] = (7, 4)
    template_sf = ["lora_sim_chain"]
    mean = df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).time.agg('mean').unstack().values.tolist()[0]
    minval = df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).time.agg('min').unstack().values.tolist()[0]
    maxval = df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).time.agg('max').unstack().values.tolist()[0]

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
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(sf, mean, xerr=errors, capsize=6, label=sf, color=colors)
    plt.yticks(sf)
    plt.ylabel("SpreadiIng Factor")
    plt.xlabel("Execution time [s]")
    file_name = "time_n_runs"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_nright(df):
    """PLot the execution time of multiple runs of sf

    Args:
        df ([type]): [description]
    """
    # set image size
    plt.rcParams["figure.figsize"] = (7, 4)
    template_sf = ["lora_sim_chain"]
    mean = df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).num_right.agg('mean').unstack().values.tolist()[0]
    minval = df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).num_right.agg('min').unstack().values.tolist()[0]
    maxval = df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).num_right.agg('max').unstack().values.tolist()[0]

    min_err = []
    zip_object = zip(mean, minval)
    for list1_i, list2_i in zip_object:
        min_err.append(list1_i - list2_i)

    max_err = []
    zip_object = zip(maxval, mean)
    for list1_i, list2_i in zip_object:
        max_err.append(list1_i - list2_i)

    errors = [min_err, max_err]
    # errors = maxval
    # fig, ax = plt.subplots()
    sf = [7, 8, 9, 10, 11, 12]
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    plt.barh(sf, mean, xerr=errors, capsize=6, label=sf, color=colors)
    plt.yticks(sf)
    plt.ylabel("Spreading Factor")
    plt.xlabel("Number of rightly decoded messages")
    file_name = "time_n_right"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()

    # Save the figure and show
    # plt.tight_layout()


def plot_time(df):
    """[summary]
    Args:
        df ([type]): [description]
    """
    plt.rcParams["figure.figsize"] = (7, 4)
    template_sf = ["lora_sim_blocks", "lora_sim_chain"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).time.max().unstack().plot.barh()
    plt.yticks(ticks=np.arange(2), labels=("blocks", "chain"))

    # ax = plt.axes()
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
    #           ncol=3, fancybox=True, shadow=True)
    plt.ylabel("Implementation")
    plt.xlabel("Execution time [s]")
    file_name = "sf_time"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_num_right(df):
    """Plot the number of rightly decoded messages

    Args:
        df ([type]): [description]
    """
    template_sf = ["lora_sim_chain"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).num_right.max().unstack().plot.barh()
    # plt.yticks(ticks=np.arange(1), labels=("chain"))
    # plt.yticks()
    plt.yticks(visible=False)
    plt.ylabel("Implementation")
    plt.xlabel("Number of rightly decoded messages")
    file_name = "sf_num_right"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_multi_time(df):
    """Plot the excution time from the multiple tx and rx's

    Args:
        df ([type]): [description]
    """
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    template_sf = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3",
                   "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(
        ['template']).time.max().plot.barh(color=colors)
    plt.yticks(ticks=np.arange(6), labels=("1", "2", "3", "4", "5", "6"))
    plt.ylabel("Number of sending Tx")
    plt.xlabel("Execution time [s]")
    file_name = "sf_time_multi"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_multi_num_right(df):
    """Plot the number of rightly decoded messages from the multiple tx and rx's

    Args:
        df ([type]): [description]
    """
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    template_sf = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3",
                   "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(
        ['template']).num_right.max().plot.barh(color=colors)
    plt.yticks(ticks=np.arange(6), labels=("1", "2", "3", "4", "5", "6"))
    plt.ylabel("Number of sending Tx")
    plt.xlabel("Number of rightly decoded messages")
    file_name = "sf_num_right_multi"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


def plot_multi_num_dec(df):
    """Plot the number of rightly decoded messages from the multiple tx and rx's

    Args:
        df ([type]): [description]
    """
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
    template_sf = ["lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3",
                   "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(
        ['template']).num_dec.max().plot.barh(color=colors)
    plt.yticks(ticks=np.arange(6), labels=("1", "2", "3", "4", "5", "6"))
    plt.ylabel("Number of sending Tx")
    plt.xlabel("Number of decoded messages")
    file_name = "sf_num_dec_multi"
    plt.savefig('figures/eps/' + file_name + '.eps', format='eps')
    plt.savefig('figures/png/' + file_name + '.png')
    plt.show()
    plt.close()


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


def main():
    """Main function
    """
    print("Welcome to the plotter..")
    mk_dir()
    print("Going to plot all single values")

    file_name = "../results/profiled_single.csv"
    df_single = pd.read_csv(file_name)
    plot_time(df_single)
    plot_num_right(df_single)
    file_name = "../results/profiled_single_runs.csv"
    df_single_n = pd.read_csv(file_name)
    plot_time_nruns(df_single_n)
    plot_nright(df_single_n)

    print("Going to plot all single values")
    file_name = "../results/profiled_multi.csv"
    df_multi = pd.read_csv(file_name)
    plot_multi_time(df_multi)
    plot_multi_num_right(df_multi)
    plot_multi_num_dec(df_multi)

    file_name = "../results/profiled_multi_runs.csv"
    df_multi_n = pd.read_csv(file_name)
    plot_time_nruns_multi(df_multi_n)
    plot_nright_multi(df_multi_n)
    plot_ndec_multi(df_multi_n)

main()
