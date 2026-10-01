import sqlite3

def init_db(db_name="saas_metrics.db"):
    """Creates tables for users, plans, and transactional billing events."""
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS billing_events (
        event_id TEXT PRIMARY KEY,
        customer_name TEXT,
        user_id TEXT,
        plan_name TEXT,
        amount REAL,
        event_type TEXT,
        failure_reason TEXT,
        event_timestamp TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()