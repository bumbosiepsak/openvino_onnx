#!/usr/bin/env bash

set -o errexit
set -o errtrace
set -o pipefail
set -o nounset

echo >&2 "INFO: Building and running the dockerized 'openvino_onnx' scripts sequence"
echo >&2 "INFO: Once it's completed, see the 'volumes/build' folder and follow README.md advice"

export PROJECT_ROOT="$(readlink -e $(dirname "${0}"))"

export RUNTIME_VARIANT=cpu

source "${PROJECT_ROOT}/source/glue/runners.sh"

validate_provisioning

# NOTE: Performing all steps in a monolithic command for the sake of demo simplicity

build regular_service

run_command \
    --interactive \
    openvino_onnx \
        "./generate_test_data.py"

run_command \
    --interactive \
    openvino_onnx \
        "./generate_model_onnx.py"

run_command \
    --interactive \
    openvino_onnx \
        "./convert_model_onnx_openvino.py"

run_command \
    --interactive \
    openvino_onnx \
        "./generate_model_graph.py --model-name sample_model.onnx"

run_command \
    --interactive \
    openvino_onnx \
        "./generate_model_graph.py --model-name sample_model.xml"

run_command \
    --interactive \
    openvino_onnx \
        "./run_inference_onnx.py"

run_command \
    --interactive \
    openvino_onnx \
        "./run_inference_openvino.py"

run_command \
    --interactive \
    openvino_onnx \
        "./compare_models.py"


echo >&2 "INFO: Done running the 'openvino_onnx' scripts sequence"
