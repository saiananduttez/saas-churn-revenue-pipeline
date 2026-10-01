import sqlite3
import random
import uuid
from datetime import datetime, timedelta
from database import init_db

# Clean professional customer names
CUSTOMER_NAMES = [
    "Aarav Sharma", "Priya Patel", "Vikram Malhotra", "Ananya Iyer",
    "Rohan Verma", "Sneha Kulkarni", "Karthik Nair", "Pooja Reddy",
    "David Miller", "Elena Rostova", "Marcus Vance", "Sarah Jenkins"
]

def generate_billing_events(n=120):
    """Simulates real-world SaaS subscription transactions and payment failures."""
    plans = {"Basic Tier": 19.0, "Pro Tier": 49.0, "Enterprise Tier": 199.0}
    event_types = ["payment_succeeded", "payment_failed", "subscription_cancelled"]
    failure_reasons = ["insufficient_funds", "card_expired", "bank_gateway_timeout"]
    
    events = []
    base_time = datetime.now() - timedelta(days=60)
    
    for i in range(n):
        plan = random.choice(list(plans.keys()))
        ev_type = random.choices(event_types, weights=[0.72, 0.18, 0.10])[0]
        f_reason = random.choice(failure_reasons) if ev_type == "payment_failed" else "None"
        cust_name = random.choice(CUSTOMER_NAMES)
        user_id = f"USR_{abs(hash(cust_name)) % 1000:03d}"
        
        event = (
            str(uuid.uuid4())[:8],
            cust_name,
            user_id,
            plan,
            plans[plan],
            ev_type,
            f_reason,
            (base_time + timedelta(hours=i * 12)).strftime("%Y-%m-%d %H:%M:%S")
        )
        events.append(event)
    return events

def ingest_events(events, db_name="saas_metrics.db"):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.executemany("""
    INSERT OR IGNORE INTO billing_events 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, events)
    conn.commit()
    conn.close()
    print(f"Success: Ingested {len(events)} subscription transactions into SQLite.")

if __name__ == "__main__":
    init_db()
    data = generate_billing_events(120)
    ingest_events(data)