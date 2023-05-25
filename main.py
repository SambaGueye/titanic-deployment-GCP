# import pandas as pd
# import numpy as np

from google.cloud import bigquery
# import os

bigquery_client = bigquery.Client(project='dev-project-360718')

def query_load(client, query, destination_table):
    
    # client = self.bigquery_client()
    job_config = bigquery.QueryJobConfig(
        write_disposition="WRITE_TRUNCATE", #WRITE_APPEND
        destination=destination_table,
    )
    query_job = client.query(
        query=query,
        job_config=job_config,
    )
    return query_job




if __name__=='__main__':

    DESTINATION = 'dev-project-360718.titanic_dataset.survived_titanic'

    query = """
    # CREATE OR REPLACE TABLE ${DESTINATION} AS (
    select * from `dev-project-360718.titanic_dataset.titanic`
    where Survived=1
    # )
    """
    
    res = query_load(bigquery_client, query, DESTINATION)
    if(res):
        print('Job  exécuté avec succèss')
    else:
        print('Erreur lors du lancement du Job bigquery')