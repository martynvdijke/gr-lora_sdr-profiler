import subprocess
import re
import time as td


def profile(string_input):
    """Runs the scalene profiler with output

    Returns:
        string : returns stdout from scalene run
    """
    start_time = td.time()
    process = subprocess.Popen('python temp/flowgraph.py',
                               shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    stdout = process.stdout.readlines()
    time = (td.time() - start_time)
    return parser_stdout(stdout, string_input, time)


def parser_stdout(stdout, string_input, time):
    """[summary]

    Args:
        stdout ([lines]): output of stdout
        string_input ([string]): string to match against

    Returns:
        [int]: number of rightlyfull decoded messages
    """
    num_right = 0
    for out in stdout:
        line = str(out)
        re_text = 'Decode msg is:' + str(string_input)
        out = re.search(re_text, line)
        # check if the search found match objects
        if out is not None:
            num_right = num_right + 1
    return num_right, time


def parser_scalene():
    """[summary]

    Returns:
        [int,int]: memory usage, time usage
    """

    # regular expressions to match agains output of scalene
    re_mb_line = '\d+\.\d+MB'
    re_time = '\d+\.\d+s'
    re_val = '\d+\.\d+'
    f = open('temp/scalene_output', 'r')
    line = f.readline()
    mem_line = re.search(re_mb_line, line).group()
    mem = re.search(re_val, mem_line).group()
    line = f.readline()
    time_line = re.search(re_time, line).group()
    time = re.search(re_val, time_line).group()
    return mem, time
