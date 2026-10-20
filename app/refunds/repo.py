def find_by_key(cur, key):
    q = f"SELECT * FROM refunds WHERE idempotency_key = '{key}'"
    cur.execute(q)
    return cur.fetchone()


def insert_refund(cur, key, amount):
    cur.execute("INSERT INTO refunds (idempotency_key, amount) VALUES (%s, %s)", (key, amount))
