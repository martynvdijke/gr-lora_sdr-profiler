import subprocess
import logging

_logger = logging.getLogger(__name__)


def load_avg_1min():
    """
    Querys the Linux system with the average 1 min Linux load
    Returns: average 1 min Linux load

    """
    process = subprocess.Popen(
        "cat /proc/loadavg | awk '{ print $1; }'", shell=True, stdout=subprocess.PIPE
    )
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load


def load_avg_5min():
    """
    Querys the Linux system with the average 5 min Linux load
    Returns: average 5 min Linux load

    """
    process = subprocess.Popen(
        "cat /proc/loadavg | awk '{ print $2; }'", shell=True, stdout=subprocess.PIPE
    )
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load


def load_avg_15min():
    """
    Querys the Linux system with the average 15 min Linux load
    Returns: average 15 min Linux load

    """
    process = subprocess.Popen(
        "cat /proc/loadavg | awk '{ print $3; }'", shell=True, stdout=subprocess.PIPE
    )
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load


def load_all():
    """
    Runs the above functions to get all the loads (1,5 and 15 minutes)
    Returns:

    """
    load_1min = load_avg_1min()
    load_5min = load_avg_5min()
    load_15min = load_avg_15min()

    return load_1min, load_5min, load_15min
