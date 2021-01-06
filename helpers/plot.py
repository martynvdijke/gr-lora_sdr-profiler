import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_sf(df):
    template_sf = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1"]
    df[df['template'].isin(template_sf)].groupby(['template', 'sf']).time.max().unstack().plot.barh()
    plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Execution time [s]")
    plt.savefig('figures/sf_time.eps', format='eps')
    plt.show()
    plt.close()


def plot_mem(df):
    template_sf = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1"]
    df[df['template'].isin(template_sf)].groupby(['template', 'sf']).mem.max().unstack().plot.barh()
    plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Used memory [Mb]")
    plt.savefig('figures/sf_mem.eps', format='eps')
    plt.show()
    plt.close()


def plot_num_right(df):
    template_sf = ["lora_sim_blocks", "lora_sim_chain", "lora_sim_multi1"]
    df[df['template'].isin(template_sf)].groupby(['template', 'sf']).num_right.max().unstack().plot.barh()
    plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Number of rightly decoded messages")
    plt.savefig('figures/sf_num_right.eps', format='eps')
    plt.show()
    plt.close()

def plot_multi_time(df):
    template_sf = ["lora_sim_multi2","lora_sim_multi3","lora_sim_multi4","lora_sim_multi5","lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(['template', 'sf']).time.max().unstack().plot.barh()
    # plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Execution time [s]")
    plt.savefig('figures/sf_time_multi.eps', format='eps')
    plt.show()
    plt.close()

def plot_multi_mem(df):
    template_sf = ["lora_sim_multi2","lora_sim_multi3","lora_sim_multi4","lora_sim_multi5","lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(['template', 'sf']).mem.max().unstack().plot.barh()
    # plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Used memory [Mb]")
    plt.savefig('figures/sf_mem_multi.eps', format='eps')
    plt.show()
    plt.close()

def plot_multi_num_right(df):
    template_sf = ["lora_sim_multi2","lora_sim_multi3","lora_sim_multi4","lora_sim_multi5","lora_sim_multi6"]
    df[df['template'].isin(template_sf)].groupby(['template', 'sf']).num_right.max().unstack().plot.barh()
    # plt.yticks(ticks=np.arange(3), labels=("blocks", "chain", "multi"))
    plt.ylabel("Implementation")
    plt.xlabel("Number of rightly decoded messages")
    plt.savefig('figures/sf_num_right_multi.eps', format='eps')
    plt.show()
    plt.close()


def main():
    file_name = "../profiled_test.csv"
    df = pd.read_csv(file_name)
    
    plot_sf(df)
    plot_mem(df)
    plot_num_right(df)
    plot_multi_time(df)
    plot_multi_mem(df)
    plot_multi_num_right(df)


main()
