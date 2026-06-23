from agents.shipping import ShippingAgent

shipping = ShippingAgent()

result = shipping.get_shipping_info(
    "How long does shipping to Germany take?"
)

print(result)