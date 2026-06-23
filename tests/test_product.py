from agents.product_catalog import ProductCatalogAgent

catalog = ProductCatalogAgent()

result = catalog.get_product_info(
    "Is the iPhone 15 Pro in stock?"
)

print(result)