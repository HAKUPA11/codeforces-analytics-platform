<div align="center">

# Codeforces Analytics Platform

**Competitive Programming Data Engineering & Analytics System**

A database-centric platform that automates the collection, storage, and analysis of Codeforces data through a fully integrated ETL pipeline built with Python and MySQL.

---

Python • MySQL • SQL • ETL • REST API • Data Analytics

</div>


## Overview

Competitive programming platforms generate a massive amount of valuable data every day—contest participation, problem solving patterns, rating changes, submission statistics, and language usage.

The **Codeforces Analytics Platform** transforms this raw data into a structured relational database capable of supporting analytical queries and reporting. Using the official Codeforces API, the platform automatically extracts data, processes it through Python ETL pipelines, and stores it in a normalized MySQL database designed for efficient querying and future scalability.

The project demonstrates practical applications of database engineering, SQL programming, API integration, and data pipeline development using real-world data.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Automated Data Collection | Retrieves live data directly from the official Codeforces API |
| ETL Pipeline | Extracts, transforms and loads data into MySQL |
| Relational Database | Stores normalized contest, user and submission data |
| SQL Programming | Implements Views, Stored Procedures and Triggers |
| Analytics | Generates meaningful insights through SQL queries |
| Data Integrity | Prevents duplicate records through reusable upsert procedures |

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

## ETL Workflow

```mermaid
flowchart LR

    A[Codeforces API]

    A --> B1[user.info]
    A --> B2[contest.list]
    A --> B3[problemset.problems]
    A --> B4[user.status]
    A --> B5[user.rating]

    B1 --> C[load_users.py]
    B2 --> D[load_contests.py]
    B3 --> E[load_problems.py]
    B3 --> F[load_problem_tags.py]
    B4 --> G[load_submissions.py]
    B5 --> H[load_rating_history.py]

    C --> I[(MySQL Database)]
    D --> I
    E --> I
    F --> I
    G --> I
    H --> I
```


## Database Schema

The platform is built on a **normalized relational database** designed to efficiently manage competitive programming data while maintaining referential integrity. The schema consists of **seven core entities** connected through foreign key relationships, enabling efficient querying and analytical reporting.

### Entity Overview

| Table | Description | Primary Key |
| :----- | :---------- | :---------- |
| `users` | Stores Codeforces user profiles, ratings, organizations, and account metadata. | `user_id` |
| `contests` | Maintains contest information including contest type, phase, duration, and schedule. | `contest_id` |
| `problems` | Contains contest problems along with rating, points, difficulty, and metadata. | `problem_id` |
| `tags` | Stores the master list of problem tags used for categorization. | `tag_id` |
| `problem_tags` | Junction table implementing the many-to-many relationship between problems and tags. | `(problem_id, tag_id)` |
| `submissions` | Records user submissions, verdicts, execution time, memory usage, and programming language. | `submission_id` |
| `rating_history` | Stores historical rating updates after every rated contest. | `rating_history_id` |

---

### Entity Relationships

```mermaid
erDiagram

    USERS ||--o{ SUBMISSIONS : submits
    CONTESTS ||--o{ SUBMISSIONS : contains
    PROBLEMS ||--o{ SUBMISSIONS : attempts

    CONTESTS ||--o{ PROBLEMS : includes

    USERS ||--o{ RATING_HISTORY : has
    CONTESTS ||--o{ RATING_HISTORY : updates

    PROBLEMS ||--o{ PROBLEM_TAGS : categorized_as
    TAGS ||--o{ PROBLEM_TAGS : classifies
```

---

### Design Highlights

- Database follows **Third Normal Form (3NF)** to eliminate redundancy and improve maintainability.
- **Primary Keys** uniquely identify every entity.
- **Foreign Keys** enforce referential integrity across related tables.
- **Stored Procedures** are used for controlled insertion and update operations.
- **Views** simplify analytical reporting by exposing pre-joined datasets.
- **Triggers** automate timestamp management and maintain database consistency.
- The schema is designed to support efficient analytical queries while remaining scalable for future enhancements.


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

