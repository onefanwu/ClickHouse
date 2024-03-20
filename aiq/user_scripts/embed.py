#!/usr/bin/python3

import sys
import json
import torch
from sentence_transformers import SentenceTransformer

def main():
    fd = open("/tmp/debug.log", "w")
    
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    model_path = '/workdir/AiQ-dev/models/all-MiniLM-L6-v2'
    model = SentenceTransformer(model_path, device=device)

    try:
        # Read a batch of input records
        for number in sys.stdin:
            rows = int(number)

            texts = []
            for row in range(0, rows):
                texts.append(sys.stdin.readline())

            embeddings = model.encode(texts)

            # Write the output
            for vector in embeddings:
                print(json.dumps(vector.tolist()))
            
            sys.stdout.flush()

    except Exception as e:
        traceback.print_exc(file=fd)
        fd.close()

if __name__ == "__main__":
    main()