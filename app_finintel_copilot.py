# ==============================================================================
# FININTEL 360: AUTONOMOUS REACT & RAG EXECUTIVE COPILOT (STREAMLIT)
# Save as: F:\FinIntel360\app_finintel_copilot.py
# ==============================================================================
import os
import json
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import AzureOpenAI, OpenAI

st.set_page_config(page_title="FinIntel 360 | Autonomous Risk & Treasury Copilot", layout="wide")

# ------------------------------------------------------------------------------
# 1. LOAD GOLD LAKEHOUSE SNAPSHOTS & REGULATORY/SEC RAG CORPUS
# ------------------------------------------------------------------------------
DATA_DIR = r"F:\FinIntel360\CopilotData"

@st.cache_data
def load_gold_snapshots():
    with open(os.path.join(DATA_DIR, "top_p1_fraud_alerts.json"), "r") as f:
        fraud_data = json.load(f)
    with open(os.path.join(DATA_DIR, "treasury_milp_plan.json"), "r") as f:
        treasury_data = json.load(f)
    with open(os.path.join(DATA_DIR, "peer_financials_benchmark.json"), "r") as f:
        peer_data = json.load(f)
    return fraud_data, treasury_data, peer_data

RAG_CORPUS = [
    {
        "doc_id": "SEC-PYPL-10K-MD&A",
        "source": "PayPal Holdings (PYPL) FY2025 Form 10-K - Item 7 MD&A",
        "text": "Transaction take rate compressed by 18 bps year-over-year driven by higher volume mix toward unbranded enterprise processing (Braintree) and increased cross-border FX hedging costs under elevated Federal Funds rates."
    },
    {
        "doc_id": "SEC-XYZ-10K-RISK",
        "source": "Block, Inc. (XYZ) Form 10-K - Item 1A Risk Factors",
        "text": "Instant off-ramp peer-to-peer transfers and Cash App liquidation rails face heightened scrutiny from FinCEN and state regulators regarding account takeover (ATO) and mule structuring rings. Rapid balance-draining transfers require automated pre-clearing holds."
    },
    {
        "doc_id": "SEC-FI-10Q-STRATEGY",
        "source": "Fiserv, Inc. (FI) Form 10-Q - Enterprise Payments",
        "text": "Fiserv maintained operating margins above 28% by shifting commercial merchant acquiring toward dynamic interchange pass-through pricing and automating treasury sweep facilities into overnight sovereign reverse repos."
    },
    {
        "doc_id": "REG-FINCEN-SAR-31CFR",
        "source": "FinCEN BSA / 31 CFR § 1020.320 Suspicious Activity Reporting Protocol",
        "text": "Financial institutions must file a Suspicious Activity Report (SAR) within 30 days for any transaction or structured series of transfers aggregating $5,000 or more involving suspected account takeover, rapid passthrough mule accounts, or 100% origin account balance depletion without commercial purpose. Immediate 24-hour pre-clearing hold is authorized."
    },
    {
        "doc_id": "REG-BASEL3-LCR",
        "source": "Federal Reserve Liquidity Coverage Ratio (LCR) & Treasury Policy 4.2",
        "text": "Minimum intraday commercial clearing settlement buffer must cover 99.9% (3.09 sigma) of peak daily clearing drawdowns ($85.0M floor). Excess operational float above $85.0M should be swept into Tier-1 Overnight Reverse Repo (ON RRP) or 3-Month Sovereign T-Bills subject to a 35% single-counterparty concentration cap."
    }
]

@st.cache_resource
def build_rag_index():
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    corpus_texts = [f"{d['source']} {d['text']}" for d in RAG_CORPUS]
    tfidf_matrix = vectorizer.fit_transform(corpus_texts)
    return vectorizer, tfidf_matrix

# ------------------------------------------------------------------------------
# 2. DEFINE REACT AGENT TOOLS
# ------------------------------------------------------------------------------
def execute_tool(tool_name, args, fraud_data, treasury_data, peer_data, vectorizer, tfidf_matrix):
    if tool_name == "query_fraud_telemetry":
        tx_id = args.get("tx_id")
        if tx_id is not None and str(tx_id).strip() not in ("", "None", "null", "ALL"):
            matches = [r for r in fraud_data if str(r["tx_id"]) == str(tx_id).strip()]
            if matches:
                return json.dumps(matches[0], indent=2)
        return json.dumps(fraud_data[:5], indent=2)

    elif tool_name == "query_treasury_and_peers":
        topic = str(args.get("topic") or "all").lower()
        result = {}
        if "treasury" in topic or "cash" in topic or "all" in topic:
            result["treasury_milp_plan"] = treasury_data
        if "peer" in topic or "margin" in topic or "all" in topic:
            result["peer_financials_sample"] = peer_data[:12]
        return json.dumps(result, indent=2)

    elif tool_name == "search_sec_and_regulatory_rag":
        query = str(args.get("query") or "")
        q_vec = vectorizer.transform([query])
        sims = cosine_similarity(q_vec, tfidf_matrix).flatten()
        top_idx = np.argsort(sims)[::-1][:3]
        hits = [{"score": round(float(sims[i]), 3), **RAG_CORPUS[i]} for i in top_idx]
        return json.dumps(hits, indent=2)

    return json.dumps({"error": "Unknown tool"})

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "query_fraud_telemetry",
            "description": "Fetch high-risk P1 fraud transaction details, accounting balance errors, and 1-hour velocity from Fabric Gold telemetry.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tx_id": {
                        "type": ["string", "null"],
                        "description": "Optional transaction ID to inspect, or null to retrieve top P1 alerts"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "query_treasury_and_peers",
            "description": "Retrieve optimal MILP working capital allocations and peer SEC quarterly margin/take-rate benchmarks.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "enum": ["treasury", "peers", "all"]
                    }
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_sec_and_regulatory_rag",
            "description": "Search SEC 10-K/Q competitor filings (PayPal, Block, Fiserv), FinCEN SAR rules, and Basel III liquidity guidelines.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Semantic search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

