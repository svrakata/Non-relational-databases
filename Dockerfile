FROM ubuntu
LABEL author="svrakata"

RUN apt-get update -y && \
    apt-get -y install python3.6 && \
    apt-get install -y python-pip python-dev && \
    pip install neo4j numpy pandas 

WORKDIR /code
COPY ./neo4j_parser.py /code
COPY ./entry.py /code

ENTRYPOINT [ "python3.6" ]

CMD [ "entry.py" ]