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

FinIntel360/
├── app_finintel_copilot.py                # Streamlit ReAct multi-tool agent & TF-IDF SEC/FinCEN RAG engine
├── notebooks/
│   └── 01_finintel_medallion_etl_ml_milp.ipynb  # Microsoft Fabric PySpark ETL, Hybrid ML, MC VaR & SciPy MILP
├── CopilotData/
│   ├── top_p1_fraud_alerts.json           # Gold Lakehouse P1 critical alert snapshot for local Copilot inference
│   ├── treasury_milp_plan.json            # Optimal MILP allocation schedule (+$9.02M yield uplift)
│   └── peer_financials_benchmark.json     # Quarterly peer benchmark dataset (APEX, PYPL, XYZ, FI)
├── assets/                                # Dashboard & ReAct Copilot screenshots
├── requirements.txt                       # Python dependencies
├── .gitignore                             # Excludes virtual environments, caches, and secret files
└── README.md

## Executive Visual Showcase

### 1. Executive C-Suite Command Center (Power BI Direct Lake)
![Executive C-Suite Command Center](assets/page1_command_center.png)

### 2. Real-Time Fraud & AML Surveillance (With Dynamic Copilot URL Handoff)
![Real-Time Fraud & AML Surveillance](assets/page2_fraud_surveillance.png)

### 3. Autonomous ReAct + RAG Copilot Investigation (`tx_id=4440`)
![Autonomous ReAct Copilot Memo](assets/copilot_react_memo.png)

### 4. Macro Stress-Testing & Monte Carlo VaR
![Macro Stress-Testing & Monte Carlo VaR](assets/page3_macro_var.png)

### 5. Working Capital MILP Optimizer (`+$9.02M` Annual Yield Uplift)
![Capital MILP Optimizer](assets/page4_treasury_milp.png)