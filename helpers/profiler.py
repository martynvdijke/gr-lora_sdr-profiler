import subprocess
import re
import time as td
import datetime


# def load_avg():
#     process = subprocess.Popen("cat /proc/loadavg | awk '{ print $1 }'",
#                                shell=True, stdout=subprocess.PIPE)
#     out, err = process.communicate()
#     print(str(out))

# # stdout = process.stdout.readlines()
# re_load = '\d+\.\d+'
# for line in out:
#     load = re.search(re_load, str(line)).group()
#     print(load)
# print(stdout)


def profile(string_input):
    """Runs the scalene profiler with output

    Returns:
        string : returns stdout from scalene run
    """
    now = datetime.datetime.now()
    print("New run:")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    start_time = td.time()
    process = subprocess.Popen('./helpers/run.sh',
                               shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    process.communicate()
    process_read = subprocess.call('cat temp/out.txt',
                                    shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
    try:
        process_read.communicate()
    except:
        print("test")
    process.terminate()

    # process_read.terminate()
    
    # print("Waited for execution, now catting the file")

    # stdout = process_read.stdout.readlines()
    file1 = open('temp/out2.txt', 'r') 
    try:
        stdout = file1.readlines() 
    except:
        print("except in reading")
    time = (td.time() - start_time)
    # process = subprocess.Popen('rm temp/out.txt',
    #                            shell=True, stdout=subprocess.PIPE,
    #                            stderr=subprocess.STDOUT)
    # process.terminate()
    return parser_stdout(stdout, string_input, time)


def parser_stdout(stdout, string_input, time):
    """[summary]

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
    print(string_input)
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

# deprecated


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

# load_avg()

# profile("PKdhtXMmr18n2L9K88eMlGn7CcctT9RwKSB1FebW397VI5uG1yhc3uavuaOb9vyJ")