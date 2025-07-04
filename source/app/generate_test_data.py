#!/usr/bin/env python3

import numpy as np
import sys


if __name__ == '__main__':
    print('INFO: Generating test data', file=sys.stderr)

    dimensions = [1, 3]

    x = np.random.randn(*dimensions).astype(np.float32)
    y = np.random.randn(*dimensions).astype(np.float32)

    np.savez('/opt/openvino_onnx/build/test_data.npz', x=x, y=y)

    print('INFO: Done generating test data', file=sys.stderr)
