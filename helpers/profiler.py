import subprocess
import re


def profile(string_input):
    """Runs the scalene profiler with output

    Returns:
        string : returns stdout from scalene run
    """
    process = subprocess.Popen('python -m scalene --outfile temp/scalene_output temp/flowgraph.py',
                               shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    stdout = process.stdout.readlines()
    return parser_stdout(stdout, string_input)


def parser_stdout(stdout, string_input):
    """[summary]

    Args:
        stdout ([type]): [description]
        string_input ([type]): [description]

    Returns:
        [type]: [description]
    """
    num_right = 0
    for out in stdout:
        line = str(out)
        re_text = 'Decode msg is:' + str(string_input)
        out = re.search(re_text, line)
        # check if the search found match objects
        if out is not None:
            num_right = num_right + 1
    return num_right

def parser_scalene():

    re_mb = '\d+\.\d+MB'
    re_time = '\d+\.\d+s'
    f = open('temp/scalene_output','r')
    line = f.readline()
    mem = re.search(re_mb, line).group()
    line = f.readline()
    time = re.search(re_time, line).group()

    return mem,time