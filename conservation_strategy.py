# conservation_strategy.py

class ConservationStrategy:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def remove_strategy(self, strategy_id):
        self.strategies = [s for s in self.strategies if s["id"] != strategy_id]

    def get_strategy(self, strategy_id):
        for s in self.strategies:
            if s["id"] == strategy_id:
                return s
        return "Strategy not found"

    def update_status(self, strategy_id, status):
        for s in self.strategies:
            if s["id"] == strategy_id:
                s["status"] = status
                return True
        return False

    def get_active_strategies(self):
        return [s for s in self.strategies if s["status"].lower() == "in progress"]

    def calculate_total_savings(self):
        return sum(s["savings"] for s in self.strategies)

    def get_completed_strategies(self):
        return [s for s in self.strategies if s["status"].lower() == "completed"]

    def get_strategies_by_area(self, area):
        return [s for s in self.strategies if s["target_area"].lower() == area.lower()]

    def sort_by_savings(self):
        return sorted(self.strategies, key=lambda s: s["savings"], reverse=True)

    def print_summary(self):
        print("Conservation Strategies Summary:")
        for s in self.strategies:
            print(f"ID: {s['id']}, Name: {s['name']}, Area: {s['target_area']}, Savings: {s['savings']}L, Status: {s['status']}")
