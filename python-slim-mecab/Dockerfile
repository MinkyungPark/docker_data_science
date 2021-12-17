FROM python:3.8-slim

RUN apt-get -qq update && \
  # slim variants dont have man page
  if [ ! -d /usr/share/man/man1 ]; then \
  mkdir -p /usr/share/man/man1; \
  fi; \
  apt-get install --no-install-recommends -y build-essential autotools-dev automake g++ openjdk-11-jdk-headless python3-dev git curl vim procps && \
  # mecab-ko
  cd /tmp && \
  curl -LO https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz && \
  tar zxfv mecab-0.996-ko-0.9.2.tar.gz && \
  cd mecab-0.996-ko-0.9.2 && ./configure && make && make check && make install && \
  ldconfig && \
  # mecab-ko-dic
  curl -LO https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz && \
  tar -zxvf mecab-ko-dic-2.1.1-20180720.tar.gz && \
  cd mecab-ko-dic-2.1.1-20180720 && \
  ./autogen.sh && ./configure && make && make install && \
  sh -c 'echo "dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic" > /usr/local/etc/mecabrc' && \
  cd / && \
  rm -rf /var/lib/apt/lists/* /tmp/* && \
  apt-get purge -y curl

WORKDIR /src/app
EXPOSE 5000

RUN pip install --upgrade pip && \
    pip install pip install numpy scipy gensim==3.8.3 JPype1 tweepy==3.10.0 konlpy mecab-python nltk pandas pymongo scikit-learn tqdm psutil Flask jupyterlab pybullet bym && \
	pip3 install torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html