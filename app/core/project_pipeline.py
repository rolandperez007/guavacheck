from app.core.project_classifier import ProjectClassifier
from app.core.design_brain import DesignBrain
from app.core.boq_engine import BOQEngine
from app.core.cost_engine import CostEngine
from app.core.timeline_engine import TimelineEngine
from app.core.investment_brain import InvestmentBrain
from app.core.payment_router import PaymentRouter


class PaymentBrain:
    def __init__(self):
        self.router = PaymentRouter()

    def generate_invoice(self, cost, user):
        return {
            "amount": cost["estimated_cost"],
            "currency": cost.get("currency", "USD"),
            "user": user,
        }

    def process_payment(self, cost, user):
        invoice = self.generate_invoice(cost, user)

        return self.router.charge(
            amount=invoice["amount"], currency=invoice["currency"], user=invoice["user"]
        )


class ProjectPipeline:
    def run(self, query):
        project = ProjectClassifier.classify(query)

        design = DesignBrain().generate(project)

        boq = BOQEngine().generate(design)

        cost = CostEngine().estimate(boq)

        timeline = TimelineEngine().generate(project["asset_type"])

        investment = InvestmentBrain().analyze(cost)
        payment = PaymentRouter().charge(
            amount=cost["estimated_cost"],
            currency=cost["currency"],
            user={"id": "system", "country": project.get("country", "US")},
        )

        return {
            "project": project,
            "design": design,
            "boq": boq,
            "cost": cost,
            "timeline": timeline,
            "investment": investment,
            "payment": payment,
        }
