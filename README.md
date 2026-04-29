# NIM Inference Benchmarking: Nemotron Across Three Industries

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/itsChanelML/nim-inference-benchmarking/blob/main/nim_benchmarking.ipynb)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![NVIDIA NIM](https://img.shields.io/badge/NVIDIA-NIM-76B900.svg)](https://build.nvidia.com)

**Model:** `nvidia/llama-3.3-nemotron-super-49b-v1.5` via NVIDIA NIM  
**Author:** Chanel Power | [@itsChanelML](https://github.com/itsChanelML)  

---

## The Question

Every developer building on NIM eventually asks the same thing:

*Which model, which config, for which workload?*

This study answers that question empirically across three real-world industry domains. Two complete runs of 27 tests each — first with synthetic prompts, then with real government data pulled live from NYC's Department of Health, the USDA NASS API, the Bureau of Labor Statistics, and the US Census. 54 tests total.

---

## Test Matrix

| Industry | Tasks | Context Lengths | Tests per Run |
|----------|-------|-----------------|---------------|
| Climate Tech | Sensor summary, Policy brief, Risk assessment | Short / Medium / Long | 9 |
| Agriculture | Crop recommendation, Yield prediction, Soil analysis | Short / Medium / Long | 9 |
| Workforce Dev | Career advice, Skill gap analysis, Job match scoring | Short / Medium / Long | 9 |
| **Total** | **9 task types** | **3 context lengths** | **27 per run / 54 total** |

---

## Results

### Run 1 — Synthetic Prompts

| Metric | Value |
|--------|-------|
| Average latency | 39.79s |
| Latency range | 11.33s – 144.02s |
| Average throughput | 32.3 tokens/sec |
| Average quality score | 79.4 / 100 |

**By Industry:**

| Industry | Avg Latency | Quality Score | Throughput |
|----------|-------------|---------------|------------|
| Agriculture | 52.84s | **81.7 / 100** | 29.0 tok/s |
| Workforce Dev | 38.89s | 80.6 / 100 | 33.0 tok/s |
| Climate Tech | 27.64s | 76.1 / 100 | 34.7 tok/s |

**By Context Length:**

| Context | Avg Latency | Quality Score |
|---------|-------------|---------------|
| Short | 34.72s | 77.2 / 100 |
| Medium | 32.99s | **81.1 / 100** |
| Long | 51.66s | 80.0 / 100 |

---

### Run 2 — Real Government Data

Data sources: NYC DOHMH Air Quality (NYC Open Data), USDA NASS Iowa Corn Yield and Crop Progress (live API), BLS OES 2023 NYC Metro occupational wages, US Census ACS 2022 NYC Metro workforce data.

| Metric | Value |
|--------|-------|
| Average latency | 42.65s |
| Average quality score | 74.6 / 100 |

**By Industry:**

| Industry | Avg Latency | Quality Score | vs Synthetic |
|----------|-------------|---------------|--------------|
| Climate Tech | 38.96s | 79.4 / 100 | +3.3 |
| Agriculture | 49.84s | 73.9 / 100 | -7.8 |
| Workforce Dev | 39.13s | 70.6 / 100 | -10.0 |

**By Context Length:**

| Context | Avg Latency | Quality Score | vs Synthetic |
|---------|-------------|---------------|--------------|
| Short | 49.04s | 70.6 / 100 | -6.6 |
| Medium | 37.30s | 75.6 / 100 | -5.5 |
| Long | 41.60s | 77.8 / 100 | -2.2 |

---

## Key Findings

**1. Real data creates measurably different inference behavior.**  
Climate Tech quality improved with real air quality readings (+3.3 points). Agriculture and Workforce Dev dropped significantly — real agronomic terminology and specific salary and census data create more complex reasoning demands than generic prompts. The context length pattern flipped entirely between runs.

**2. Context length adds 1.5x latency but quality holds within each run.**  
Short to long context adds roughly 1.5x latency across both runs. Quality scores remain more stable than latency. For high-stakes outputs like policy briefs or risk assessments, longer context is worth the cost.

**3. Medium context outperformed Long on quality in Run 1 (81.1 vs 80.0).**  
Counterintuitive but consistent. Adding context beyond a certain point does not improve output quality with synthetic prompts. With real data, Long context performed best — suggesting real structured data benefits from more context to anchor the model.

**4. Agriculture produced the highest quality scores in Run 1 (81.7/100).**  
NIM handles structured domain data with specific technical vocabulary well. The drop in Run 2 reflects the increased complexity of real agronomic inputs, not model degradation.

**5. Test with real domain data before you ship.**  
Synthetic benchmarks will not predict real-world behavior. The fastest response was 11.33s. The slowest was 144.02s. Design your context strategy around your latency budget — and validate against real data before making architecture decisions.

---

## Notebook Structure

| Cell | Purpose |
|------|---------|
| Cell 1 | Setup — API client, model config, dependencies |
| Cell 2 | 27 prompts across 3 industries and 3 context lengths |
| Cell 3 | Quality scoring rubric (Relevance, Completeness, Specificity, Actionability) |
| Cell 4 | Benchmarking loop — calls NIM, measures latency and throughput |
| Cell 5 | Results dataframe — pandas summary by industry and context length |
| Cell 6 | Visualizations — 4 charts saved to results/ |
| Cell 7 | Developer conclusions |

---

## Run It

```bash
git clone https://github.com/itsChanelML/nim-inference-benchmarking.git
cd nim-inference-benchmarking
pip install openai pandas matplotlib python-dotenv
cp .env.example .env
# Add your NVIDIA NIM API key to .env
jupyter notebook
```

Or click the Colab badge above for zero-setup access.

---

## Stack

| Layer | Tool |
|-------|------|
| Model | nvidia/llama-3.3-nemotron-super-49b-v1.5 |
| Inference | NVIDIA NIM API |
| Analysis | Python, pandas, matplotlib |
| Notebook | Jupyter + Google Colab |
| Real Data | NYC Open Data, USDA NASS API, BLS OES, US Census ACS |

---

## Built By

**Chanel Power**  
Senior ML Engineer · Founder & CEO, Mentor Me Collective  
Genspark Builder Grant Recipient · GTC 2026  
GitHub: [@itsChanelML](https://github.com/itsChanelML)  
LinkedIn: [linkedin.com/in/powerc1](https://linkedin.com/in/powerc1)