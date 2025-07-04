# syntax=docker/dockerfile:1.7.0

ARG DOCKER_REGISTRY
ARG VERSION_TAG
FROM ${DOCKER_REGISTRY}/base-linux_x86_64:${VERSION_TAG}

LABEL com.opera.schema-version="1.0"
LABEL com.opera.platform="linux"
LABEL com.opera.system="x86_64"

LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.description="A Docker image for the 'ONNX to OpenVINO conversion'"
LABEL org.label-schema.vendor="Intel"

# ---------------------------------------------------------------------------

ENV OPENVINO_ONNX_DIRECTORY=/opt/openvino_onnx

COPY "source/containers/images/openvino_onnx/${PLATFORM_AND_SYSTEM}/variants" "${OPENVINO_ONNX_DIRECTORY}/variants"

ARG PYPI_REPOSITORY=pypi.org/simple

RUN --mount=type=cache,sharing=locked,mode=0755,uid=0,gid=0,id=pip3_cache,target=/tmp/pip3/cache \
    <<EOF
    echo >&2 "Python virtual environments"

    mkdir --parents "${OPENVINO_ONNX_DIRECTORY}/venv"

    assert_is_pip3_cache_accessible.sh /tmp/pip3/cache

    find "${OPENVINO_ONNX_DIRECTORY}/variants" -mindepth 1 -maxdepth 1 -type d | while IFS= read -r variant_directory; do

        runtime_variant="$(basename "${variant_directory}")"

        python3 -m venv "${OPENVINO_ONNX_DIRECTORY}/venv/${runtime_variant}"

        source "${OPENVINO_ONNX_DIRECTORY}/venv/${runtime_variant}/bin/activate"

        pip3 install --upgrade \
            pip \
            setuptools \
            wheel
    done
EOF

ENV PLAYWRIGHT_BROWSERS_PATH=/opt/playwright

RUN --mount=type=cache,sharing=locked,mode=0755,uid=0,gid=0,id=pip3_cache,target=/tmp/pip3/cache \
    <<EOF
    echo >&2 "Hardware dependencies of runtime variants"

    assert_is_pip3_cache_accessible.sh /tmp/pip3/cache

    find "${OPENVINO_ONNX_DIRECTORY}/variants" -mindepth 1 -maxdepth 1 -type d | while IFS= read -r variant_directory; do

        runtime_variant="$(basename "${variant_directory}")"
        source "${OPENVINO_ONNX_DIRECTORY}/venv/${runtime_variant}/bin/activate"

        pip3 install \
            --cache-dir /tmp/pip3/cache \
            --extra-index-url "$(cat "${variant_directory}/pip3_index.txt")" \
            --index-url "https://$PYPI_REPOSITORY" \
            --requirement "${variant_directory}/requirements.txt"
    done
EOF

RUN --mount=type=cache,sharing=locked,mode=0755,uid=0,gid=0,id=pip3_cache,target=/tmp/pip3/cache \
    --mount=type=cache,sharing=locked,mode=0755,uid=0,gid=0,id=var_cache_apt,target=/var/cache/apt \
    --mount=type=cache,sharing=locked,mode=0755,uid=0,gid=0,id=var_lib_apt,target=/var/lib/apt \
    <<EOF
    echo >&2 "Playwright dependencies"

    find "${OPENVINO_ONNX_DIRECTORY}/variants" -mindepth 1 -maxdepth 1 -type d | while IFS= read -r variant_directory; do

        runtime_variant="$(basename "${variant_directory}")"
        source "${OPENVINO_ONNX_DIRECTORY}/venv/${runtime_variant}/bin/activate"

        playwright install --with-deps \
            chromium
    done
EOF

COPY --chmod=755 "source/containers/images/openvino_onnx/${PLATFORM_AND_SYSTEM}/run_command.bat" "/run_command.bat"

COPY --chmod=755 "source/app" "${OPENVINO_ONNX_DIRECTORY}/app"

USER ${USER_NAME}

WORKDIR "${OPENVINO_ONNX_DIRECTORY}/app"
