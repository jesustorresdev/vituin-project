FROM continuumio/miniconda3

RUN adduser --system --group vituin

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y curl

WORKDIR /home/vituin-dashboard

COPY --chown=vituin:vituin vituin-dashboard/environment.yml environment.yml
RUN conda env create -f environment.yml \
    && conda clean -tipsy

COPY --chown=vituin:vituin vituin-dashboard scripts ./
RUN chmod +x *.sh

USER vituin
EXPOSE 5000
CMD ["./boot.sh"]
