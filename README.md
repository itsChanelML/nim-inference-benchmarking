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

This notebook answers that question empirically across three real-world industry domains — measuring latency, throughput, and output quality across 27 tests.

---

## Test Matrix

| Industry | Tasks | Context Lengths | Tests |
|----------|-------|-----------------|-------|
| Climate Tech | Sensor summary, Policy brief, Risk assessment | Short / Medium / Long | 9 |
| Agriculture | Crop recommendation, Yield prediction, Soil analysis | Short / Medium / Long | 9 |
| Workforce Dev | Career advice, Skill gap analysis, Job match scoring | Short / Medium / Long | 9 |
| **Total** | **9 task types** | **3 context lengths** | **27** |

---

## Results

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

## Key Findings

**1. Context length adds 1.5x latency but quality holds.**  
Short context averages 34.72s. Long context averages 51.66s — a 1.5x increase. Quality scores remain stable (77–81 across all lengths). For high-stakes outputs like policy briefs or risk assessments, longer context is worth the cost.

**2. Medium context outperformed Long on quality (81.1 vs 80.0).**  
Counterintuitive but consistent across industries. Adding context beyond a certain point doesn't improve output quality — it just increases latency. Compress and curate your context rather than maximizing it.

**3. Agriculture domain produced the highest quality outputs (81.7/100).**  
NIM handles structured domain data with specific technical vocabulary exceptionally well. Agronomic terminology, soil chemistry, and yield modeling all produced highly specific, actionable outputs.

**4. Climate Tech was fastest (27.64s avg) but lowest quality (76.1/100).**  
The tradeoff between latency and quality is real. For latency-sensitive climate monitoring applications, Climate Tech prompts are the most efficient. For depth and specificity, Agriculture and Workforce Dev prompts outperform.

**5. Developer recommendation: compress context for latency-sensitive apps.**  
The fastest response was 11.33s (Climate Tech, Short context). The slowest was 144.02s (Agriculture, Long context, complex yield modeling). Design your context strategy around your latency budget.

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

---

## Built By

**Chanel Power**  
Senior ML Engineer · Founder & CEO, Mentor Me Collective  
Genspark Builder Grant Recipient · GTC 2026  
GitHub: [@itsChanelML](https://github.com/itsChanelML)  
LinkedIn: [linkedin.com/in/powerc1](https://linkedin.com/in/powerc1)