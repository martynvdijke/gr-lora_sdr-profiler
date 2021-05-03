import logging
_logger = logging.getLogger(__name__)

def get_time_estimate(sf, n_times, counter):
    """
    Gets an time estimate of how long the run is going to take
    using a simple lookup table

    Args:
        sf: spreading factor that is being used
        n_times: total number of runs the script must make
        counter: current script counter

    Returns: time: current time estimate in seconds

    """
    approx_times = {
        7: 3,
        8: 3,
        9: 4,
        10: 7,
        11: 12,
        12: 18
    }

    time = approx_times[sf]*n_times - counter*approx_times[sf]

    return time



