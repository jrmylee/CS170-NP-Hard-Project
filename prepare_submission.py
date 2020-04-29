import sys
import os
import json
import re


def validate_file(path):
    """File must not exceed 100KB and must contain only numbers and spaces"""
    if os.path.getsize(path) > 100000:
        print(f"{path} exceeds 100KB, make sure you're not repeating edges!")
        return False
    with open(path, "r") as f:
        if not re.match(r"^[\d\.\s]+$", f.read()):
            print(f"{path} contains characters that are not numbers and spaces")
            return False
    return True


if __name__ == '__main__':
    outputs_dir = sys.argv[1]
    submission_name = sys.argv[2]
    submission = {}
    for input_path in os.listdir("inputs"):
        graph_name = input_path.split('.')[0]
        output_file = f'{outputs_dir}/{graph_name}.out'
        if os.path.exists(output_file) and validate_file(output_file):
            output = open(f'{outputs_dir}/{graph_name}.out').read()
            submission[input_path] = output
    with open(submission_name, 'w') as f:
        f.write(json.dumps(submission))
