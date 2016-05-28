FROM centos:7

RUN yum update -y && yum clean all

RUN yum install -y \
        autoconf \
        automake \
        gcc \
        git \
        libtool \
        m4 \
        make \
        pkgconfig \
        python \
        python-devel \
        tar

RUN curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install --upgrade \
        setuptools && \
    pip install --upgrade \
        pytest \
        pytest-cov \
        pytest-mock \
        flake8 \
        redis

WORKDIR /tmp
RUN mkdir -p /usr/local/{include,lib}

RUN curl http://download.redis.io/releases/redis-3.2.0.tar.gz | tar -xz && \
    pushd redis-3.2.0 && \
    make && \
    make install && \
    pushd deps/hiredis && \
    make install && \
    popd && \
    popd && \
    rm -rf redis-3.2.0*

RUN ldconfig -v

RUN useradd -m -U -s /bin/bash concrete && \
    passwd -l concrete
RUN echo 'export PATH="$HOME/.local/bin:$PATH"' >> \
        /home/concrete/.bashrc
ADD . /home/concrete/concrete-python
RUN chown -R concrete:concrete /home/concrete

USER concrete
WORKDIR /home/concrete/concrete-python
RUN python setup.py test --addopts '--cov=concrete/ tests' && \
    bash check-style.bash && \
    python setup.py install --user
