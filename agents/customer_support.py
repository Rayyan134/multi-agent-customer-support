from agents.product_catalog import ProductCatalogAgent
from agents.shipping import ShippingAgent
from agents.router import AgentRouter


class CustomerSupportAgent:
    def __init__(self):
        self.product_agent = ProductCatalogAgent()
        self.shipping_agent = ShippingAgent()
        self.router = AgentRouter()

    def handle_query(self, message: str) -> str:

        route = self.router.decide(message)

        if route == "product":
            product = self.product_agent.get_product_info(message)

            if product:
                stock_status = (
                    "currently in stock"
                    if product["stock"]
                    else "currently out of stock"
                )

                return f"{product['name']} costs {product['price']} and is {stock_status}."

            return "Product not found."

        elif route == "shipping":
            shipping = self.shipping_agent.get_shipping_info(message)

            if shipping:
                return f"Shipping to {shipping['country']} takes approximately {shipping['estimate']}."

            return "Shipping info not found."

        else:
            return "Sorry, I couldn't understand your request."