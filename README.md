# Codeforces Analytics Platform

A full-stack data engineering and database analytics project that collects, stores, and analyzes competitive programming data from the Codeforces API.

The platform automates data ingestion using Python ETL pipelines, stores normalized data in MySQL, and provides SQL-based analytical insights through views, stored procedures, and business analytics queries.

## Project Overview

The Codeforces Analytics Platform is designed to automate the collection and analysis of competitive programming data.

The project retrieves live data from the official Codeforces API, stores it in a normalized MySQL database, and provides meaningful analytical queries for users, contests, problems, submissions, and rating history.

The objective of this project is to demonstrate practical database design, SQL programming, ETL development, and API integration using real-world data.

## Features

- Automated data extraction from Codeforces API
- Normalized relational database
- MySQL Views
- Stored Procedures
- Database Triggers
- Business Analytics Queries
- Python ETL Pipelines
- Duplicate-safe Upsert Operations
- Rating History Tracking
- Problem Tag Mapping

## Tech Stack

### Database
- MySQL 8

### Backend
- Python 3

### Libraries
- mysql-connector-python
- requests
- python-dotenv

### APIs
- Codeforces API

### Version Control
- Git
- GitHub

Codeforces API
        │
        ▼
Python ETL
        │
        ▼
Stored Procedures
        │
        ▼
MySQL Database
        │
        ▼
Views
        │
        ▼
Analytics Queries


## Database Schema

### Users

Stores user profile information including

- Handle
- Ratings
- Contribution
- Organization
- Country
- Friend Count

---

### Contests

Stores contest metadata

- Contest ID
- Contest Name
- Contest Type
- Contest Phase
- Duration

---

### Problems

Stores contest problems

- Problem Index
- Rating
- Points
- Type

---

### Submissions

Stores submission history

- Verdict
- Language
- Execution Time
- Memory Usage

---

### Rating History

Stores rating changes after every contest.

---

### Tags

Stores problem tags.

---

### Problem Tags

Many-to-many relationship between Problems and Tags.


codeforces-analytics-platform/

data/

docs/

python/

database/

etl/

api/

utils/

sql/

01_database.sql

02_tables.sql

03_constraints.sql

04_indexes.sql

05_views.sql

06_procedures.sql

07_triggers.sql

08_queries.sql

09_analytics.sql


User Handle
      │
      ▼

Users API

Contest API

Problemset API

User Status API

Rating API

      │

      ▼

Python ETL

      ▼

Stored Procedures

      ▼

MySQL Database

## Database Objects

### Tables

- Users
- Contests
- Problems
- Tags
- Problem Tags
- Submissions
- Rating History

### Views

- User Profile
- Submission Details
- Contest Summary
- Problem Statistics
- User Statistics
- Contest Statistics
- Rating History
- Problem Details

### Stored Procedures

- User Upsert
- Contest Upsert
- Problem Upsert
- Tag Upsert
- Add Problem Tag
- Add Submission
- Add Rating History

### Triggers

Database automation triggers for maintaining integrity and timestamps.


## API

Official Codeforces API

Endpoints Used

- user.info
- contest.list
- problemset.problems
- user.status
- user.rating

## Setup

Clone Repository

Install Dependencies

pip install -r requirements.txt

Configure .env

Run

python main.py


## Current Dataset

Users : 1

Contests : 2138

Problems : 10000+

Submissions : 4746

Rating History : 306


## Future Improvements

- Bulk User Import
- Interactive Dashboard
- Power BI Reports
- Machine Learning Based Performance Prediction
- User Comparison
- Contest Recommendation System
- Scheduled ETL Jobs


## Author

Harsh Pandit

GitHub:
https://github.com/HAKUPA11

LinkedIn:

