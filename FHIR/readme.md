# For Generating Fake Datasets with FHIR - R4: 
- Can use online tool to generate docker image: 
    - https://synthetichealth.github.io/spt/#/customizer 
- Then follow instructions: 
    - docker build --tag syntheadocker .
    - mkdir docker_output
    - docker run -v ./docker_output:/output -it syntheadocker

# For Running FHIR server, recommend going with HAPI FHIR: 
- https://github.com/hapifhir/hapi-fhir-jpaserver-starter
- Clone the repo/create a fork....etc 
- Simple server that can just do `docker compose up` on 

# Pushing data to FHIR resource: 
- Can then use the scratch_fhir_upload 