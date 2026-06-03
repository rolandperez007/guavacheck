class MortgageAgent:

    def calculate(
        self,
        property_price,
        down_payment,
        annual_interest,
        years
    ):

        loan_amount = property_price - down_payment

        monthly_rate = annual_interest / 100 / 12

        months = years * 12

        if monthly_rate == 0:
            monthly_payment = loan_amount / months

        else:
            monthly_payment = (
                loan_amount *
                monthly_rate *
                ((1 + monthly_rate) ** months)
            ) / (
                ((1 + monthly_rate) ** months) - 1
            )

        total_paid = monthly_payment * months

        total_interest = total_paid - loan_amount

        return {
            "loan_amount": round(loan_amount, 2),
            "monthly_payment": round(monthly_payment, 2),
            "total_interest": round(total_interest, 2)
        }