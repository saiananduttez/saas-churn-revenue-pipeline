import sqlite3
import pandas as pd

def run_saas_metrics(db_name="saas_metrics.db"):
    conn = sqlite3.connect(db_name)
    
    # 1. Total Monthly Recurring Revenue (MRR) & Lost Revenue
    rev_query = """
    SELECT 
        event_type,
        COUNT(*) AS transaction_count,
        ROUND(SUM(amount), 2) AS total_revenue_usd
    FROM billing_events
    GROUP BY event_type;
    """
    
    # 2. Involuntary Churn Breakdown (Root cause of failed transactions)
    fail_query = """
    SELECT 
        failure_reason,
        COUNT(*) AS failure_count,
        ROUND(SUM(amount), 2) AS recoverable_revenue_usd
    FROM billing_events
    WHERE event_type = 'payment_failed'
    GROUP BY failure_reason
    ORDER BY recoverable_revenue_usd DESC;
    """
    
    # 3. Top High-Value At-Risk Customers
    risk_query = """
    SELECT 
        customer_name,
        plan_name,
        ROUND(SUM(amount), 2) AS at_risk_amount
    FROM billing_events
    WHERE event_type = 'payment_failed'
    GROUP BY customer_name, plan_name
    ORDER BY at_risk_amount DESC
    LIMIT 5;
    """

    df_rev = pd.read_sql_query(rev_query, conn)
    df_fail = pd.read_sql_query(fail_query, conn)
    df_risk = pd.read_sql_query(risk_query, conn)
    conn.close()
    
    print("\n========================================================")
    print("           REVENUE & CHURN BREAKDOWN                    ")
    print("========================================================")
    print(df_rev.to_string(index=False))
    
    print("\n========================================================")
    print("     INVOLUNTARY CHURN REASON (PAYMENT FAILURES)        ")
    print("========================================================")
    print(df_fail.to_string(index=False))

    print("\n========================================================")
    print("          TOP AT-RISK HIGH-VALUE CUSTOMERS              ")
    print("========================================================")
    print(df_risk.to_string(index=False))

if __name__ == "__main__":
    run_saas_metrics()