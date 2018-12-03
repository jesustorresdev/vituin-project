FROM plotly/dashboardsly

USER root

#============
# Install pip and plotly
#============

RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends python-pip \
    wget \
    nano \
    apache2 \
    npm \
    libapache2-mod-wsgi \
    && apt-get clean


RUN pip install dash==0.20.0  # The core dash backend
RUN pip install dash-renderer==0.7.3   # The dash front-end
RUN pip install dash-html-components==0.8.0  # HTML components
RUN pip install dash-core-components==0.18.1  # Supercharged components
RUN pip install plotly --upgrade  # Plotly graphing library used in examples
RUN pip install googlemaps
RUN pip install elasticsearch

RUN npm config set strict-ssl false
RUN npm install -g builder-init
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN pip install Werkzeug
RUN pip install plotly
RUN pip install jinja2
RUN pip install click
RUN pip install itsdangerous
RUN pip install flask-compress
RUN pip install dash-core-components
RUN pip install dash
RUN pip install dash-renderer

# In the carpet of plotly extra components write npm install
