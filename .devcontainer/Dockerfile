FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget bzip2 cmake build-essential git x11-apps libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh
# Add conda to PATH
ENV PATH="/opt/conda/bin:$PATH"

RUN conda tos accept

# Install OpenLPT
WORKDIR /opt
RUN git clone https://github.com/clockj/OpenLPT.git \
    && cd OpenLPT \
    && conda create -n OpenLPT python=3.9 

SHELL ["conda", "run", "-n", "OpenLPT", "/bin/bash", "-c"]
RUN cd OpenLPT \
    && pip install -r requirements.txt \
    && pip install .