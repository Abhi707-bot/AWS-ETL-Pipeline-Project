# AWS ETL Pipeline Project

## Overview
This project demonstrates the creation of an ETL pipeline using AWS services, including S3, IAM, Glue, and Athena. The pipeline ingests data, transforms it, and loads it into S3 in Parquet format, with scheduled triggers for automation.

## Table of Contents
  ![Link Text](♦ Technologies Used)
  ♦ Getting Started
  ♦ Project Structure
  ♦ Steps Performed
  ♦ Trigger Configuration

## Technologies Used
  ♦ AWS S3: For data storage
  ♦ AWS IAM: For role and permission management
  ♦ AWS Glue: For ETL processes and data cataloging
  ♦ AWS Athena: For querying data
  ♦ AWS Glue Crawler: For automatic schema discovery

## Getting Started

### Prerequisites

• An AWS account
• Basic knowledge of AWS services
• AWS CLI configured on your local machine
https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html

## Setup Instructions

1) Create an S3 Bucket
    - Create an S3 bucket with three subfolders.
    - Upload the CSV file into the bucket.

   ![s3bucket](https://github.com/user-attachments/assets/71948b4e-0d2c-49b8-acbf-7d599a375fb1)

   
3) Create an IAM Role for Glue
    - Create an IAM role for the Glue workspace with admin access.
   
   
4) Create a Database in AWS Glue Data Catalog
    • Initially, attempt to create tables manually for the database.

5) Set Up AWS Glue Crawler
    • Instead of manual table creation, configure a Glue Crawler to automatically create schemas of the tables.
    • Run the crawler to populate the Glue Data Catalog.

6) ETL Process
    • Source: Data ingested from the AWS Data Catalog.
    • Transformation: Change schemas as needed.
    • Target: Load the transformed data into the S3 bucket in Parquet format.
    • AWS Glue will generate the ETL job script automatically.

7) Run the ETL Job
   • Execute the ETL job to load data into the S3 bucket in Parquet format.

8) Athena Configuration
   • Create a connection with AWS Athena to read the transformed data.
   • Load query results into the S3 bucket.
   
9) Trigger Configuration
• Create triggers to schedule jobs daily.
• Support for event-based triggers.
• Ability to activate or deactivate triggers on a daily basis.


