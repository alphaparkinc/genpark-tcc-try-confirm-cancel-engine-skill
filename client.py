class TCCEngine:
    """
    Try-Confirm-Cancel (TCC) Distributed Business Transaction Engine.
    """
    def __init__(self):
        self.reservations = {}
        self.confirmed = {}

    def try_reserve(self, tx_id, component, amount, available_balance):
        if available_balance >= amount:
            if tx_id not in self.reservations:
                self.reservations[tx_id] = {}
            self.reservations[tx_id][component] = amount
            return True
        return False

    def confirm(self, tx_id):
        if tx_id in self.reservations:
            self.confirmed[tx_id] = self.reservations.pop(tx_id)
            return True
        return False

    def cancel(self, tx_id):
        if tx_id in self.reservations:
            del self.reservations[tx_id]
            return True
        return False
