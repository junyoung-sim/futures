#!/usr/bin/env python3

# Specify these arguments in the command line to execute
#       0       1     2     3        4         5           6            7         8
# ./futures.py mode model symbol start_date end_date learning_rate, iteration, backtest

import sys
from lib import Futures

if __name__ == "__main__":
    model = Futures(sys.argv[2])
    if sys.argv[1] == "train":
        model.train(sys.argv[3], sys.argv[4], sys.argv[5], float(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]))
    elif sys.argv[1] == "run":
        model.run(sys.argv[3])
    elif sys.argv[1] == "test_trained":
        model.test_trained_data(sys.argv[3], sys.argv[4], sys.arg[5])
    else:
        print("Invalid argument was given")

