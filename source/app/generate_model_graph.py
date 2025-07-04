#!/usr/bin/env python3

import argparse
import subprocess
import sys


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model-name', dest='model_name', required=True, help='Model name')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    print(f'INFO: Generating model graph for {args.model_name}', file=sys.stderr)

    command = [
        'netron_export', 
        '--output', 
        f'/opt/openvino_onnx/build/model_graphs/{args.model_name}.svg', 
        f'/opt/openvino_onnx/build/{args.model_name}'
    ]

    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    print(f'INFO: Done generating model graph for {args.model_name}', file=sys.stderr)
