def find_by_key(cur, key):
    cur.execute("SELECT * FROM refunds WHERE idempotency_key = %s", (key,))
    return cur.fetchone()


def insert_refund(cur, key, amount):
    cur.execute("INSERT INTO refunds (idempotency_key, amount) VALUES (%s, %s)", (key, amount))
