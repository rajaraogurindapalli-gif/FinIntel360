# FinIntel 360: Autonomous Risk, Macro Stress-Testing & Treasury Intelligence Platform

**FinIntel 360** is an end-to-end enterprise FinTech decision-intelligence platform engineered on **Microsoft Fabric OneLake**, **Power BI Direct Lake**, and an **Autonomous ReAct + RAG AI Copilot**. It unifies real-time payment fraud surveillance, macroeconomic Monte Carlo Value-at-Risk (VaR) stress-testing, and Mixed-Integer Linear Programming (MILP) working-capital optimization into a single closed-loop executive workflow.

---

## Executive Business Impact

| Domain | Baseline / Legacy State | FinIntel 360 Target Architecture | Quantified Business Impact |
| :--- | :--- | :--- | :--- |
| **Fraud & AML Surveillance** | Static rule thresholds with high false-positive friction | Hybrid Ensemble (XGBoost + Autoencoder) on OneLake Gold | **99.66% Recall**, **0.00% FPR**, isolating **$12.06B** in P1 critical exposure |
| **Treasury Liquidity Optimization** | **$320.0M** unallocated idle cash in zero-yield buffers | MILP Optimization under Basel III LCR ($85M floor, 35% cap) | **+$9.02M** annual risk-free yield uplift across ON RRP, 3M T-Bills & Sweeps |
| **Macro Stress-Testing & VaR** | Static quarterly spreadsheet projections | 10,000-path Monte Carlo VaR across Fed Funds & CPI regimes | Quantified **-$21.23M** 95% Quarterly VaR across Baseline, Hawkish & Dovish shocks |
| **Executive Investigation Loop** | Manual SQL lookups across disconnected BI and compliance tools | Power BI Direct Lake Web URL Handoff $\rightarrow$ ReAct + SEC/FinCEN RAG | **One-click alert-to-SAR memo** generation with regulatory citations |

---

## End-to-End Architecture

```text
+-----------------------------------------------------------------------------------+
| 1. MICROSOFT FABRIC ONELAKE (MEDALLION LAKEHOUSE: FinIntel_OneLake)               |
|                                                                                   |
|  [Bronze Layer]  -->  [Silver Layer]  -->  [Gold Star Schema & ML/OR Tables]      |
|  - SEC 10-K/Q         - Cleansed           - gold_dim_company / gold_dim_channel  |
|  - FRED Macro         - Feature Eng.       - gold_fact_corporate_financials       |
|  - Payment Txns       - 1H Velocity        - gold_fact_fraud_scored (Hybrid ML)   |
|  - Treasury Rates     - Balance Errors     - gold_fact_revenue_forecast (MC VaR)  |
|                                            - gold_fact_treasury_optimization      |
+-----------------------------------------+-----------------------------------------+
                                          |
                     Direct Lake Framing  |  Gold JSON Snapshots
                     (Zero-Import Query)  |  (F:\FinIntel360\CopilotData)
                                          v
+-----------------------------------+     +-----------------------------------------+
| 2. POWER BI DIRECT LAKE DASHBOARD |     | 3. AUTONOMOUS REACT & RAG COPILOT       |
|    (FinIntel360_Executive_Dashboard)    |    (Streamlit + Groq / Azure OpenAI)    |
|                                   |     |                                         |
|  - Page 1: C-Suite Command Center |     |  - Tool 1: query_fraud_telemetry        |
|  - Page 2: Fraud & AML Table  ----+---->|  - Tool 2: query_treasury_and_peers     |
|            (Dynamic ?tx_id= URL)  |     |  - Tool 3: search_sec_and_regulatory_rag|
|  - Page 3: Macro Stress & VaR     |     |  - Output: Executive Prescriptive Memo  |
|  - Page 4: Capital MILP Optimizer |     |            & FinCEN SAR Action Plan     |
+-----------------------------------+     +-----------------------------------------+

## Executive Visual Showcase

### 1. Executive C-Suite Command Center (Power BI Direct Lake)
![Executive C-Suite Command Center](Assets/Executive%20C-Suite%20Command%20Center.png)

### 2. Real-Time Fraud & AML Surveillance (With Dynamic Copilot URL Handoff)
![Real-Time Fraud & AML Surveillance](Assets/Real-Time%20Fraud%20%26%20AML%20Surveillance.png)

### 3. Macro Stress-Testing & Monte Carlo VaR
![Macro Stress-Testing & Monte Carlo VaR](Assets/Macro%20Stress-Testing%20%26%20Monte%20Carlo%20VaR.png)

### 4. Working Capital MILP Optimizer (`+$9.02M` Annual Yield Uplift)
![Capital MILP Optimizer](Assets/Capital%20MLP%20Optimizer.png)

---

## Repository Structure

```text
FinIntel360/
├── app_finintel_copilot.py                                                  # Streamlit ReAct multi-tool agent & TF-IDF SEC/FinCEN RAG engine
├── Notebooks/
│   ├── NOTEBOOK 01_ BRONZE INGESTION (FRED MACRO + SEC EDGAR + SYNTHETIC APEX).ipynb
│   ├── Notebook_02_Silver_Feature_Engineering.ipynb
│   ├── Notebook_03_Gold_Star_Schema.ipynb
│   ├── Notebook_04_Predictive_ML_and_Governance.ipynb
│   ├── Notebook_05_Prescriptive_Treasury_MILP.ipynb
│   └── Notebook_06_Export_Copilot_Context.ipynb
├── CopilotData/
│   ├── top_p1_fraud_alerts.json                                             # Gold Lakehouse P1 critical alert snapshot for local Copilot inference
│   ├── treasury_milp_plan.json                                              # Optimal MILP allocation schedule (+$9.02M yield uplift)
│   └── peer_financials_benchmark.json                                       # Quarterly peer benchmark dataset (APEX, PYPL, XYZ, FI)
├── Assets/                                                                  # Power BI Direct Lake .pbix & dashboard screenshots
├── FinIntel 360 Master Project Specification.pdf                            # Full architectural & functional specification
├── requirements.txt                                                         # Python dependencies
├── .gitignore                                                               # Excludes raw archives, caches, and secret files
└── README.md
