# 📊🐍🗃️ Data Engineering Foundations

## Messy Data Enters, Reliable Pipelines Leave 🚰✨

Welcome to the **Data Engineering Foundations** phase of my Cloud Data & Security Engineering roadmap.

This phase moves from small scripts into systems that ingest, clean, validate, store, query, and document data.

Data engineering is not simply “move CSV from Folder A to Folder B.”

It is deciding:

- What the data means
- How it should be structured
- How it moves
- What happens when it is wrong
- What happens when the API fails
- How the pipeline can be repeated
- How another engineer can understand it later

A pipeline that only works once on my laptop is not a pipeline. It is a very confident accident 😭

This phase builds reliability from the beginning.

---

## 🎓 Roadmap Certification Checkpoint

**AWS Certified Data Engineer - Associate**

The roadmap uses this phase to build the core data concepts that later move into AWS services and cloud-native pipelines.

---

## 🎯 What This Phase Covers

### 📦 Data Formats and Wrangling

- Data-engineering lifecycle overview
- CSV, JSON, and Parquet
- pandas fundamentals
- Cleaning data
- Filtering and grouping
- Datetime handling
- Time-based reporting

### 🗃️ SQL and Data Modeling

- SQL joins
- Aggregations and KPIs
- Common table expressions and subqueries
- Window functions
- Database-design basics
- Normalization
- PostgreSQL local setup

### 🚰 ETL and Application-to-Database Flow

- ETL concepts
- Python and SQLAlchemy
- Loading data into PostgreSQL
- Data-quality checks
- Great Expectations concepts
- Logging in Python
- Error handling and fault tolerance

### 🌍 API Ingestion and Resilience

- HTTP API requests
- External data ingestion
- Pagination
- Retries and backoff
- Resilient API clients

### 🐳 Reproducibility and Collaboration

- Docker fundamentals
- Containerizing ETL jobs
- Docker Compose
- Multi-service local environments
- Git branching and pull requests
- Project planning and architecture documentation

### 🧪 Portfolio Project Build

- API ingestion
- Data cleaning
- Database storage
- Validation
- Containerization
- Documentation
- SQL interview practice
- Phase refactoring and publication

---

## 🧰 Why This Matters

Cloud systems, security platforms, dashboards, machine-learning workflows, and business analytics all depend on reliable data movement.

The pipeline must survive messy inputs, missing values, duplicate records, API limits, network failures, schema drift, and human decisions made at 16:59 on a Friday.

This phase develops the habit of designing for failure instead of being personally betrayed when failure arrives.

Reliable data engineering means:

- Inputs are understood
- Transformations are explicit
- Quality is tested
- Failures are logged
- Retries are controlled
- Storage is structured
- Results are reproducible
- Documentation tells the truth

---

## 🗺️ Roadmap Learning Path

1. Map the data-engineering lifecycle
2. Compare CSV, JSON, and Parquet
3. Clean and transform data with pandas
4. Build time-based reports
5. Strengthen SQL joins, aggregations, CTEs, subqueries, and window functions
6. Design and normalize a relational schema
7. Run PostgreSQL locally with Docker
8. Build Python-to-PostgreSQL flows with SQLAlchemy
9. Add data-quality validation
10. Add structured logging and error handling
11. Pull data from APIs
12. Handle pagination, retries, and backoff
13. Containerize the ETL workflow
14. Run multiple services with Docker Compose
15. Use branches, pull requests, and project planning
16. Build, validate, containerize, document, and publish the phase capstone

---

## 📁 What You’ll Find in This Folder

```text
03-data-engineering-foundations/
├── README.md
└── day-projects/
    ├── day-01-data-engineering-lifecycle/
    ├── day-02-data-formats/
    ├── day-03-pandas-cleaning/
    ├── day-04-filtering-grouping-datetime/
    ├── day-05-sql-joins-and-aggregations/
    ├── day-06-ctes-subqueries-window-functions/
    ├── day-07-database-design-and-normalization/
    ├── day-08-postgresql-with-docker/
    ├── day-09-etl-concepts/
    ├── day-10-python-sqlalchemy/
    ├── day-11-data-quality-checks/
    ├── day-12-logging-and-error-handling/
    ├── day-13-api-ingestion/
    ├── day-14-pagination-retries-backoff/
    ├── day-15-dockerized-etl/
    ├── day-16-docker-compose-stack/
    ├── day-17-git-branching-and-prs/
    ├── day-18-project-planning/
    ├── day-19-to-22-capstone-build/
    ├── day-23-sql-practice-pack/
    └── day-24-phase-recap/
```

