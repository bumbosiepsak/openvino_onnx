#!/usr/bin/env python3

import onnxruntime
import numpy as np
import sys


if __name__ == '__main__':
    print('INFO: Running inference on the ONNX model', file=sys.stderr)

    test_data = np.load('/opt/openvino_onnx/build/test_data.npz')

    session = onnxruntime.InferenceSession('/opt/openvino_onnx/build/sample_model.onnx')

    x_name = session.get_inputs()[0].name
    y_name = session.get_inputs()[1].name

    output_data = session.run(
        output_names=None,
        input_feed={
            x_name: test_data['x'],
            y_name: test_data['y'],
        }
    )

    np.save('/opt/openvino_onnx/build/inference_result_onnx.npy', output_data)

    print('INFO: Done running inference on the ONNX model', file=sys.stderr)
