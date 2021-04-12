import argparse
import logging
import sys
from profiler import  __version__

__author__ = "Martyn van Dijke"
__copyright__ = "Martyn van Dijke"
__license__ = "MIT"
_logger = logging.getLogger(__name__)
__templates__ = (
"lora_sim_blocks", "lora_sim_chains", "lora_sim_multi1", "lora_sim_multi2", "lora_sim_multi3", "lora_sim_multi4",
"lora_sim_multi5", "lora_sim_multi6")


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
    parser.add_argument("-t", "--template", default="lora_sim_chains",
                        choices=__templates__,
                        help="Specify the template to use [default=%(default)r]")
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
    _logger.info("Starting profiler with template: {}".format(args.template))


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html
    main(sys.argv[1:])
