# Exchange Rate Dashboard

This project fetches exchange rate data from an API and stores it in a PostgreSQL database using Apache Airflow.

## Features
- Dockerized Airflow pipeline
- API integration
- PostgreSQL storage
- Optional Telegram CSV export
- Power BI dashboard-ready

## How to Run

1. Clone the repo:
   ```bash
   git clone git@github.com:madebylemon/fsoft-internship.git
   ```

2. Navigate into the project:
   ```bash
   cd exchange_rate_project
   ```

3. Start with Docker:
   ```bash
   docker-compose up --build
   ```

4. Access Airflow UI at: [http://localhost:8080](http://localhost:8080)

## Technologies
- Python
- Apache Airflow
- Docker
- PostgreSQL
- Power BI

## Author
Hoang Khang – [hoangkhang.17jle@gmail.com](mailto:hoangkhang.17jle@gmail.com)
