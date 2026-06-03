from app.agents.swarm.mortgage_agent import MortgageAgent

agent = MortgageAgent()

result = agent.calculate(
    property_price=150000000,
    down_payment=30000000,
    annual_interest=18,
    years=20
)

print(result)