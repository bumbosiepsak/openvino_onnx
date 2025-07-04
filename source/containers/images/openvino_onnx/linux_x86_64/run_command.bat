#!/usr/bin/env bash

set -o errexit
set -o errtrace
set -o pipefail
set -o nounset

COMMAND="${1}"

RUNTIME_VARIANT=cpu

function exit_handler {
    exit 0
}

trap exit_handler SIGTERM SIGINT SIGQUIT SIGHUP

source "${OPENVINO_ONNX_DIRECTORY}/venv/${RUNTIME_VARIANT}/bin/activate"

bash -c "${COMMAND}"
