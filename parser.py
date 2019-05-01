import tarfile
import pandas
import os

pZip = tarfile.open('./data/clinical.cart.2019-02-13.tar.gz')
pMember = pZip.getmembers()[0]
exMember = pZip.getmembers()[1]

patients = pZip.extractfile(pMember)
exposure = pZip.extractfile(exMember)

print(patients.read())