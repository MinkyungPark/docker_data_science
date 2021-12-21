# Base Image
FROM nvidia/cuda:11.2.0-base-ubuntu20.04
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Basic Utils
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -qq update && \
	apt-get install --no-install-recommends -y build-essential \
	bzip2 \
	ca-certificates \
	curl \
	git \
	libcanberra-gtk-module \
	libgtk2.0-0 \
	libx11-6 \
	sudo \
	graphviz \
	vim

# Install Miniconda
ENV PATH /opt/conda/bin:$PATH
RUN apt-get install -y wget ibglib2.0-0 libxext6 libsm6 libxrender1 \
	mercurial subversion
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
	/bin/bash ~/miniconda.sh -b -p /opt/conda && \
	rm ~/miniconda.sh && \
	ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
	echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
	echo "conda activate base" >> ~/.bashrc
RUN apt-get install -y default-jdk default-jre
RUN apt-get install -y grep sed dpkg && \
	TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
	curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
	dpkg -i tini.deb && \
	rm tini.deb && \
	apt-get clean

# Install Python Packages
RUN conda install av -c conda-forge && \
	conda install -c conda-forge jupyterlab && \
	pip install --upgrade pip && \
	pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install sklearn matplotlib pandas numba tensorflow tensorboard kss regex ray pymongo jupyterlab-system-monitor

RUN mkdir -p /workspace 
WORKDIR /workspace 

# KoLNPy
RUN pip install Jpype1 tweepy==3.10.0 konlpy 
RUN cd /workspace && \ 
	curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -s