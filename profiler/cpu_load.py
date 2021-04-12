import subprocess

def load_avg():
    """
    Querys the Linux system with the average 1 min Linux load
    Returns: average 1 min Linux load

    """
    process = subprocess.Popen("helpers/avg_load.sh",
                               shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load
