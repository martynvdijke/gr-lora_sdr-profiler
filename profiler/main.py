import argparse
import logging
import sys
import os
from profiler import  __version__
from . import frame_detector
from . import multi_stream
from . import frame_detector

__author__ = "Martyn van Dijke"
__copyright__ = "Martyn van Dijke"
__license__ = "MIT"
_logger = logging.getLogger(__name__)
__templates__ = (
"lora_sim_blocks", "lora_sim_chains", "lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3", "lora_sim_multi4",
"lora_sim_multi5", "lora_sim_multi6","lora_sim_frame_detector")
__modes__ = ("multi_stream","frame_detector","cran")



def make_dirs(_logger):
    """
    Makes nececarry dirs
    Args:
        _logger: logger output

    Returns:

    """
    try:
        os.makedirs("temp")
        os.makedirs("results")
    except:
        _logger.debug("Something went wrong making dirs")


def parse_args(args):
    """
    Args:
        args: cli arguments given to script

    Returns:
        list of supported arguments

    """
    parser = argparse.ArgumentParser(description="Profiler documentation")
    parser.add_argument(
        "--version",
        action="version",
        version=f"profiler {__version__}",
    )
    #chose the template to choose from
    parser.add_argument("-m", "--mode", default="frame_detector",
                        choices=__modes__,
                        help="Specify the mode to use [default=%(default)r]")
    #set logging level
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

    parser.add_argument("config", metavar="FILE", nargs='+',
                        help="Input config file")
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
    args = parse_args(args)
    setup_logging(args.loglevel)
    make_dirs(_logger)
    _logger.info("Starting profiler with mode: {}".format(args.mode))
    if args.mode == "multi_stream":
        multi_stream.main()
    if args.mode == "frame_detector":
        args.filename = "lora_sim_frame_detector.py"
        frame_detector.main(args,_logger)

    _logger.info("Profiler ended")

if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html
    main(sys.argv[1:])
