import storage_utils as su
import utils
import nyt_newswire_api as nyt
import functions_framework
from datetime import datetime
from google.cloud import storage
from google.cloud import bigquery


# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def load_articles(cloud_event):

    nyt_articles = nyt.NYTimesAPI()
    ndjson_data = nyt_articles.get_articles_from_nyt()
    storage_client = storage.Client.from_service_account_json('nytarticles-bigquery_credentials.json')

    date = datetime.now().strftime("%d-%m-%Y")
    bucket = su.create_bucket(storage_client, date)

    # Convert the current datetime to string
    blob = bucket.blob(utils.create_file_name(date))

    # Upload the blob
    blob.upload_from_string(data=ndjson_data, content_type='application/json')

    # Create external table
    su.create_external_table(date)

    client = bigquery.Client()

    query = utils.merge_query(date)

    client.query(query)
