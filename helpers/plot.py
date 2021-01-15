import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def plot_sf(df):
    template_sf = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).time.max().unstack().plot.barh()
    plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Execution time [s]")
    file_name = "sf_time"
    plt.savefig('figures/eps/'+file_name+'.eps', format='eps')
    plt.savefig('figures/png/'+file_name+'.png')
    plt.show()
    plt.close()


def plot_mem(df):
    template_sf = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).mem.max().unstack().plot.barh()
    plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Used memory [Mb]")
    file_name = "sf_mem"
    plt.savefig('figures/eps/'+file_name+'.eps', format='eps')
    plt.savefig('figures/png/'+file_name+'.png')
    plt.show()
    plt.close()


def plot_num_right(df):
    template_sf = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).num_right.max().unstack().plot.barh()
    plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Number of rightly decoded messages")
    file_name = "sf_num_right"
    plt.savefig('figures/eps/'+file_name+'.eps', format='eps')
    plt.savefig('figures/png/'+file_name+'.png')
    plt.show()
    plt.close()


def plot_multi_time(df):
    template_sf = ["lora_sim_multi2", "lora_sim_multi3",
                   "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).time.max().unstack().plot.barh()
    # plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Execution time [s]")
    file_name = "sf_time_multi"
    plt.savefig('figures/eps/'+file_name+'.eps', format='eps')
    plt.savefig('figures/png/'+file_name+'.png')
    plt.show()
    plt.close()


def plot_multi_mem(df):
    template_sf = ["lora_sim_multi2", "lora_sim_multi3",
                   "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).mem.max().unstack().plot.barh()
    # plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Used memory [Mb]")
    file_name = "sf_mem_multi"
    plt.savefig('figures/eps/'+file_name+'.eps', format='eps')
    plt.savefig('figures/png/'+file_name+'.png')
    plt.show()
    plt.close()


def plot_multi_num_right(df):
    template_sf = ["lora_sim_multi2", "lora_sim_multi3",
                   "lora_sim_multi4", "lora_sim_multi5", "lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(
        ['template', 'sf']).num_right.max().unstack().plot.barh()
    # plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Number of rightly decoded messages")
    file_name = "sf_num_right_multi"
    plt.savefig('figures/eps/'+file_name+'.eps', format='eps')
    plt.savefig('figures/png/'+file_name+'.png')
    plt.show()
    plt.close()


def mk_dir():
    print("Generting output structure")
    if not os.path.exists('figures'):
        os.makedirs('figures')
    if not os.path.exists('figures/eps'):
        os.makedirs('figures/eps')
    if not os.path.exists('figures/png'):
        os.makedirs('figures/png')


def main():
    print("Welcome to the plotter..")
    mk_dir()

    file_name = "../profiled_single.csv"
    df_single = pd.read_csv(file_name)
    print("Going to plot all single values")
    plot_sf(df_single)
    plot_num_right(df_single)

    file_name = "../profiled_multi.csv"
    df_multi = pd.read_csv(file_name)
    print("Going to plot all single values")
    plot_multi_time(df_multi)
    plot_multi_num_right(df_multi)


main()
