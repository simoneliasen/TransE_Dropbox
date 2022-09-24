FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

ENV PATH=/opt/conda/bin:$PATH

WORKDIR /transe

COPY . .

RUN apt update -y && apt upgrade -y && apt-get install -y wget time && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && bash ~/miniconda.sh -b -p /opt/conda && rm ~/miniconda.sh && conda init

RUN conda create -n transe -c conda-forge -y python=2.7 theano=0.9 numpy scipy nose_parameterized mkl-service && conda activate transe && bash download_data.sh && bash process_data.sh
