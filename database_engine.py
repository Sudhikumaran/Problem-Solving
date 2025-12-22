import threading
import bisect


data = {}
index = []
tx_stack = []
lock = threading.RLock()


def put(key, val):
    with lock:
        old = data.get(key)

        if tx_stack:
            tx_stack[-1].append((key, old))

        if key not in data:
            bisect.insort(index, key)

        data[key] = val
        print("PUT ->", key, "=", val)


def get(key):
    with lock:
        val = data.get(key)
        print("GET ->", key, "=", val)
        return val


def delete(key):
    with lock:
        if key not in data:
            print("Delete ->", key, "not found")
            return

        if tx_stack:
            tx_stack[-1].append((key, data[key]))

        del data[key]
        index.remove(key)
        print("Delete ->", key)


def begin_transaction():
    with lock:
        tx_stack.append([])
        print("Transaction Begin")


def commit():
    with lock:
        if not tx_stack:
            print("No Transaction To Commit")
            return

        tx_stack.pop()
        print("Transaction Commit")


def rollback():
    with lock:
        if not tx_stack:
            print("No Transaction To RollBack")
            return

        logs = tx_stack.pop()

        for key, old_val in reversed(logs):
            if old_val is None:
                if key in data:
                    del data[key]
                    index.remove(key)
            else:
                if key not in data:
                    bisect.insort(index, key)
                data[key] = old_val

        print("Transaction RollBack")


def show_index():
    print("Index ->", index)



put("a", 10)
put("b", 20)

begin_transaction()
put("a", 99)
delete("b")
get("a")

rollback()

get("a")
get("b")
show_index()
