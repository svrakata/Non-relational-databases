FROM ubuntu
LABEL author="svrakata"

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install python3.6

WORKDIR /code
COPY ./neo4j_parser.py /code
COPY ./entry.py /code

ENTRYPOINT [ "python3.6" ]

CMD [ "entry.py" ]