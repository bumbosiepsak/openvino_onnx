#!/usr/bin/env python3

import openvino
import sys


if __name__ == '__main__':
    print('INFO: Converting models from ONNX to OpenVINO', file=sys.stderr)

    openvino_model = openvino.convert_model('/opt/openvino_onnx/build/sample_model.onnx')

    openvino.save_model(openvino_model, '/opt/openvino_onnx/build/sample_model.xml')

    print('INFO: Done converting models from ONNX to OpenVINO', file=sys.stderr)
