# distribution_system.py

class DistributionSystem:
    def __init__(self):
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def remove_route(self, route_id):
        self.routes = [r for r in self.routes if r["id"] != route_id]

    def get_route(self, route_id):
        for r in self.routes:
            if r["id"] == route_id:
                return r
        return "Route not found"

    def update_flow_rate(self, route_id, new_flow_rate):
        for r in self.routes:
            if r["id"] == route_id:
                r["flow_rate"] = new_flow_rate
                return True
        return False

    def get_total_distributed_volume(self):
        return sum(r["volume"] for r in self.routes)

    def get_routes_by_status(self, status):
        return [r for r in self.routes if r["status"].lower() == status.lower()]

    def get_routes_by_area(self, area):
        return [r for r in self.routes if r["area"].lower() == area.lower()]

    def get_high_loss_routes(self, threshold):
        return [r for r in self.routes if r["loss"] > threshold]

    def calculate_average_loss(self):
        if not self.routes:
            return 0
        return sum(r["loss"] for r in self.routes) / len(self.routes)

    def print_summary(self):
        print("Distribution System Summary:")
        for r in self.routes:
            print(f"ID: {r['id']}, Area: {r['area']}, Volume: {r['volume']}L, Flow Rate: {r['flow_rate']}L/min, Loss: {r['loss']}L, Status: {r['status']}")
