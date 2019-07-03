FROM arm64v8/debian

RUN apt-get update && \
	apt-get install -y unzip python-dev gcc make && \
	apt-get install -y --reinstall build-essential

RUN mkdir -p /opt/pybliss 

WORKDIR /opt/pybliss 

COPY . .

RUN make && python setup.py install

RUN mkdir -p /home/pybliss 

WORKDIR /home/pybliss 

ADD test_enumerate.py .
ADD test_iso.py .
ADD data/ ./data/

CMD ["bash"]
