FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3

ARG PYTHON_VERSION=3.9.18

# Install python 3.9.18 in base env
RUN conda install python=${PYTHON_VERSION} -y && conda clean -afy

# Install GUI support packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
 && rm -rf /var/lib/apt/lists/*

