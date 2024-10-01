# AWS ETL Pipeline Project

## Overview

This project demonstrates the creation of an ETL pipeline using AWS services, including S3, IAM, Glue, and Athena. The pipeline ingests data, transforms it, and loads it into S3 in Parquet format, with scheduled triggers for automation.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Steps Performed](#steps-performed)
- [Trigger Configuration](#trigger-configuration)
- [License](#license)

## Technologies Used

- **AWS S3**: For data storage
- **AWS IAM**: For role and permission management
- **AWS Glue**: For ETL processes and data cataloging
- **AWS Athena**: For querying data
- **AWS Glue Crawler**: For automatic schema discovery

## Getting Started

### Prerequisites

- An AWS account
- Basic knowledge of AWS services
- AWS CLI configured on your local machine

### Setup Instructions

1. **Create an S3 Bucket**
   - Create an S3 bucket with three subfolders.
   - Upload the CSV file into the bucket.

2. **Create an IAM Role for Glue**
   - Create an IAM role for the Glue workspace with admin access.

3. **Create a Database in AWS Glue Data Catalog**
   - Initially, attempt to create tables manually for the database.

4. **Set Up AWS Glue Crawler**
   - Configure a Glue Crawler to automatically create schemas of the tables.
   - Run the crawler to populate the Glue Data Catalog.

5. **ETL Process**
   - **Source**: Data ingested from the AWS Data Catalog.
   - **Transformation**: Change schemas as needed.
   - **Target**: Load the transformed data into the S3 bucket in Parquet format.
   - AWS Glue will generate the ETL job script automatically.

6. **Run the ETL Job**
   - Execute the ETL job to load data into the S3 bucket in Parquet format.

7. **Athena Configuration**
   - Create a connection with AWS Athena to read the transformed data.
   - Load query results into the S3 bucket.

## Trigger Configuration

- Create triggers to schedule jobs daily.
- Support for event-based triggers.
- Ability to activate or deactivate triggers on a daily basis.


