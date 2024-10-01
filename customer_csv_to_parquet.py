import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1727714434523 = glueContext.create_dynamic_frame.from_catalog(database="customers_db", table_name="customers_csv", transformation_ctx="AWSGlueDataCatalog_node1727714434523")

# Script generated for node Change Schema
ChangeSchema_node1727714482580 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1727714434523, mappings=[("customerid", "long", "customerid", "long"), ("namestyle", "boolean", "namestyle", "boolean"), ("title", "string", "title", "string"), ("firstname", "string", "firstname", "string"), ("middlename", "string", "middlename", "string"), ("lastname", "string", "lastname", "string"), ("suffix", "string", "suffix", "string"), ("companyname", "string", "companyname", "string"), ("salesperson", "string", "salesperson", "string"), ("emailaddress", "string", "emailaddress", "string"), ("phone", "string", "phone", "string"), ("passwordhash", "string", "passwordhash", "string"), ("passwordsalt", "string", "passwordsalt", "string"), ("rowguid", "string", "rowguid", "string"), ("modifieddate", "string", "modifieddate", "string"), ("dataload", "string", "dataload", "string")], transformation_ctx="ChangeSchema_node1727714482580")

# Script generated for node Amazon S3
AmazonS3_node1727714528313 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1727714482580, connection_type="s3", format="glueparquet", connection_options={"path": "s3://glue-demo-new071/data/customers_db/customer_parquet/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1727714528313")

job.commit()