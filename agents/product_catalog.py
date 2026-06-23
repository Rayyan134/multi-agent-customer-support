import json
from pathlib import Path

class ProductCatalogAgent:

    def __init__(self):
        data_path = Path(__file__).parent.parent / "data" / "products.json"

        with open(data_path, "r", encoding="utf-8") as file:
            self.products = json.load(file)

    def get_product_info(self, query: str):
        """
        Search for a product by name
        Returns a dictionary if found, otherwise None
        """

        query = query.lower()

        for product in self.products:
            if product["name"].lower() in query:
                return product
            
        return None