FROM python:3

MAINTAINER Jiakun Fu

ADD requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt \
    && rm /requirements.txt

RUN pip3 install scipy scikit-learn statsmodels ipyvolume

ADD jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

WORKDIR /data/jiakun

COPY . /data/jiakun


ENTRYPOINT ["/bin/sh", "-c"]
CMD ["jupyter notebook --allow-root"]
#CMD jupyter lab --ip=* --port=8888 --no-browser --notebook-dir=/notebooks --allow-root