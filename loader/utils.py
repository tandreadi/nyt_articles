from google.cloud import bigquery


def create_file_name(date):
    '''Generate a .json filename using the current date'''

    file_name = 'nyt_articles_' + date

    return file_name


def define_table_schema():
    """Define the table schema"""

    schema = [
        bigquery.SchemaField("slug_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("section", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("subsection", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("title", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("abstract", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("uri", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("url", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("byline", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("thumbnail_standard", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("item_type", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("source", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("updated_date", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("created_date", "TIMESTAMP", mode="NULLABLE"),
        bigquery.SchemaField("published_date", "TIMESTAMP", mode="NULLABLE"),
        bigquery.SchemaField("first_published_date", "TIMESTAMP", mode="NULLABLE"),
        bigquery.SchemaField("material_type_facet", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("kicker", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("subheadline", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("des_facet", "STRING", mode="REPEATED"),
        bigquery.SchemaField("org_facet", "STRING", mode="REPEATED"),
        bigquery.SchemaField("geo_facet", "STRING", mode="REPEATED"),
        bigquery.SchemaField("per_facet", "STRING", mode="REPEATED"),
        bigquery.SchemaField("related_urls", "RECORD", mode="REPEATED",
                             fields=[
                                 bigquery.SchemaField("suggested_link_text",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("url",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                    ],
                            ),
        bigquery.SchemaField("multimedia", "RECORD", mode="REPEATED",
                             fields=[
                                 bigquery.SchemaField("url",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("format",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("height",
                                                      "INTEGER",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("width",
                                                      "INTEGER",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("type",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("subtype",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("caption",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                 bigquery.SchemaField("copyright",
                                                      "STRING",
                                                      mode="NULLABLE"),
                                    ],
                            ),
            ]
    return schema


def merge_query(date):
    """ The query that merges the external table"""

    query = f"""
        MERGE `nyt_articles_dataset.nyt_articles` T
        USING `nyt_articles_dataset.et_nyt_articles_{date}` ET
        ON T.uri = ET.uri
        WHEN MATCHED THEN
            UPDATE SET T.slug_name = ET.slug_name, T.section = ET.section, T.subsection = ET.subsection,
            T.title = ET.title, T.abstract = ET.abstract, T.uri = ET.uri, T.url = ET.url, T.byline = ET.byline,
            T.thumbnail_standard = ET.thumbnail_standard, T.item_type = ET.item_type, T.source = ET.source,
            T.updated_date = ET.updated_date, T.created_date = ET.created_date, T.published_date = ET.published_date,
            T.first_published_date = ET.first_published_date, T.material_type_facet = ET.material_type_facet,
            T.kicker = ET.kicker, T.subheadline = ET.subheadline, T.des_facet = ET.des_facet, T.org_facet = ET.org_facet,
            T.per_facet = ET.per_facet, T.geo_facet = ET.geo_facet, T.related_urls = ET.related_urls, T.multimedia = ET.multimedia
        WHEN NOT MATCHED THEN
            INSERT(slug_name, section, subsection, title, abstract, uri, url, byline, thumbnail_standard,
                    item_type, source, updated_date, created_date, published_date, first_published_date, material_type_facet,
                    kicker, subheadline, des_facet, org_facet, per_facet, geo_facet, related_urls, multimedia)
            VALUES (ET.slug_name, ET.section, ET.subsection, ET.title, ET.abstract, ET.uri, ET.url, ET.byline, ET.thumbnail_standard,
                    ET.item_type, ET.source, ET.updated_date, ET.created_date, ET.published_date, ET.first_published_date, ET.material_type_facet,
                    ET.kicker, ET.subheadline, ET.des_facet, ET.org_facet, ET.per_facet, ET.geo_facet, ET.related_urls, ET.multimedia)
    """
    return query
