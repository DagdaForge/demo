from app.refunds.service import refund


class Cur:
    def __init__(self):
        self.calls = []

    def execute(self, q, args=()):
        self.calls.append((q, args))


def test_refund_inserts():
    c = Cur()
    assert refund(c, "k1", 10) == {"status": "created"}
    assert len(c.calls) == 1
