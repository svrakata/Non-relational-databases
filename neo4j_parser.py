# import tarfile
# import pandas as pd
# import numpy as nm
# import os

# filePath =  './data/clinical.cart.2019-02-13.tar.gz'
# files = tarfile.open(filePath)

# pMember = files.getmembers()[0]
# exMember = files.getmembers()[1]

# patients = files.extractfile(pMember)
# exposure = files.extractfile(exMember)

# pDataFrame = pd.read_csv(patients, sep='\t')

# class graphBase(object):
#     def __init__(self, uri, user, password):
#         self._driver = GraphDatabase.driver(uri, auth=(user, password))

#     def close(self):
#         self._driver.close()

def init():
    print('neo4j parser started')

    
