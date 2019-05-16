import tarfile
import pandas as pd
import numpy as nm
from neo4j.v1 import GraphDatabase
import os

# df stands for dataframe
# rows = df.iterrows()

class Parser():
    def __init__(self, filePath):
        self.archive = tarfile.open(filePath)
        self.members = self.archive.getmembers()

    def getDataAsDict(self):
        for m in self.members:
            f = self.archive.extractfile(m)

            df = pd.read_csv(f, sep='\t')
            yield df.to_dict(orient='records')


class graphBase(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def create(self):
        pass

    def close(self):
        self._driver.close()



def init():
    db = graphBase('bolt://localhost:7687', 'neo4j', 'test')
    df = Parser('./data/clinical.cart.2019-02-13.tar.gz')
    data = df.getDataAsDict()
    patients = next(data)
    exposure = next(data)






if __name__ == '__main__':
    init()