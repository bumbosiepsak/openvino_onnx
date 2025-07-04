#!/usr/bin/env python3

import numpy as np
import openvino
import sys


if __name__ == '__main__':
    print('INFO: Running inference on the OpenVINO model', file=sys.stderr)

    test_data = np.load('/opt/openvino_onnx/build/test_data.npz')

    core = openvino.Core()

    model = core.read_model('/opt/openvino_onnx/build/sample_model.xml')
    compiled_model = core.compile_model(model, device_name='CPU')

    input_ports = compiled_model.inputs
    x_name = input_ports[0].get_any_name()
    y_name = input_ports[1].get_any_name()

    infer_request = compiled_model.create_infer_request()

    infer_request.set_tensor(x_name, openvino.Tensor(test_data['x']))
    infer_request.set_tensor(y_name, openvino.Tensor(test_data['y']))

    infer_request.infer()

    outputs = [infer_request.get_tensor(output) for output in compiled_model.outputs]
    output_data = [output.data for output in outputs]

    np.save('/opt/openvino_onnx/build/inference_result_openvino.npy', output_data)

    print('INFO: Done running inference on the OpenVINO model', file=sys.stderr)
