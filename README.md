# saas-churn-revenue-pipeline
Automated data ingestion pipeline and SQL analytics engine tracking SaaS subscription billing events, involuntary payment churn, and recoverable recurring revenue.
# Micro-SaaS Subscription Churn & Revenue Recovery Pipeline

An automated data pipeline and SQL analytics engine that ingests simulated SaaS billing transactions, tracks involuntary payment failures, and identifies at-risk Monthly Recurring Revenue (MRR).

## 📌 Overview
Subscription companies lose up to 10-20% of revenue not because users want to cancel, but because of involuntary churn (expired cards, gateway timeouts, insufficient funds). This pipeline simulates real-world payment event transactions, stores them in an SQLite relational database, and runs financial SQL queries to isolate recoverable revenue.

## 🛠 Tech Stack
- **Language:** Python 3
- **Libraries:** `pandas`, `sqlite3`, `uuid`, `datetime`
- **Database:** SQLite
- **Target Roles:** Data Analyst, Financial/Revenue Analyst, Data Engineer, Python Developer

## 🚀 Key Features
- **Transactional Event Ingestion:** Ingests dynamic billing event streams across subscription tiers (`Basic`, `Pro`, `Enterprise`).
- **Involuntary vs. Voluntary Churn Analysis:** Distinguishes active user cancellations from technical payment failures.
- **Dunning Intelligence:** Aggregates recoverable ARR/MRR and pinpoints high-value enterprise accounts requiring automated payment retry triggers.

## 💻 How to Run Locally

1. Clone repository:
   ```bash
   git clone [https://github.com/saiananduttez/saas-churn-revenue-pipeline.git](https://github.com/saiananduttez/saas-churn-revenue-pipeline.git)
   cd saas-churn-revenue-pipeline
