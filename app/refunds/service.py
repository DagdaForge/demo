from app.refunds.repo import find_by_key, insert_refund


def refund(cur, key, amount):
    existing = find_by_key(cur, key)
    if existing:
        return {"status": "duplicate"}
    insert_refund(cur, key, amount)
    return {"status": "created"}
