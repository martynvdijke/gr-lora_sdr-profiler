import subprocess

def load_avg():
    process = subprocess.Popen("helpers/avg_load.sh",
                               shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    load = float(out.decode("utf-8")[:-1])
    return load
