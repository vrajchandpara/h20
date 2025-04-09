# treatment_plant.py

class TreatmentPlant:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def remove_plant(self, plant_id):
        self.plants = [p for p in self.plants if p["id"] != plant_id]

    def get_pending_plants(self):
        return [p for p in self.plants if p["status"].lower() == "pending"]

    def get_operational_plants(self):
        return [p for p in self.plants if p["status"].lower() == "operational"]

    def update_status(self, plant_id, new_status):
        for p in self.plants:
            if p["id"] == plant_id:
                p["status"] = new_status
                return True
        return False

    def get_total_treatment_capacity(self):
        return sum(p["capacity"] for p in self.plants)

    def get_plants_by_location(self, location):
        return [p for p in self.plants if p["location"].lower() == location.lower()]

    def sort_by_capacity(self):
        return sorted(self.plants, key=lambda x: x["capacity"], reverse=True)

    def get_plant(self, plant_id):
        for p in self.plants:
            if p["id"] == plant_id:
                return p
        return None

    def print_summary(self):
        print("Treatment Plant Summary:")
        for p in self.plants:
            print(f"ID: {p['id']}, Location: {p['location']}, Capacity: {p['capacity']}L/day, Status: {p['status']}")
