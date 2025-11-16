# FRTB - Fundamental Review of Trading Book

## Overview

This repository contains comprehensive regulatory capital calculation modules for banking compliance under Basel III FRTB (Fundamental Review of the Trading Book) framework, along with supplementary investment calculation tools.

## Investment Calculator

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Levan-Danelia/FRTB/blob/main/FRTB_Investment_Calculator.ipynb)

### FRTB_Investment_Calculator.ipynb

Comprehensive investment calculation module providing:
- **Future Value (FV)** - Calculate future value with multiple compounding frequencies
- **Present Value (PV)** - Discount future cash flows to present value
- **Compound Interest** - Calculate returns with optional regular contributions
- **Return on Investment (ROI)** - Total and annualized return calculations
- **Annuity Calculations** - Future and present values of annuities
- **Portfolio Analysis** - Multi-asset portfolio performance tracking

**Key Features:**
- Support for annual, semi-annual, quarterly, monthly, daily, and continuous compounding
- Regular contribution modeling for savings plans
- Portfolio-level analysis with detailed asset breakdowns
- Ready-to-use examples and custom calculation templates

## FRTB Risk Calculation Modules

### Commodity Risk (CM)
- **FRTB_CMDL.ipynb** - Commodity Delta Risk
- **FRTB_CMCV.ipynb** - Commodity Curvature Risk
- **FRTB_CMVG.ipynb** - Commodity Vega Risk

### Credit Risk (CR)
- **CRDL_Non_Securitization.ipynb** - Credit Delta (Non-Sec)
- **CRDL_Securitization_ACTP.ipynb** - Credit Delta (Sec ACTP)
- **CRDL_Securitization_Non_ACTP.ipynb** - Credit Delta (Sec Non-ACTP)
- **CRCV_Non_Securitization.ipynb** - Credit Curvature (Non-Sec)
- **CRCV_Securitization_ACTP.ipynb** - Credit Curvature (Sec ACTP)
- **CRCV_Securitization_Non_ACTP.ipynb** - Credit Curvature (Sec Non-ACTP)
- **CRVG_Non_Securitization.ipynb** - Credit Vega (Non-Sec)
- **CRVG_Securitization_ACTP.ipynb** - Credit Vega (Sec ACTP)
- **CRVG_Securitization_Non_ACTP.ipynb** - Credit Vega (Sec Non-ACTP)

### Equity Risk (EQ)
- **FRTB_EQDL.ipynb** - Equity Delta Risk
- **FRTB_EQCV.ipynb** - Equity Curvature Risk
- **FRTB_EQVG.ipynb** - Equity Vega Risk

### Foreign Exchange Risk (FX)
- **FRTB_FDXL.ipynb** - FX Delta Risk
- **FRTB_FXCV.ipynb** - FX Curvature Risk
- **FRTB_FXVG.ipynb** - FX Vega Risk

### Interest Rate Risk (IR)
- **FRTB_IRDL.ipynb** - Interest Rate Delta Risk
- **FRTB_IRCV.ipynb** - Interest Rate Curvature Risk
- **FRTB_IRVG.ipynb** - Interest Rate Vega Risk

### Other Risk Calculations
- **FRTB_DRC_*.ipynb** - Default Risk Charge (multiple variants)
- **FRTB_RRAO.ipynb** - Residual Risk Add-On

## Technology Stack

- **Python** - Primary programming language
- **pandas** - Data manipulation and aggregation
- **numpy** - Numerical calculations and matrix operations
- **Jupyter Notebook** - Interactive development environment
- **Google Colab** - Cloud-based execution support

## Usage

Each module is a standalone Jupyter notebook that can be:
1. Opened and executed locally with Jupyter
2. Run in Google Colab (click the Colab badge in each notebook)
3. Modified for specific calculation requirements

## Module Structure

All risk calculation modules follow a consistent pattern:
1. **Input Phase** - Load portfolio data and risk factors
2. **Preparation** - Net sensitivities by risk factor
3. **Risk Weights** - Apply regulatory risk weights
4. **Intra-Bucket Aggregation** - Calculate bucket-level capital
5. **Cross-Bucket Aggregation** - Combine buckets into final capital
6. **Scenario Analysis** - Run correlation scenarios (high/medium/low)
7. **Output** - Final capital requirement

## Getting Started

```python
# Example: Using the Investment Calculator
import pandas as pd
import numpy as np

# Calculate future value
principal = 10000
rate = 0.07
years = 10
fv = future_value(principal, rate, years, 'annual')
print(f"Future Value: ${fv:,.2f}")
```

## License

This project is for educational and compliance purposes.

## Contributing

Contributions are welcome! Please ensure any new modules follow the established pattern and include comprehensive documentation.