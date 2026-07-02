# Data Redundancy Removal System

## Overview

The Data Redundancy Removal System is a cloud-based application developed using Python Flask and PostgreSQL. It identifies duplicate records in a database and removes redundant entries to improve data consistency, storage efficiency, and database performance.

## Features

* Duplicate record detection
* Automatic redundancy removal
* PostgreSQL database integration
* Flask web application
* AWS EC2 deployment
* Simple and user-friendly interface

## Technology Stack

* Python 3
* Flask
* PostgreSQL
* HTML
* AWS EC2
* Ubuntu Linux

## Project Architecture

User Browser
↓
Flask Application
↓
Duplicate Validation Module
↓
PostgreSQL Database
↓
Cleaned Data Output

## Database Schema

| Column | Description        |
| ------ | ------------------ |
| id     | Unique Identifier  |
| name   | User Name          |
| email  | User Email Address |

### Sample Data

| id | name  | email                                     |
| -- | ----- | ----------------------------------------- |
| 1  | Sai   | [sai@gmail.com](mailto:sai@gmail.com)     |
| 2  | Sai   | [sai@gmail.com](mailto:sai@gmail.com)     |
| 3  | Ravi  | [ravi@gmail.com](mailto:ravi@gmail.com)   |
| 4  | Ravi  | [ravi@gmail.com](mailto:ravi@gmail.com)   |
| 5  | Kiran | [kiran@gmail.com](mailto:kiran@gmail.com) |
| 6  | Teja  | [teja@gmail.com](mailto:teja@gmail.com)   |
| 7  | Sasi  | [sasi@gmail.com](mailto:sasi@gmail.com)   |

### Output After Duplicate Removal

| id | name  | email                                     |
| -- | ----- | ----------------------------------------- |
| 1  | Sai   | [sai@gmail.com](mailto:sai@gmail.com)     |
| 3  | Ravi  | [ravi@gmail.com](mailto:ravi@gmail.com)   |
| 5  | Kiran | [kiran@gmail.com](mailto:kiran@gmail.com) |
| 6  | Teja  | [teja@gmail.com](mailto:teja@gmail.com)   |
| 7  | Sasi  | [sasi@gmail.com](mailto:sasi@gmail.com)   |

## Installation

### Clone Repository

git clone https://github.com/Venkata291/DATA-REDUNDANCY-REMOVAL-SYSTEM-Project.git

cd DATA-REDUNDANCY-REMOVAL-SYSTEM-Project

### Create Virtual Environment

python3 -m venv venv

source venv/bin/activate

### Install Dependencies

pip install flask psycopg2-binary

## Run Application

python3 app.py

Application URL:

http://PUBLIC_IP:5000

## API Endpoints

### Home Page

GET /

Response:

Data Redundancy Removal System Running

### Remove Duplicates

GET /remove_duplicates

Response:

{
"deleted_records": 2,
"message": "Duplicates Removed Successfully"
}

## AWS Infrastructure Used

* VPC
* Public Subnet
* Internet Gateway
* Route Table
* Security Group
* EC2 Instance
* PostgreSQL Database
* Flask Application

## Project Workflow

1. User accesses the Flask application.
2. Application connects to PostgreSQL database.
3. Duplicate records are identified.
4. Redundant entries are removed.
5. Database is updated with cleaned records.
6. Result is displayed to the user.

## Benefits

* Improves data quality
* Reduces storage redundancy
* Enhances database performance
* Maintains data consistency
* Simplifies data management

## Future Enhancements

* Machine Learning based duplicate detection
* User authentication
* Analytics dashboard
* Automated scheduled cleanup
* Multi-database support

## Author

Venkata Saibabu Kalluri

Cloud Computing Internship Project

Data Redundancy Removal System


