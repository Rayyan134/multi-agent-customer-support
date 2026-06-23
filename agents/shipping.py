import json
from pathlib import Path


class ShippingAgent:
    def __init__(self):
        data_path = Path(__file__).parent.parent / "data" / "shipping.json"

        with open(data_path, "r", encoding="utf-8") as file:
            self.shipping_times = json.load(file)

    def get_shipping_info(self, query: str):
        """
        Search for a country mentioned in the user's query.
        Returns a shipping estimate or None.
        """
        query = query.lower()

        for country, estimate in self.shipping_times.items():
            if country.lower() in query:
                return {
                    "country": country,
                    "estimate": estimate
                }

        return None