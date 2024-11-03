#!/usr/bin/env -S python3 -u

import sys
import os
import requests

if __name__ == "__main__" :
    # Rename these variables to something meaningful
    input1 = sys.argv[1]
    input2 = sys.argv[2]


    # Fake example outputs
    output1 = "Hello"
    output2 = "World"

    # This is how you produce workflow outputs.
    # Make sure corresponds to output variable names in action.yml
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f :
            print("{0}={1}".format("output-one", output1), file=f)
            print("{0}={1}".format("output-two", output2), file=f)
