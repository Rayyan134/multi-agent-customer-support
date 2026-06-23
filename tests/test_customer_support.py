from agents.customer_support import  CustomerSupportAgent

agent = CustomerSupportAgent()

queries = [
    "Is the iPhone 15 Pro in stock?",
    "How long does shipping to Germany take?",
    "Do you sell gaming chairs?"
]

for query in queries:
    print(f"\nUser: {query}")
    print(f"Agent: {agent.handle_query(query)}")