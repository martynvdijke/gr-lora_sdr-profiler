"""Plotter script
    Using this script all values loaded from a csv pandas dataframe can be plotted
"""
import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from . import get_config


_logger = logging.getLogger(__name__)
__plot_options__ = WordCompleter(["line", "bar", "barh"])
__aggregate_options__ = ["min", "max", "mean", "sum", "count", "all"]

mpl_logger = logging.getLogger("matplotlib")
mpl_logger.setLevel(logging.WARNING)
# pylint: disable=R0902


class Plotter:
    """
    Class to do all the plotting
    """

    def __init__(self, args):
        """
        Initializes the plotter class
        Args:
            args: sys arguments given to script
        """
        self.logger = _logger
        self.figsize = (7, 4)
        self.template = args.mode
        self.output_dir = "figures"
        self.output_eps = self.output_dir + "/eps"
        self.output_png = self.output_dir + "/png"
        self.output = True
        self.show = True
        self.barwidth = 0.9
        self.data_frame = pd.read_csv(args.plot)
        self.colum_names = get_config.parse_config_colums(self.template)
        self.make_dirs()

    def make_dirs(self):
        """
        Makes the output directories
        Returns:

        """
        try:
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
            if not os.path.exists(self.output_eps):
                os.makedirs(self.output_eps)
            if not os.path.exists(self.output_png):
                os.makedirs(self.output_png)
        except RuntimeError:
            _logger.error("Something went wrong making dirs")

    def line_plot(self):
        """
        Lets user choose from the values in the data frame and makes a line plot
        based on those values x vs y values
        Returns:

        """
        _logger.debug("Making line plot")
        plot_x = prompt("Y value to choose ", completer=WordCompleter(self.colum_names)).strip()
        plot_y = prompt("X value to choose ", completer=WordCompleter(self.colum_names)).strip()
        plot_z = prompt("Value to groupby", completer=WordCompleter(self.colum_names)).strip()
        agg = prompt("Aggregate by", completer=(WordCompleter(__aggregate_options__))).strip()
        # get labels for names
        labels = get_config.get_label(plot_x, plot_y, plot_z)

        axes = self.data_frame.groupby([plot_x, plot_z])[plot_y].agg(agg).unstack().plot.line()
        axes.legend(bbox_to_anchor=(1.04, 1), title=labels[2])
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        # check if we want to plot all aggegrate options
        agg_list = []
        if agg == "all":
            temp = __aggregate_options__.copy()
            agg_list = temp[:-1]
        else:
            agg_list = [agg]
        for agg in agg_list:
            if self.output:
                self.logger.debug("Writing plot to file")
                filename = "/line_{0}_{1}_{2}_{3}".format(plot_x, plot_y, plot_z, agg)
                plt.savefig(self.output_eps + filename + ".eps", format="eps")
                plt.savefig(self.output_png + filename + ".png")
            if self.show:
                plt.show()
            self.logger.debug("Line plotted %s vs %s", plot_x, plot_y)

    def bar_plot(self):
        """
        Lets user choose from the values in the data frame and makes a bar plot
        based on those values x vs y values
        Returns: none

        """
        _logger.debug("Making bar plot")
        plot_x = prompt("X value to choose ", completer=WordCompleter(self.colum_names)).strip()
        plot_y = prompt("Y value to choose ", completer=WordCompleter(self.colum_names)).strip()
        plot_z = prompt("Value to groupby", completer=WordCompleter(self.colum_names)).strip()
        agg = prompt("Aggregate by", completer=(WordCompleter(__aggregate_options__))).strip()
        labels = get_config.get_label(plot_x, plot_y, plot_z)
        axes = self.data_frame.groupby([plot_x, plot_z])[plot_y].agg(agg).unstack().plot.bar()
        axes.legend(bbox_to_anchor=(1.04, 1), title=labels[2])
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        # check if we want to plot all aggegrate options
        agg_list = []
        if agg == "all":
            temp = __aggregate_options__.copy()
            agg_list = temp[:-1]
        else:
            agg_list = [agg]
        for agg in agg_list:
            # start the plotting
            if self.output:
                self.logger.debug("Writing plot to file")
                filename = "/bar_{0}_{1}_{2}_{3}".format(plot_x, plot_y, plot_z, agg)
                plt.savefig(self.output_eps + filename + ".eps", format="eps", bbox_inches="tight")
                plt.savefig(self.output_png + filename + ".png", bbox_inches="tight")
            if self.show:
                plt.show()
            self.logger.debug("Bar plotted %s vs %s vs %s using %s", plot_x, plot_y, plot_z, agg)

    def barh_plot(self):
        """
        Lets user choose from the values in the data frame and makes a barh plot
        based on those values x vs y values
        Returns: none

        """
        _logger.debug("Making bar plot")
        plot_x = prompt("X value to choose ", completer=WordCompleter(self.colum_names)).strip()
        plot_y = prompt("Y value to choose ", completer=WordCompleter(self.colum_names)).strip()
        plot_z = prompt("Value to groupby", completer=WordCompleter(self.colum_names)).strip()
        agg = prompt("Aggregate by", completer=WordCompleter((__aggregate_options__))).strip()
        labels = get_config.get_label(plot_x, plot_y, plot_z)
        # check if we want to plot aLL aggegrate options
        agg_list = []
        if agg == "all":
            temp = __aggregate_options__.copy()
            agg_list = temp[:-1]
        else:
            agg_list = [agg]
        # start the plotting
        for agg in agg_list:
            axes = (
                self.data_frame.groupby([plot_y, plot_z])[plot_x]
                .agg(agg)
                .unstack()
                .plot.barh(width=self.barwidth)
            )
            plt.xlabel(labels[0])
            plt.ylabel(labels[1])
            axes.legend(bbox_to_anchor=(1.04, 1), title=labels[2])
            if self.output:
                self.logger.debug("Writing plot to file")
                filename = "/barh_{0}_{1}_{2}_{3}".format(plot_x, plot_y, plot_z, agg)
                plt.savefig(self.output_eps + filename + ".eps", format="eps", bbox_inches="tight")
                plt.savefig(self.output_png + filename + ".png", bbox_inches="tight")
            if self.show:
                plt.show()
                plt.close()
            self.logger.debug("Barh plotted %s vs %s vs %s using %s", plot_x, plot_y, plot_z, agg)

    def main(self):
        """
        Main function for the plotter handling the dispatching of the separate plot functions
        Returns: none

        """
        run = True
        while run:
            plot_type = prompt("What plot you want to make ", completer=__plot_options__)
            if plot_type.strip() == "line":
                self.line_plot()
            if plot_type.strip() == "bar":
                self.bar_plot()
            if plot_type.strip() == "barh":
                self.barh_plot()

            exit_plotter = prompt("Do you want to quit ?[N/y]", default="N")
            if exit_plotter == "y":
                run = False
        _logger.info("Received quit signal, stopping plotting")
