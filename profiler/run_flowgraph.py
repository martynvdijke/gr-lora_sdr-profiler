import subprocess
import re
import time as td
import datetime
import os




def profile_flowgraph(string_input, timeout, _logger):
    """
    Runs the actual flowgraph
    Args:
        string_input: string input to verify against
        timeout : maximum number of seconds to let the flowgraph run
        _logger : logger from the main file

    Returns: the number of decoded messages

    """
    _logger.debug("Starting new flowgraph run")
    # check if dirs exists otherwise make them
    make_dirs(_logger)
    #set starttime
    start_time = td.time()
    process = subprocess.Popen('./bash_scripts/run.sh',
                               shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    process.communicate()
    #read the output of the file
    process_read = subprocess.call('cat temp/out.txt',
                                   shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
    try:
        process_read.communicate()
    except:
        _logger.debug("Error reading the output of the run")
    process.terminate()
    file1 = open('temp/out2.txt', 'r')
    try:
        stdout = file1.readlines()
    except:
        _logger.debug("Error reading the output of the run")
        stdout = "except in reading"
    #set total time
    time = (td.time() - start_time)

    return parse_stdout(stdout, string_input, time)


def parse_stdout(stdout, string_input, time):
    """
    Parses the stdout file of the flowgraph runner to find the number of decoded and rightfully decoded messages

    Args:
        stdout ([lines]): output of stdout
        string_input ([string]): string to match against

    Returns:
        [int]: number of rightlyfull decoded messages
    """
    # Number of rightlyfully decoded messages
    num_right = 0
    # Number of decoded messages
    num_dec = 0
    # for each line in stdout find the number of rightfull and decoded messages
    for out in stdout:
        try:
            line = str(out)
            re_text_right = 'Decode msg is:' + str(string_input)
            out_right = re.search(re_text_right, line)
            re_text_dec = 'Decode msg is:'
            out_dec = re.search(re_text_dec, line)
            # check if the search found match objects
            if out_right is not None:
                num_right = num_right + 1
            if out_dec is not None:
                num_dec = num_dec + 1
        except:
            print("exception throw hero")
    return num_right, num_dec, time
