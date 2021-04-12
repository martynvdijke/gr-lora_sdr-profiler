import profiler.main
from profiler import main
import sys

def run():
    profiler.main.main(sys.argv[1:])

run()