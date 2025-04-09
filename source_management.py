# source_management.py

class SourceManagement:
    def __init__(self):
        self.sources = []

    def add_source(self, source):
        self.sources.append(source)

    def remove_source(self, source_id):
        self.sources = [s for s in self.sources if s["id"] != source_id]

    def get_active_sources(self):
        return [s for s in self.sources if s["status"] == "Active"]

    def update_level(self, source_id, new_level):
        for s in self.sources:
            if s["id"] == source_id:
                s["current_level"] = new_level
                return True
        return False

    def check_quality(self, source_id):
        for s in self.sources:
            if s["id"] == source_id:
                return s["quality"]
        return "Source not found"

    def get_total_capacity(self):
        return sum(s["capacity"] for s in self.sources)

    def get_available_water(self):
        return sum(s["current_level"] for s in self.sources)

    def deactivate_source(self, source_id):
        for s in self.sources:
            if s["id"] == source_id:
                s["status"] = "Inactive"
                return True
        return False

    def get_sources_by_type(self, source_type):
        return [s for s in self.sources if s["type"] == source_type]

    def print_summary(self):
        print("Source Summary:")
        for s in self.sources:
            print(f"ID: {s['id']}, Type: {s['type']}, Level: {s['current_level']}/{s['capacity']}, Quality: {s['quality']}, Status: {s['status']}")
