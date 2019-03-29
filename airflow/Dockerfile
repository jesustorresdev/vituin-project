FROM selenium/node-chrome:3.8.1-bohrium
LABEL authors=SeleniumHQ

USER seluser

#====================================
# Scripts to run Selenium Standalone
#====================================
#COPY entry_point.sh /opt/bin/entry_point.sh

EXPOSE 4444

USER root

ARG GECKODRIVER_VERSION=0.19.1
ARG CHROMEDRIVER_VERSION=2.34

#============
# Install pip and selenium-python
#============

RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends python-pip \
    && pip install selenium

#============
# GeckoDriver
#============
RUN wget https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && tar xzf geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && rm geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && export PATH=$PATH:/usr/local/bin/geckodriver

RUN wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && rm chromedriver_linux64.zip  \
    && mv chromedriver /usr/local/bin/ \
    && export PATH=$PATH:/usr/local/bin/chromedriver


# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Airflow
ARG AIRFLOW_VERSION=1.8.0
ARG AIRFLOW_HOME=/usr/local/airflow

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN set -ex \
    && buildDeps=' \
        python-dev \
        libkrb5-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        build-essential \
        libblas-dev \
        liblapack-dev \
        libpq-dev \
        git \
    '
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        $buildDeps \
        python-pip \
        python-requests \
        apt-utils \
        curl \
        netcat \
        locales \
        sudo \
        wget
RUN apt-get install -yqq --no-install-recommends  \
  autoconf                                \
  automake                                \
  build-essential                         \
  ca-certificates                         \
  g++                                     \
  gdb                                     \
  git-core                                \
  heimdal-clients                         \
  libapr1-dev                             \
  libboost-dev                            \
  libcurl4-nss-dev                        \
  libgoogle-glog-dev                      \
  libprotobuf-dev                         \
  libpython-dev                           \
  libsasl2-dev                            \
  libsasl2-modules-gssapi-heimdal         \
  libsvn-dev                              \
  libtool                                 \
  make                                    \
  protobuf-compiler                       \
  python                                  \
  python-dev                              \
  python-pip                              \
  python-protobuf                         \
  python-setuptools                       \
  python-virtualenv                       \
  python2.7                               \
  unzip                                   \
  zlib1g-dev

RUN sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \
    && python -m pip install -U pip \
    && pip install setuptools \
    && pip install Cython \
    && pip install pytz \
    && pip install pyOpenSSL \
    && pip install ndg-httpsclient \
    && pip install pyasn1 \
    && pip install airflow[crypto,celery,postgres,hive,hdfs,jdbc]==$AIRFLOW_VERSION \
    && pip install celery[redis]==3.1.17 \
    && pip install scrapy \
    && pip install nltk \
    && pip install elasticsearch \
    && pip install elasticsearch-dsl \
    && pip install xlrd \
    && pip install googlemaps \
    && apt-get remove --purge -yqq $buildDeps \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base
RUN set -ex \
    && pip install airflow[github_enterprise,redis,docker]==$AIRFLOW_VERSION




COPY script/entrypoint.sh /entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg


RUN chown -R airflow: ${AIRFLOW_HOME}

EXPOSE 8080 5555 8793

USER airflow
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]

#COPY entrypoint.sh /opt/bin/entrypoint.sh

