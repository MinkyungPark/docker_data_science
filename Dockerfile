FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
    && apt install -y htop python3-dev wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

RUN conda create -y -n ml python==3.7

COPY . src/
RUN pip install --upgrade pip
RUN /bin/bash -c "cd src \
    && source activate ml \
    && pip3 install --no-cache-dir -r requirements.txt"
RUN mkdir root/docker_data
RUN cd src && mv train.csv ../docker_data