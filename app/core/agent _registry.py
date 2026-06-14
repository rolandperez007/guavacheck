from app.agents.listing_agent import ListingAgent
from app.agents.mortgage_agent import MortgageAgent

AGENTS = {"property_search": ListingAgent(), "mortgage": MortgageAgent()}
