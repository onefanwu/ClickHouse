#!/usr/bin/python3

import sys
import json
import random

def main():
    fd = open("/tmp/debug.log", "w")

    try:
        # Read a batch of input records
        for number in sys.stdin:
            rows = int(number)

            texts = []
            for row in range(0, rows):
                texts.append(sys.stdin.readline())

            # Write the output
            for vector in texts:
                print(json.dumps([random.random() for _ in range(384)]))

            sys.stdout.flush()

    except Exception as e:
        traceback.print_exc(file=fd)
        fd.close()

if __name__ == "__main__":
    main()