# ------------------------------------------------------------------------------
# 3. STREAMLIT UI & REACT LOOP ORCHESTRATOR
# ------------------------------------------------------------------------------
st.title("FinIntel 360: Autonomous Risk & Treasury Copilot")
st.caption("Powered by Microsoft Fabric OneLake Gold Telemetry + ReAct Multi-Tool Reasoning + SEC/FinCEN RAG")

with st.sidebar:
    st.header("LLM Provider Configuration")
    provider = st.radio(
        "Select Inference Engine",
        ["Groq / OpenAI-Compatible Free Tier", "Azure OpenAI (PAYG gpt-4o-mini)"]
    )
    if provider == "Azure OpenAI (PAYG gpt-4o-mini)":
        azure_endpoint = st.text_input("Azure OpenAI Endpoint", value="https://cog-finintel-ai-a1f61.openai.azure.com/")
        azure_key = st.text_input("Azure OpenAI API Key", type="password")
        deployment_name = st.text_input("Deployment Name", value="gpt-4o-mini")
    else:
        api_key = st.text_input("Groq / OpenAI API Key", type="password")
        base_url = st.text_input("Base URL", value="https://api.groq.com/openai/v1")
        model_name = st.text_input("Model Name", value="openai/gpt-oss-120b")

fraud_data, treasury_data, peer_data = load_gold_snapshots()
vectorizer, tfidf_matrix = build_rag_index()

query_params = st.query_params
default_prompt = (
    f"Investigate critical fraud transaction tx_id={query_params['tx_id']}, cross-reference FinCEN SAR rules, and draft an executive hold & SAR action memo."
    if "tx_id" in query_params
    else "Analyze ApexFin's top P1 fraud alerts alongside our $9.02M Treasury MILP optimization and peer SEC 10-K margin trends. Prescribe an executive action plan."
)

user_query = st.text_area("Executive Prompt / Power BI Alert Handoff:", value=default_prompt, height=90)

if st.button("Execute ReAct Agent Investigation", type="primary"):
    if provider == "Azure OpenAI (PAYG gpt-4o-mini)":
        client = AzureOpenAI(azure_endpoint=azure_endpoint, api_key=azure_key, api_version="2024-10-21")
        active_model = deployment_name
    else:
        client = OpenAI(api_key=api_key, base_url=base_url)
        active_model = model_name

    messages = [
        {"role": "system", "content": "You are the FinIntel 360 Chief Risk & Treasury AI Strategist for Apex Financial Technologies. Always use your tools to inspect Gold Lakehouse data and SEC/FinCEN RAG documents before prescribing concrete quantitative actions."},
        {"role": "user", "content": user_query}
    ]

    with st.status("Running Autonomous ReAct Reasoning Loop...", expanded=True) as status:
        for step in range(5):
            response = client.chat.completions.create(
                model=active_model,
                messages=messages,
                tools=TOOLS_SCHEMA,
                tool_choice="auto",
                temperature=0.1
            )
            msg = response.choices[0].message
            messages.append(msg)

            if msg.tool_calls:
                for tc in msg.tool_calls:
                    fn_name = tc.function.name
                    fn_args = json.loads(tc.function.arguments or "{}")
                    st.write(f"**Step {step+1} — Tool Call:** `{fn_name}({fn_args})`")
                    tool_out = execute_tool(fn_name, fn_args, fraud_data, treasury_data, peer_data, vectorizer, tfidf_matrix)
                    with st.expander(f"Observation from {fn_name}"):
                        st.code(tool_out[:1500], language="json")
                    messages.append({"role": "tool", "tool_call_id": tc.id, "content": tool_out})
            else:
                status.update(label="ReAct Investigation Complete!", state="complete")
                st.markdown("### Executive Prescriptive Memo")
                st.markdown(msg.content)
                break