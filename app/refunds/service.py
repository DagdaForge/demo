from app.refunds.repo import insert_refund


def refund(cur, key, amount):
    insert_refund(cur, key, amount)
    return {"status": "created"}
