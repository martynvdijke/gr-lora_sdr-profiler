import subprocess
import re
import time as td
import datetime
import os

def profile_flowgraph(string_input, timeout, template, _logger):
    """
    Runs the actual flowgraph
    Args:
        string_input: string input to verify against
        timeout : maximum number of seconds to let the flowgraph run
        _logger : logger from the main file

    Returns: the number of decoded messages

    """
    _logger.debug("Starting new flowgraph run")
    # set starttime
    start_time = td.time()
    # call bash script to exectue flowgraph
    subprocess.call('profiler/bash_scripts/run.sh {}'.format(timeout), shell=True)
    time = (td.time() - start_time)
    # open output for parsing processing
    file1 = open('temp/out.txt', 'r')
    try:
        stdout = file1.readlines()
    except:
        _logger.debug("Error reading the output of the run")
        stdout = "nothing"

    return parse_stdout(stdout, string_input, time, template, _logger)


def parse_stdout(stdout, string_input, time, template, _logger):
    """
    Parses the stdout file of the flowgraph runner to find the number of decoded and rightfully decoded messages

    Args:
        stdout ([lines]): output of stdout
        string_input ([string]): string to match against
        time (int): execeution time
        template (string) : template file to use

    Returns:
        [int]: number of rightlyfull decoded messages
    """
    # Number of rightlyfully decoded messages
    num_right = 0
    # Number of decoded messages
    num_dec = 0

    snr = []
    # for each line in stdout find the number of rightfull and decoded messages
    for out in stdout:
        try:
            line = str(out)
            re_text_right = 'msg :' + str(string_input)
            out_right = re.search(re_text_right, line)
            re_text_dec = 'msg :'
            out_dec = re.search(re_text_dec, line)
            if template == "frame_detector":
                re_text_snr = 'snr: '
                out_snr = re.search(re_text_snr, line)
                if out_snr is not None:
                    snr.append(float(re.findall("\d+\.\d+",line)[0]))
            # check if the search found match objects
            if out_right is not None:
                num_right = num_right + 1
            if out_dec is not None:
                num_dec = num_dec + 1
        except:
            _logger.debug("Error in parsing the flowgraph output")


    if template == "frame_detector":
        avg_snr = sum(snr)/len(snr)
        return num_right, num_dec, time, avg_snr
    else:
        return num_right, num_dec, time
