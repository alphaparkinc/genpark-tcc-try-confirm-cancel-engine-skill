from client import TCCEngine

def main():
    print("=== Testing TCC (Try-Confirm-Cancel) Engine ===")
    tcc = TCCEngine()
    ok = tcc.try_reserve("order:101", "inventory", 2, available_balance=10)
    print("Try reserve inventory status:", ok)
    assert ok

    confirmed = tcc.confirm("order:101")
    print("Confirm commitment:", confirmed)
    assert confirmed
    assert "inventory" in tcc.confirmed["order:101"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