---

## 🧪 Portfolio Artifacts From This Phase

- `notes/data-engineering-lifecycle-map.md`
- `data-format-lab/csv-json-parquet-comparison.md`
- `pandas/clean-dataset.ipynb`
- `pandas/grouped-summary-report.py`
- `pandas/time-based-report.py`
- `sql/multi-table-queries.sql`
- `sql/kpi-aggregations.sql`
- `sql/ctes-and-subqueries.sql`
- `sql/window-functions.sql`
- `database/simple-schema.sql`
- `database/normalization-case-study.md`
- `postgres/docker-postgres-setup/`
- `etl/pipeline-design-sketch.png`
- `etl/sqlalchemy-loader.py`
- `quality/validation-rules.py`
- `logging/logged-pipeline.py`
- `reliability/fault-tolerant-job.py`
- `api/api-pull-script.py`
- `api/resilient-paginated-client.py`
- `docker/dockerized-etl/`
- `docker-compose/local-data-stack/`
- `collaboration/feature-branch-pr-demo.md`
- `capstone/api-to-postgres-pipeline/`
- `sql-practice/ten-interview-questions.sql`

These artifacts show the difference between moving data and engineering a dependable data flow.

---

## 🧠 Skills Gained Here

By the end of this phase, I should be able to:

- Explain the stages of a data pipeline
- Choose between CSV, JSON, and Parquet for a use case
- Clean, filter, group, and transform data with pandas
- Handle timestamps and time-based analysis
- Write joins, aggregations, CTEs, subqueries, and window functions
- Design and normalize a relational schema
- Run PostgreSQL locally
- Load data with Python and SQLAlchemy
- Define and execute data-quality checks
- Add useful logs and error handling
- Ingest API data
- Handle pagination, transient failures, retries, and backoff
- Containerize an ETL process
- Use Docker Compose for a local data stack
- Work with branches and pull requests
- Plan and document a data project

---

## 🌍 Real-World Connection

This phase connects directly to:

- Junior data engineering
- Analytics engineering
- Cloud data pipeline development
- Security data ingestion
- API integration
- Database operations
- Data-quality engineering
- Platform automation
- DevOps-supported data workflows

Security teams need reliable telemetry.

Analytics teams need trustworthy models.

Cloud platforms need reproducible pipelines.

This phase is where those needs start becoming actual code.

---

## 🏁 Phase Capstone: Dockerized API-to-PostgreSQL Pipeline

The capstone should:

1. Pull records from a safe public or generated API
2. Handle pagination and transient failures
3. Clean and transform the data
4. Validate at least five quality rules
5. Load the result into PostgreSQL
6. Log pipeline progress and failures
7. Run inside Docker
8. Start supporting services with Docker Compose
9. Include SQL queries that demonstrate useful analysis
10. Include an architecture diagram and polished README

Suggested flow:

```text
API → Python Ingestion → Validation → Transformation → PostgreSQL → SQL Report
```

The final repository should become the first strong data-engineering case study in the portfolio.

---

## ✅ Phase Completion Checklist

- [ ] I compared CSV, JSON, and Parquet
- [ ] I completed pandas cleaning and reporting labs
- [ ] I strengthened analytical SQL
- [ ] I designed and normalized a relational schema
- [ ] I ran PostgreSQL locally
- [ ] I loaded data with SQLAlchemy
- [ ] I added quality checks
- [ ] I added logging and fault handling
- [ ] I built a paginated API client with retries
- [ ] I containerized an ETL job
- [ ] I used Docker Compose for the local stack
- [ ] I used a feature branch and pull-request workflow
- [ ] I solved the SQL practice pack
- [ ] I published the capstone as a reproducible portfolio artifact

---

## 🔜 What Comes Next

Next is **Cloud Foundations**.

The pipeline skills now move into AWS: compute, storage, identity, networking, monitoring, serverless workflows, databases, analytics services, and infrastructure as code.

Local pipeline complete. Time to send it into the sky ☁️🚀

[⬅️ Previous Phase: Networking + Security Basics](../02-networking-security-basics/README.md) | [Main Roadmap](../README.md) | [Next Phase: Cloud Foundations ➡️](../04-cloud-foundations/README.md)
