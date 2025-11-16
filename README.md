# FRTB - Fundamental Review of Trading Book

## Overview

This repository contains comprehensive regulatory capital calculation modules for banking compliance under Basel III FRTB (Fundamental Review of the Trading Book) framework

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


## Module Structure

All risk calculation modules follow a consistent pattern:
1. **Input Phase** - Load portfolio data and risk factors
2. **Preparation** - Net sensitivities by risk factor
3. **Risk Weights** - Apply regulatory risk weights
4. **Intra-Bucket Aggregation** - Calculate bucket-level capital
5. **Cross-Bucket Aggregation** - Combine buckets into final capital
6. **Scenario Analysis** - Run correlation scenarios (high/medium/low)
7. **Output** - Final capital requirement
