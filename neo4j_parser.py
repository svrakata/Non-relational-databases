import tarfile
import pandas as pd
import numpy as nm
from neo4j.v1 import GraphDatabase
import os


def readAndParseFiles():
    filePath =  './data/clinical.cart.2019-02-13.tar.gz'
    files = tarfile.open(filePath)

    pMember = files.getmembers()[0]
    exMember = files.getmembers()[1]

    patients = files.extractfile(pMember)
    exposure = files.extractfile(exMember)

    return pd.read_csv(patients, sep='\t')


class graphBase(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
    def close(self):
        self._driver.close()



def init():
    db = graphBase('bolt://localhost:7687', 'neo4j', 'test')
    df = readAndParseFiles()
    rows = df.iterrows()
    # print(df.to_dict(orient='records'))
    print(df['days_to_birth'].astype(int))


if __name__ == '__main__':
    init()