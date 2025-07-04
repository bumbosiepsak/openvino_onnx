#!/usr/bin/env bash

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo >&2 "ERROR: This file is supposed to be sourced!"
    exit 1
fi

OPENVINO_ONNX_RUNTIME_PARAMS=(
    --auto-devices
    --disk
    --disk-cache-dir "${OPENVINO_ONNX_DIRECTORY}/app/cache"
    --listen
    --trust-remote-code
)
