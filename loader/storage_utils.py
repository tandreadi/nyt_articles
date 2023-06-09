from google.cloud import bigquery
import os
import utils


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'nytarticles-bigquery_credentials.json'


def create_bucket(storage_client, date):
    """Create a bucket in google cloud storage"""

    bucket_name = 'data_bucket_' + date

    bucket = storage_client.bucket(bucket_name)
    bucket.location = 'EUROPE-CENTRAL2'
    bucket = storage_client.create_bucket(bucket)

    return bucket


def create_external_table(date):
    """Create the external table in Bigquery"""

    # Construct a BigQuery client object.
    client = bigquery.Client()

    dataset_id = 'nyt_articles_dataset'
    project = 'nytarticles'
    bigquery.DatasetReference(project, dataset_id)
    table_id = f"nytarticles.nyt_articles_dataset.et_nyt_articles_{date}"

    # Configure the external data source and query job.
    external_config = bigquery.ExternalConfig("NEWLINE_DELIMITED_JSON")
    external_config.source_uris = [f"gs://data_bucket_{date}/nyt_articles_{date}"]
    external_config.schema = utils.define_table_schema()

    table = bigquery.Table(table_id, schema=external_config.schema)
    table.external_data_configuration = external_config

    # Create a permanent table linked to the GCS file
    table = client.create_table(table)  # API request


def create_table():
    """Create the table in Bigquery"""

    # Construct a BigQuery client object.
    client = bigquery.Client()
    table_id = "nytarticles.nyt_articles_dataset.nyt_articles"

    # Define the schema
    schema = utils.define_table_schema()

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
