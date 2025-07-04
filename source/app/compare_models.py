#!/usr/bin/env python3

import numpy as np
import pathlib
import sys


if __name__ == '__main__':
    print('INFO: Comparing models')

    different_indices = pathlib.Path('/opt/openvino_onnx/build/different_indices.txt')
    different_onnx = pathlib.Path('/opt/openvino_onnx/build/different_onnx.txt')
    different_openvino = pathlib.Path('/opt/openvino_onnx/build/different_openvino.txt')

    different_indices.unlink(missing_ok=True)
    different_onnx.unlink(missing_ok=True)
    different_openvino.unlink(missing_ok=True)

    output_data_onnx = np.load('/opt/openvino_onnx/build/inference_result_onnx.npy')
    output_data_openvino = np.load('/opt/openvino_onnx/build/inference_result_openvino.npy')

    if not np.allclose(output_data_onnx, output_data_openvino):
        different_indices.write_text(str(np.where(output_data_onnx != output_data_openvino)))
        different_onnx.write_text(str(output_data_onnx[different_indices]))
        different_openvino.write_text(str(output_data_openvino[different_indices]))

    print('INFO: Done comparing models')
