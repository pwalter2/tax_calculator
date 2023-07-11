from dataclasses import dataclass

# Reference: https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2023

@dataclass
class MarginalTaxRate:
    income_threshold: int
    tax_factor: float


# could combine the two into one class
# that takes annual_income as init value
def calculate_taxes(annual_income: int): 
    # tax year 2023 adjustments
    marginal_tax_rates = [
        MarginalTaxRate(11_000, 0.1),
        MarginalTaxRate(44_725, 0.12),
        MarginalTaxRate(95_375, 0.22),
        MarginalTaxRate(182_100, 0.24),
        MarginalTaxRate(231_250, 0.32),
        MarginalTaxRate(578_125, 0.35),
        MarginalTaxRate(annual_income, 0.37),  # will force difference to below zero
    ]
    i = 0
    tax_buckets = []
    while annual_income > 0:
        next_tax = marginal_tax_rates[i]
        if annual_income - next_tax.income_threshold > 0:
            tax_buckets.append(next_tax.income_threshold * next_tax.tax_factor)
        else:
            tax_buckets.append(annual_income * next_tax.tax_factor)
        annual_income -= next_tax.income_threshold
        i += 1

    return(tax_buckets)
    