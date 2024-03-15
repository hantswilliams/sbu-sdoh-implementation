import json
import os
import requests


#fhir server endpoint
URL = "http://localhost:8080/fhir"

#fhir server json header content
headers = {"Content-Type": "application/fhir+json;charset=utf-8"}

# got to synthea, and generate/download a R4 bundle of fake patients and save to local folder
# or potentially remote s3/blob storage

#loop over all files in the output folder in order to upload each json file for each patient.
for dirpath, dirnames, files in os.walk('FHIR/docker_output/fhir/'):

    for file_name in files:
        print('Uploading file: ' + file_name)
        with open('FHIR/docker_output/fhir/'+file_name, "r") as bundle_file:
                data = bundle_file.read()

        r = requests.post(url = URL, data = data, headers = headers)

        #output file name that was processed
        print(file_name)