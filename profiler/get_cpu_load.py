import subprocess

def load_avg_1min():
    """
    Querys the Linux system with the average 1 min Linux load
    Returns: average 1 min Linux load

    """
    process = subprocess.Popen("helpers/avg_load_1.sh",
                               shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load

def load_avg_5min():
    """
    Querys the Linux system with the average 5 min Linux load
    Returns: average 5 min Linux load

    """
    process = subprocess.Popen("helpers/avg_load_5.sh",
                               shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load

def load_avg_15min():
    """
    Querys the Linux system with the average 15 min Linux load
    Returns: average 15 min Linux load

    """
    process = subprocess.Popen("helpers/avg_load_15.sh",
                               shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load