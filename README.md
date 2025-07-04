# openvino_onnx

Performs and checks ONNX to OpenVINO model format conversion

## Task definition

1. Create a simple ONNX model any possible way. Model should have any two inputs, and contains more than 3 different layers. For example: Gelu((x + y) * 15)
2. Create a script (we prefer python) for model inference using onnxruntime
3. Create a script for loading model using OpenVINO and do the inference.
    1. Serialize OpenVINO model to *.xml
    2. Take a look on both models using Netron (you could attach images as a result)
4. Compare results of reference (onnxruntime) and OpenVINO (doesn't matter how, just to verify model is converted correctly).

As result you may provide 2 models (onnx and xml), 2 scripts for inference, screenshots of models and results comparison.

## Usage

### Provisioning

The host system needs to be prepared according to this section.

You need the following dependencies to be installed on the (host) machine:

- Docker
- Docker Compose
- Docker Buildx

If you're running an Ubuntu flavour of Linux, simply run:

``` bash
cd <project root>

./provision_linux_x86_64.sh
```

Please reference and mimic [provision_linux_x86_64.sh](provision_linux_x86_64.sh) in order to prepare your machine manually.

### Building and running

In order to build and run the project, invoke:

``` bash
cd <project root>

./run.sh
```

This will build and run a Docker Compose project (combined for the sake of demo simplicity).

Your results will land in the `<project root>/volumes/build` folder.

In case inference results differ between ONNX and OpenVINO, three files will be produced:

``` bash
# Stores indices that are different in the result
<project root>/volumes/build/different_indices.txt

# Stores ONNX values, that are different
<project root>/volumes/build/build/different_onnx.txt

# Stores OpenVINO values, that are different
<project root>/volumes/build/build/different_openvino.txt
```

### Design and rationale

1. The solution uses suggested tools and libraries:

   - Python wherever possible.
   - PyTorch with ONNX extensions for ONNX model generation.
   - onnxruntime for ONNX model inference.
   - OpenVINO in the Python flavour for OpenVINO model generation and inference.
   - Netron wrapped in netron-export for the sake of headless/scripted usage.
   - Numpy for input and output data storage, manipulation and comparison.

2. The project has the following structure
   - `provision_linux_x86_64.sh` script prepares the environment
   - `run.sh` script builds and runs the project
   - `source\app` folder contains business logic (core of the task)
   - `source\containers` folder contains Docker-related code
   - `source\glue` folder contains helper scripts used for running containers

3. Certain simplifications have been made, as I considered them not the objective of the task:

   - There are no performance optimisations. All operations assume small input that fully fits in RAM.
   - Python scripts are naive (hardcoded paths/parameters, minimal error checking/handling,
       simple logging to standard error).
   - Single, small and random test dataset is being generated and used.
       In a production setup we'd prefer non-naive, multiple, targeted datasets.
   - Inference is being run on the CPU for the sake of maximum portability.
   - Results diffing is done with trivial Numpy array comparison (float comparison with epsilon).
   - All scripts (including building) are being invoked with a single call in order to make the demo simple.
   - Linux is being used as Docker can run for free on all operating systems (including WSL on Windows).
   - Docker-Compose is being used even though a pure Docker would suffice.  
       I simply had this solution at hand from my past projects.

4. The solution is being packaged in a Docker container in order to:

   - Express the whole solution as code (including dependencies).
   - Let you (the reviewer) run it with two commands (provisioning and running).
   - Reduce the "demo effect".
   - Demonstrate a modern approach with "infrastructure as a code".
   - Have it up and running after 10 years to bring back nostalgia.

5. Using Docker adds some complexity and noise.
   In my opinion this complexity is compensated with rationale from point 3.
