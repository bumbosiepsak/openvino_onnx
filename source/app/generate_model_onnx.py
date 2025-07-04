#!/usr/bin/env python3

import torch
import torch.nn
import torch.onnx
import sys


class SampleModel(torch.nn.Module):
    def __init__(self):
        super(SampleModel, self).__init__()
        self.gelu = torch.nn.GELU()

    def forward(self, x, y):
        z = (x + y) * 15
        return self.gelu(z)


if __name__ == '__main__':
    print('INFO: Generating an ONNX model', file=sys.stderr)

    dimensions = [1, 3]

    model = SampleModel()

    x = torch.randn(*dimensions)
    y = torch.randn(*dimensions)

    torch.onnx.export(
        model,
        (x, y),
        '/opt/openvino_onnx/build/sample_model.onnx',
        input_names=['x', 'y'],
        output_names=['output'],
        opset_version=17
    )

    print('INFO: Done generating an ONNX model', file=sys.stderr)
