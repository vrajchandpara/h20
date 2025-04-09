# usage_monitoring.py

class UsageMonitoring:
    def __init__(self):
        self.usage_data = []

    def add_usage_entry(self, entry):
        self.usage_data.append(entry)

    def remove_entry(self, usage_id):
        self.usage_data = [u for u in self.usage_data if u["id"] != usage_id]

    def get_entry(self, usage_id):
        for u in self.usage_data:
            if u["id"] == usage_id:
                return u
        return "Usage entry not found"

    def update_consumption(self, usage_id, new_amount):
        for u in self.usage_data:
            if u["id"] == usage_id:
                u["amount"] = new_amount
                return True
        return False

    def get_total_usage(self):
        return sum(u["amount"] for u in self.usage_data)

    def get_usage_by_user(self, user_id):
        return [u for u in self.usage_data if u["user_id"] == user_id]

    def get_usage_by_sector(self, sector):
        return [u for u in self.usage_data if u["sector"].lower() == sector.lower()]

    def get_high_consumers(self, threshold):
        return [u for u in self.usage_data if u["amount"] > threshold]

    def get_average_usage(self):
        if not self.usage_data:
            return 0
        return self.get_total_usage() / len(self.usage_data)

    def print_summary(self):
        print("Usage Monitoring Summary:")
        for u in self.usage_data:
            print(f"ID: {u['id']}, User: {u['user_id']}, Sector: {u['sector']}, Amount: {u['amount']}L")
