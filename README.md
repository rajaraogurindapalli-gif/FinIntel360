# FinIntel 360: Autonomous Risk, Macro Stress-Testing & Treasury Intelligence Platform

**Description**  
End-to-end enterprise FinTech decision-intelligence platform built on Microsoft Fabric OneLake, Power BI Direct Lake, and an Autonomous ReAct + RAG AI Copilot. It unifies real-time payment fraud surveillance, macroeconomic Monte Carlo Value-at-Risk (VaR) stress-testing, and Mixed-Integer Linear Programming (MILP) working-capital optimization into a closed-loop executive workflow that turns alerts into prescriptive, regulatory-compliant actions.

## Tech Stack
- **Microsoft Fabric** (OneLake medallion lakehouse: Bronze → Silver → Gold)
- **Power BI Direct Lake** (zero-import executive dashboards with dynamic URL handoff)
- **Python** (Streamlit, data processing, ML pipelines)
- **Machine Learning**: XGBoost + Autoencoder hybrid ensemble for fraud detection
- **Optimization**: Mixed-Integer Linear Programming (MILP) for treasury
- **Simulation**: Monte Carlo VaR (10,000 paths)
- **AI Copilot**: ReAct + RAG (Streamlit + Groq / Azure OpenAI, TF-IDF SEC/FinCEN)
- Notebooks for end-to-end lakehouse and model development

## Executive Business Impact

| Domain | Baseline / Legacy State | FinIntel 360 Target Architecture | Quantified Business Impact |
| :--- | :--- | :--- | :--- |
| **Fraud & AML Surveillance** | Static rule thresholds with high false-positive friction | Hybrid Ensemble (XGBoost + Autoencoder) on OneLake Gold | **99.66% Recall**, **0.00% FPR**, isolating **$12.06B** in P1 critical exposure |
| **Treasury Liquidity Optimization** | **$320.0M** unallocated idle cash in zero-yield buffers | MILP Optimization under Basel III LCR ($85M floor, 35% cap) | **+$9.02M** annual risk-free yield uplift across ON RRP, 3M T-Bills & Sweeps |
| **Macro Stress-Testing & VaR** | Static quarterly spreadsheet projections | 10,000-path Monte Carlo VaR across Fed Funds & CPI regimes | Quantified **-$21.23M** 95% Quarterly VaR across Baseline, Hawkish & Dovish shocks |
| **Executive Investigation Loop** | Manual SQL lookups across disconnected BI and compliance tools | Power BI Direct Lake Web URL Handoff → ReAct + SEC/FinCEN RAG | **One-click alert-to-SAR memo** generation with regulatory citations |

## End-to-End Architecture
(Architecture diagram preserved)

## Executive Visual Showcase

### 1. Executive C-Suite Command Center (Power BI Direct Lake)
![Executive C-Suite Command Center](Assets/Executive%20C-Suite%20Command%20Center.png)

### 2. Real-Time Fraud & AML Surveillance (With Dynamic Copilot URL Handoff)
![Real-Time Fraud & AML Surveillance](Assets/Real-Time%20Fraud%20%26%20AML%20Surveillance.png)

### 3. Macro Stress-Testing & Monte Carlo VaR
![Macro Stress-Testing & Monte Carlo VaR](Assets/Macro%20Stress-Testing%20%26%20Monte%20Carlo%20VaR.png)

### 4. Working Capital MILP Optimizer (`+$9.02M` Annual Yield Uplift)
![Capital MILP Optimizer](Assets/Capital%20MLP%20Optimizer.png)

## Repository Structure

```text
FinIntel360/
├── app_finintel_copilot.py
├── Notebooks/
│   ├── NOTEBOOK 01_ BRONZE INGESTION ...
│   ├── Notebook_02_Silver_Feature_Engineering.ipynb
│   ├── Notebook_03_Gold_Star_Schema.ipynb
│   ├── Notebook_04_Predictive_ML_and_Governance.ipynb
│   ├── Notebook_05_Prescriptive_Treasury_MILP.ipynb
│   └── Notebook_06_Export_Copilot_Context.ipynb
├── CopilotData/
├── Assets/
├── FinIntel 360 Master Project Specification.pdf
├── requirements.txt
└── README.md
```
