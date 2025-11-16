#!/usr/bin/env python3
"""
Test script for Investment Calculator functions (without external dependencies)
"""

import math

# Define functions to test
def future_value(principal, rate, periods, compounding='annual'):
    compounding_periods = {
        'annual': 1,
        'semi-annual': 2,
        'quarterly': 4,
        'monthly': 12,
        'daily': 365,
        'continuous': None
    }

    if compounding == 'continuous':
        return principal * math.exp(rate * periods)
    else:
        n = compounding_periods.get(compounding, 1)
        return principal * (1 + rate/n)**(n * periods)

def compound_interest(principal, rate, periods, additional_contribution=0, contribution_frequency='annual'):
    if contribution_frequency == 'monthly':
        n = 12
        r = rate / 12
        t = periods * 12
    else:  # annual
        n = 1
        r = rate
        t = periods

    # Future value of initial principal
    fv_principal = principal * (1 + r)**t

    # Future value of annuity (regular contributions)
    if additional_contribution > 0:
        fv_contributions = additional_contribution * (((1 + r)**t - 1) / r)
    else:
        fv_contributions = 0

    total_value = fv_principal + fv_contributions
    total_contributions = principal + (additional_contribution * t)
    interest_earned = total_value - total_contributions

    return {
        'total_value': total_value,
        'total_contributions': total_contributions,
        'interest_earned': interest_earned,
        'return_percentage': (interest_earned / total_contributions) * 100
    }

def calculate_roi(initial_investment, final_value, holding_period_years=None):
    gain = final_value - initial_investment
    roi = (gain / initial_investment) * 100

    result = {
        'gain': gain,
        'roi_percentage': roi
    }

    if holding_period_years:
        annualized_roi = ((final_value / initial_investment)**(1/holding_period_years) - 1) * 100
        result['annualized_roi_percentage'] = annualized_roi

    return result

# Run tests
print("=" * 60)
print("TESTING INVESTMENT CALCULATOR")
print("=" * 60)

# Test 1: Future Value
print("\nTest 1: Future Value Calculation")
fv = future_value(10000, 0.07, 10, 'annual')
print(f"✓ Future Value (Annual): ${fv:,.2f}")
assert fv > 10000, "Future value should be greater than principal"
assert abs(fv - 19671.51) < 1, "Expected ~$19,671.51"

# Test 2: Compound Interest
print("\nTest 2: Compound Interest with Contributions")
ci = compound_interest(5000, 0.08, 20, 200, 'monthly')
print(f"✓ Total Value: ${ci['total_value']:,.2f}")
print(f"✓ Total Contributions: ${ci['total_contributions']:,.2f}")
print(f"✓ Interest Earned: ${ci['interest_earned']:,.2f}")
assert ci['total_value'] > ci['total_contributions'], "Total value should exceed contributions"

# Test 3: ROI
print("\nTest 3: ROI Calculation")
roi = calculate_roi(15000, 22500, 3)
print(f"✓ ROI: {roi['roi_percentage']:.2f}%")
print(f"✓ Annualized ROI: {roi['annualized_roi_percentage']:.2f}%")
assert roi['gain'] == 7500, "Gain should be 7500"
assert roi['roi_percentage'] == 50.0, "ROI should be 50%"

# Test 4: Different compounding frequencies
print("\nTest 4: Compounding Frequency Comparison")
principal = 10000
rate = 0.07
years = 10
fv_annual = future_value(principal, rate, years, 'annual')
fv_monthly = future_value(principal, rate, years, 'monthly')
fv_continuous = future_value(principal, rate, years, 'continuous')
print(f"✓ Annual: ${fv_annual:,.2f}")
print(f"✓ Monthly: ${fv_monthly:,.2f}")
print(f"✓ Continuous: ${fv_continuous:,.2f}")
assert fv_continuous > fv_monthly > fv_annual, "More frequent compounding should yield higher returns"

print("\n" + "=" * 60)
print("ALL TESTS PASSED ✓")
print("=" * 60)
print("\nNote: This calculator is designed for Jupyter notebooks where")
print("pandas and numpy are typically pre-installed (e.g., Google Colab).")
