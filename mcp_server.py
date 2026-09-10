import sys
import json
from client import TCCEngine

def main():
    tcc = TCCEngine()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "try":
            ok = tcc.try_reserve(params.get("tx_id"), params.get("component"), params.get("amount", 1), params.get("balance", 10))
            res = {"success": ok}
        elif method == "confirm":
            res = {"confirmed": tcc.confirm(params.get("tx_id"))}
        elif method == "cancel":
            res = {"cancelled": tcc.cancel(params.get("tx_id"))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
