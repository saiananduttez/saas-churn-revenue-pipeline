# Micro-SaaS Subscription Churn & Revenue Recovery Pipeline

An automated data pipeline and SQL analytics engine that ingests simulated SaaS billing transactions, tracks involuntary payment failures, and identifies at-risk Monthly Recurring Revenue (MRR).

## Overview
Subscription-based software companies lose significant revenue not because customers choose to leave, but due to involuntary payment failures (such as expired credit cards, gateway timeouts, and insufficient funds). This pipeline simulates production payment event streams, stores them in an SQLite relational database, and executes targeted SQL queries to isolate recoverable revenue and highlight at-risk accounts.

## Tech Stack
- Python 3
- pandas, sqlite3, uuid, datetime
- SQLite Relational Database

## Key Features
- Transactional Event Ingestion: Ingests dynamic billing event streams across subscription tiers (Basic Tier, Pro Tier, Enterprise Tier).
- Involuntary vs. Voluntary Churn Analysis: Distinguishes active user cancellations from technical payment failures.
- Dunning Intelligence: Aggregates recoverable ARR/MRR and pinpoints high-value enterprise accounts requiring automated payment retry triggers.

## How to Run Locally

Clone or download the repository:
```bash
git clone https://github.com/saiananduttez/saas-churn-revenue-pipeline.git
cd saas-churn-revenue-pipeline
