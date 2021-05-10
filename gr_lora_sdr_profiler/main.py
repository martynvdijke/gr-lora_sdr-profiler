"""
Main function that dispatches all sub functions
"""
import argparse
import logging
import sys
import os
import pathlib
from . import __version__
from . import frame_detector
from . import plotter

# pylint: disable=R0801

__author__ = "Martyn van Dijke"
__copyright__ = "Martyn van Dijke"
__license__ = "MIT"
_logger = logging.getLogger(__name__)
__templates__ = (
    "lora_sim_blocks",
    "lora_sim_chains",
    "lora_sim_multi1",
    "lora_sim_multi2",
    "lora_sim_multi3",
    "lora_sim_multi4",
    "lora_sim_multi5",
    "lora_sim_multi6",
    "lora_sim_frame_detector",
)
__modes__ = ("multi_stream", "frame_detector", "cran")


def make_dirs(_logger):
    """
    Makes necessary dirs
    Args:
        _logger: logger output

    Returns:

    """
    try:
        if not os.path.exists("temp"):
            os.makedirs("temp")
        if not os.path.exists("results"):
            os.makedirs("results")
    except RuntimeError:
        _logger.debug("Something went wrong making dirs")


def parse_args(args):
    """
    Args:
        args: cli arguments given to script

    Returns:
        list of supported arguments

    """
    parser = argparse.ArgumentParser(description="Profile gr-lora_sdr")
    parser.add_argument(
        "--version",
        action="version",
        version=f"profiler {__version__}",
    )
    # chose the template to choose from
    parser.add_argument(
        "-m",
        "--mode",
        default="frame_detector",
        choices=__modes__,
        help="Specify the mode to use [default=%(default)r]",
    )
    parser.add_argument(
        "-s",
        "--save",
        default="pandas",
        choices=("pandas", "wandb", "both"),
        help="Specify how to store the data [default=%(default)r]",
    )
    parser.add_argument(
        "-n",
        "--name",
        default="profiler-run",
        help="Specify the name to use for wandb [default=%(default)r]",
    )
    parser.add_argument(
        "-p",
        "--plot",
        metavar="FILE",
        help="Specify to plot all the values from input file  [default=%(default)r]",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="results/out.csv",
        type=pathlib.Path,
        help="Specify where to output the pandas csv file [default=%(default)r]",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        default=300,
        type=int,
        help="Maximum time a run may take [default=%(default)r]",
    )
    # set logging level
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )

    parser.add_argument("config", metavar="FILE", nargs="+", help="Input config file")
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel,
        stream=sys.stdout,
        format=logformat,
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main(args):
    """
    Main function that does all the dispatching of the subfunctions
    Args:
        args: sys arguments

    Returns:
        none
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    make_dirs(_logger)
    _logger.info("Starting gr-lora_sdr-profiler, version %s", __version__)

    if args.plot is not None:
        _logger.info("Running plotter with input file %s", args.plot)
        plot = plotter.Plotter(args)
        plot.main()
    else:
        _logger.info("Running profiler with mode: %s", args.mode)
        if args.mode == "frame_detector":
            args.filename = "lora_sim_frame_detector.py"
            frame_detector.main(args)

    _logger.info("Profiler ended")


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html
    main(sys.argv[1:])
