#!/usr/bin/python3

import sys
import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def main():
    for line in sys.stdin:
        vector = model.encode(line)
        print(json.dumps(vector.tolist()))

if __name__ == "__main__":
    main()