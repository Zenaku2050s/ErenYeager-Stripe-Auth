import string
import random
import sqlite3

# RANDOM GEN FUNCTION
def gcgenfunc(length=4):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

# Insert registration data
def insert_pm(gc):
    with sqlite3.connect('plugins/xcc_db/giftcard.db') as conn:
        db = conn.cursor()
        db.execute("INSERT INTO gc (id, status, plan) VALUES (?, ?, ?)", (gc, 'ACTIVE', 'PREMIUM'))
        conn.commit()

def insert_plan1(gc):
    with sqlite3.connect('plugins/xcc_db/giftcard.db') as conn:
        db = conn.cursor()
        db.execute("INSERT INTO gc (id, status, plan) VALUES (?, ?, ?)", (gc, 'ACTIVE', 'PLAN1'))
        conn.commit()

def insert_plan2(gc):
    with sqlite3.connect('plugins/xcc_db/giftcard.db') as conn:
        db = conn.cursor()
        db.execute("INSERT INTO gc (id, status, plan) VALUES (?, ?, ?)", (gc, 'ACTIVE', 'PLAN2'))
        conn.commit()

def insert_plan3(gc):
    with sqlite3.connect('plugins/xcc_db/giftcard.db') as conn:
        db = conn.cursor()
        db.execute("INSERT INTO gc (id, status, plan) VALUES (?, ?, ?)", (gc, 'ACTIVE', 'PLAN3'))
        conn.commit()

# Fetch info from gc
def getgc(gc):
    with sqlite3.connect('plugins/xcc_db/giftcard.db') as conn:
        db = conn.cursor()
        db.execute("SELECT * FROM gc WHERE id=?", (gc,))
        info = db.fetchone()
        return info

# Fetch all info from table
def getallgc():
    with sqlite3.connect('plugins/xcc_db/giftcard.db') as conn:
        db = conn.cursor()
        db.execute("SELECT * FROM gc")
        info = db.fetchall()
        return info

# Update data in the table
def updategc(gc):
    with sqlite3.connect('plugins/xcc_db/giftcard.db') as conn:
        db = conn.cursor()
        db.execute("UPDATE gc SET status='USED' WHERE id=?", (gc,))
        conn.commit()
      
