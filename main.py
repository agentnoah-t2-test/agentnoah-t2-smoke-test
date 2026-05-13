"""
Tiny FastAPI demo with one DELIBERATE SQL injection bug.
AgentNoah should catch the bug at line ~17 (P1 security finding).
"""
import sqlite3
import threading
from fastapi import FastAPI

app = FastAPI()
db = sqlite3.connect("users.db", check_same_thread=False)
db_lock = threading.Lock()


@app.get("/user/{user_id}")
def get_user(user_id: str):
    # SEEDED BUG: SQL injection via f-string formatting on user-controlled input.
    # An attacker can pass user_id="1 OR 1=1" and dump the table.
    query = f"SELECT * FROM users WHERE id = {user_id}"
    with db_lock:
        return db.execute(query).fetchall()


@app.get("/health")
def health():
    return {"status": "ok"}
# verify slice 5L cross-repo fetch
