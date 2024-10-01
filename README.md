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
  https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html

### Setup Instructions

1. **Create an S3 Bucket**
   
   - Create an S3 bucket with subfolders.
   - Upload the CSV file into the bucket.
     ![s3bucket](https://github.com/user-attachments/assets/1d17d7a8-c67d-4c60-ba2b-cfe9d8e7dca5)
<br />

3. **Create an IAM Role for Glue**
   
   - Create an IAM role for the Glue workspace with admin access.
     ![Iam](https://github.com/user-attachments/assets/da1f38bb-1a35-4522-b650-ba0a41d1e547)
<br />

4. **Create a Database in AWS Glue Data Catalog**
   
   - Initially, attempt to create tables manually for the database.
     ![dbdatacatalog](https://github.com/user-attachments/assets/b579273b-482b-4307-b39f-9711c320d915)
<br />

5. **Set Up AWS Glue Crawler**
   
   - Configure a Glue Crawler to automatically create schemas of the tables.
   - Run the crawler to populate the Glue Data Catalog.
     ![crawler1](https://github.com/user-attachments/assets/2eee1176-e63d-41d2-99f7-9a537d2f0d5c)
     ![crawler run](https://github.com/user-attachments/assets/2805ffdb-be32-46ea-8bdb-86d6ffcd4dcb)
     ![crawlercsv](https://github.com/user-attachments/assets/05890cad-088f-44bb-b5fb-639c18969555)
<br />


6. **ETL Process**
   
   - **Source**: Data ingested from the AWS Data Catalog.
     ![src](https://github.com/user-attachments/assets/354f4905-d1b1-402f-88eb-ad49d05c0546)

   - **Transformation**: Change schemas as needed.
     
   - **Target**: Load the transformed data into the S3 bucket in Parquet format.
     ![s3parquet](https://github.com/user-attachments/assets/98f6da32-e156-4b69-902a-b227a2203982)

   - AWS Glue will generate the ETL job script automatically.
     ![scripts](https://github.com/user-attachments/assets/804473ad-7807-4359-9102-c5ffb708b5ce)
<br />

7. **Run the ETL Job**
   
   - Execute the ETL job to load data into the S3 bucket in Parquet format.
     ![etlrun](https://github.com/user-attachments/assets/c82dffaf-5b10-4d27-92dd-d86ba9ddc8be)
<br />

8. **Athena Configuration**
   
   - Create a connection with AWS Athena to read the transformed data.
     ![athena connec](https://github.com/user-attachments/assets/5ba838bd-2ecb-483f-82fe-b17ddcdbbe72)

   - Load query results into the S3 bucket.
     ![reading data](https://github.com/user-attachments/assets/c95afcc4-562e-44be-a7bd-ed159bb4fe62)
<br />

## Trigger Configuration

- Create triggers to schedule jobs daily.
- Support for event-based triggers.
- Ability to activate or deactivate triggers on a daily basis.
  
  ![activ triigger](https://github.com/user-attachments/assets/81b26690-87b1-41fd-ac08-3afcc670cc28)



