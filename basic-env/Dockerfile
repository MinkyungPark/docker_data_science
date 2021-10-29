# Base Image   
FROM debian:latest
ENV LC_ALL=C.UTF-8

# Install Miniconda
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
RUN apt-get -qq update && apt-get -qq -y install wget curl bzip2 ca-certificates git sudo vim build-essential \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
#    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

# Install Python Packages
RUN pip install tensorflow && \
	pip install cython && \
	pip install nltk && \
	pip install pandas && \
	pip install seaborn && \
	pip install sklearn && \
	pip install simplejson && \
	pip install psycopg2-binary && \
	conda install av -c conda-forge && \
	pip install jupyterlab jupyterhub && \
	pip install jupyterlab-system-monitor




# KoLNPy
RUN mkdir -p /workspace 
WORKDIR /workspace 
RUN pip install Jpype1 konlpy 
RUN cd /workspace && \ 
	curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -s

# Requirements.txt 있을때
# COPY requirements.txt /tmp
# WORKDIR /tmp
# RUN pip install -r requirements.txt 