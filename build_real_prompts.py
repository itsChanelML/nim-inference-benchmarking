"""
build_real_prompts.py
Generates the 27 benchmark prompts using real government data.
Run this to rebuild Cell 2 of the notebook with authentic data.
"""

from load_data import load_all_data

def build_prompts(data):
    air = data['air_quality']
    health = data['health_impacts']
    yields = data['corn_yields']
    progress = data['crop_progress']
    workforce = data['workforce']
    census = data['census']
    
    # Census education earnings data
    edu = census['median_earnings_by_education']
    bachelors_premium = census['education_earnings_premium']['bachelors_vs_hs']
    total_employed = census['total_employed']
    computer_math = census['computer_math_employed']

    # Pull specific neighborhood data
    sunset = air.get('Sunset Park', {})
    williamsburg = air.get('Williamsburg - Bushwick', {})
    bedford = air.get('Bedford Stuyvesant - Crown Heights', {})
    flatbush = air.get('East Flatbush - Flatbush', {})
    brooklyn = air.get('Brooklyn', {})

    # Health impacts
    w_health = health.get('Williamsburg - Bushwick', {})
    e_health = health.get('East Flatbush - Flatbush', {})
    s_health = health.get('Sunset Park', {})
    b_health = health.get('Brooklyn', {})

    # Corn data
    y2025 = yields.get(2025, 210)
    y2024 = yields.get(2024, 211)
    y2023 = yields.get(2023, 201)
    y2022 = yields.get(2022, 200)
    y2021 = yields.get(2021, 177)
    planted_pct = progress.get('planted', {}).get('value', '1')
    planted_week = progress.get('planted', {}).get('week', '2026-04-12')

    # Workforce
    uxr = workforce['ux_researcher']
    da = workforce['data_analyst']
    ds = workforce['data_scientist']
    ops = workforce['operations_analyst']

    prompts = [

        # ── CLIMATE TECH — SENSOR SUMMARY ────────────────────────
        {
            "industry": "Climate Tech",
            "task": "Sensor Summary",
            "context_length": "Short",
            "prompt": f"Air quality reading, Brooklyn NYC (NYC Community Air Survey, Annual Average 2016): PM2.5: {brooklyn.get('pm25', 7.76)} mcg/m3, NO2: {brooklyn.get('no2', 18.48)} ppb. EPA standard: PM2.5 moderate 12-35 mcg/m3. Summarize this reading for a community board meeting in plain language."
        },
        {
            "industry": "Climate Tech",
            "task": "Sensor Summary",
            "context_length": "Medium",
            "prompt": f"""Brooklyn air quality by neighborhood (NYC Community Air Survey, Annual Average 2016):

Sunset Park: PM2.5 {sunset.get('pm25', 8.40)} mcg/m3, NO2 {sunset.get('no2', 19.44)} ppb
Williamsburg-Bushwick: PM2.5 {williamsburg.get('pm25', 9.55)} mcg/m3, NO2 {williamsburg.get('no2', 20.82)} ppb
Bedford-Stuyvesant: PM2.5 {bedford.get('pm25', 7.94)} mcg/m3, NO2 {bedford.get('no2', 19.15)} ppb
East Flatbush: PM2.5 {flatbush.get('pm25', 7.64)} mcg/m3, NO2 {flatbush.get('no2', 18.86)} ppb

EPA standards: PM2.5 good <12, moderate 12-35. NO2 annual standard 53 ppb.
Summarize for community board meeting. Identify any neighborhoods of concern."""
        },
        {
            "industry": "Climate Tech",
            "task": "Sensor Summary",
            "context_length": "Long",
            "prompt": f"""Brooklyn air quality and health impact data (NYC Community Air Survey / DOHMH):

Air Quality (Annual Average 2016):
- Sunset Park: PM2.5 {sunset.get('pm25', 8.40)} mcg/m3, NO2 {sunset.get('no2', 19.44)} ppb
- Williamsburg-Bushwick: PM2.5 {williamsburg.get('pm25', 9.55)} mcg/m3, NO2 {williamsburg.get('no2', 20.82)} ppb
- Bedford-Stuyvesant: PM2.5 {bedford.get('pm25', 7.94)} mcg/m3
- East Flatbush: PM2.5 {flatbush.get('pm25', 7.64)} mcg/m3, NO2 {flatbush.get('no2', 18.86)} ppb

Health Impacts (per 100,000 residents, 2012-2014):
- Williamsburg-Bushwick: {w_health.get('asthma_ed_pm25', 165.3):.1f} asthma ED visits from PM2.5, {w_health.get('deaths_pm25', 41.1):.1f} deaths from PM2.5
- East Flatbush: {e_health.get('asthma_ed_pm25', 97.2):.1f} asthma ED visits from PM2.5, {e_health.get('deaths_pm25', 37.3):.1f} deaths from PM2.5
- Brooklyn overall: {b_health.get('deaths_pm25', 41.0):.1f} deaths per 100K from PM2.5

Source: NYC DOHMH Community Air Survey and Health Impact Assessment

Summarize for community leaders. Identify highest-risk neighborhoods, explain health impact patterns, recommend 3 specific actions."""
        },

        # ── CLIMATE TECH — POLICY BRIEF ───────────────────────────
        {
            "industry": "Climate Tech",
            "task": "Policy Brief",
            "context_length": "Short",
            "prompt": "NYC Local Law 97 requires buildings over 25,000 sq ft to cut emissions 40% by 2030 and 80% by 2050. Buildings represent 70% of NYC greenhouse gas emissions. Write a 3-sentence policy brief on building electrification urgency."
        },
        {
            "industry": "Climate Tech",
            "task": "Policy Brief",
            "context_length": "Medium",
            "prompt": """NYC Building Electrification — Current Status:
- Local Law 97 covers 50,000+ buildings. Penalties begin 2024: $268/metric ton CO2 over limit
- Current compliance: 34% of covered buildings on track for 2030 targets
- Heat pump adoption: 18% year-over-year growth citywide
- Con Edison incentive: $10,000 residential, $50,000 commercial
- Federal IRA: 30% tax credit for heat pump installation
- Contractor gap: ~2,400 licensed installers now, estimated 8,000+ needed by 2030

Write a 150-word policy brief on accelerating electrification to meet 2030 targets. Include one specific recommendation."""
        },
        {
            "industry": "Climate Tech",
            "task": "Policy Brief",
            "context_length": "Long",
            "prompt": """NYC Building Electrification — Comprehensive Data:

Compliance: 50,000 buildings under LL97. Manhattan 41% compliant, Brooklyn 31%, Bronx 28%, Queens 29%.
Emissions: Buildings = 70% of NYC GHG. Bronx and Brooklyn have highest density AND lowest compliance.
Economics: Heat pump cost $8K-$15K residential, $40K-$200K commercial. 62% cite upfront cost as barrier.
Workforce: 2,400 licensed heat pump installers. Need 8,000+ by 2030. Median wage $68,000. CUNY offers 6-month training.
Incentives: IRA 30% credit + Con Ed $10K residential + $50K commercial.
Penalties: $268/metric ton CO2 over limit starting 2024.
Environmental justice: Lowest-income neighborhoods have highest emission exposure and lowest program uptake.

Write a 250-word policy brief addressing financing gap, workforce pipeline, and environmental justice. Include 3 recommendations with estimated impact on compliance rates."""
        },

        # ── CLIMATE TECH — RISK ASSESSMENT ────────────────────────
        {
            "industry": "Climate Tech",
            "task": "Risk Assessment",
            "context_length": "Short",
            "prompt": "Red Hook, Brooklyn: FEMA Zone AE flood zone, sea level projected +2.5 feet by 2050. Write a 2-sentence risk summary for residents."
        },
        {
            "industry": "Climate Tech",
            "task": "Risk Assessment",
            "context_length": "Medium",
            "prompt": f"""Red Hook, Brooklyn — Climate Risk Profile (FEMA / NYC Panel on Climate Change):
- Flood zone: FEMA Zone AE (high risk). Sea level rise: +2.5 feet by 2050.
- Storm surge: 10% annual probability of 3+ foot surge.
- Hurricane Sandy 2012: 6.9 foot surge, neighborhood largely inundated.
- Population: ~11,000 residents. 35% below poverty line.
- Air quality context: Nearby Sunset Park PM2.5 {sunset.get('pm25', 8.40)} mcg/m3 (NYC Community Air Survey).

Write a 150-word risk assessment that is honest but actionable. Include both flood and air quality dimensions."""
        },
        {
            "industry": "Climate Tech",
            "task": "Risk Assessment",
            "context_length": "Long",
            "prompt": f"""Red Hook, Brooklyn — Comprehensive Climate Risk (FEMA / NPCC / NYC DOHMH):

Flood Risk:
- FEMA Zone AE. Sea level: +1.5ft by 2030, +2.5ft by 2050, +4.5ft by 2080 (NPCC high estimate)
- 10% annual probability of 3+ foot surge. Sandy 2012: 6.9ft, 70% of neighborhood inundated.
- 6 of 14 streets below 6-foot elevation. Combined sewer overflow at 2 inches/hour rainfall.

Air Quality (NYC Community Air Survey):
- Nearby Sunset Park: PM2.5 {sunset.get('pm25', 8.40)} mcg/m3, NO2 {sunset.get('no2', 19.44)} ppb
- Sunset Park asthma hospitalizations from ozone: {s_health.get('asthma_ed_pm25', 11.6)} per 100K (2012-2014)

Population Vulnerability:
- 11,000 residents. 35% below poverty. 18% elderly. 34% car ownership (evacuation dependency).
- NYCHA Red Hook Houses: 6,000 residents, buildings averaging 60 years old.
- 2 evacuation routes, both susceptible to flooding above 4 feet.

Write a 300-word risk assessment for community leaders covering flood timeline, air quality compounding risks, population vulnerabilities, and 4 resilience investments prioritized by impact."""
        },

        # ── AGRICULTURE — CROP RECOMMENDATION ────────────────────
        {
            "industry": "Agriculture",
            "task": "Crop Recommendation",
            "context_length": "Short",
            "prompt": f"Iowa corn field, V6 growth stage (6-leaf collar). USDA reports Iowa {planted_week[:4]} planting at {planted_pct}% complete statewide. Soil moisture 35%, temperature 68F. What should the farmer do this week?"
        },
        {
            "industry": "Agriculture",
            "task": "Crop Recommendation",
            "context_length": "Medium",
            "prompt": f"""Field Report — Johnson County, Iowa (April 2026):
Crop: Corn (Pioneer P1185AM), Growth Stage: V6
USDA Crop Progress (week ending {planted_week}): Iowa {planted_pct}% planted statewide
Soil moisture: 35% (field capacity 42%), Soil temp: 58F
Rainfall last 14 days: 1.2 inches (30-year April average: 2.1 inches)
Forecast: Dry, highs 65-72F for next 7 days
Pre-plant fertilizer: 120 lbs/acre urea applied
Observed: Lower leaf yellowing on 15% of plants

Provide crop management recommendations for this week. Address the yellowing observation."""
        },
        {
            "industry": "Agriculture",
            "task": "Crop Recommendation",
            "context_length": "Long",
            "prompt": f"""Comprehensive Field Report — 240-acre Iowa Corn (Pioneer P1185AM, V6):

USDA Context (week ending {planted_week}): Iowa {planted_pct}% planted statewide.
5-year Iowa state yield history (USDA NASS): 2025: {y2025} bu/ac, 2024: {y2024} bu/ac, 2023: {y2023} bu/ac, 2022: {y2022} bu/ac

Field conditions:
- Zone 1 (140ac): soil moisture 35% (FC 42%)
- Zone 2 (60ac): soil moisture 38% (FC 44%)
- Zone 3 (40ac): soil moisture 29% — below threshold
- N tissue test V4: 3.6% (marginal, threshold 4.0%)
- 15% lower leaf yellowing, concentrated in Zone 3

Weather: 1.2in rain last 14 days (avg 2.1in). Dry 10 days, then 60% rain chance April 28-30.
Pest: Black cutworm 3 moths/trap/night (scouting threshold: 5).

Provide 14-day management plan with N application rates by zone and Zone 3 irrigation guidance."""
        },

        # ── AGRICULTURE — YIELD PREDICTION ────────────────────────
        {
            "industry": "Agriculture",
            "task": "Yield Prediction",
            "context_length": "Short",
            "prompt": f"Iowa corn field, V6 stage, normal rainfall, adequate fertility. USDA reports Iowa 5-year average yield around {y2023}-{y2025} bu/acre. Estimated yield range for this field?"
        },
        {
            "industry": "Agriculture",
            "task": "Yield Prediction",
            "context_length": "Medium",
            "prompt": f"""240-acre Iowa corn field yield estimate request:
Hybrid: Pioneer P1185AM (111-day). Stage: V6.
Soil moisture slightly below field capacity in one zone. N tissue 3.6% (marginal).
Rainfall last 14 days: 1.2 inches (below average).

USDA NASS Iowa state yields: 2025: {y2025} bu/ac, 2024: {y2024} bu/ac, 2023: {y2023} bu/ac, 2022: {y2022} bu/ac
Field 5-year average: 198 bu/acre. Johnson County average: 187 bu/acre.

Provide yield estimate range and identify top 2 factors influencing final yield."""
        },
        {
            "industry": "Agriculture",
            "task": "Yield Prediction",
            "context_length": "Long",
            "prompt": f"""Yield Forecast — 240-acre Iowa Corn (Pioneer P1185AM):

USDA NASS Iowa State Yields (bu/acre):
2025: {y2025} | 2024: {y2024} | 2023: {y2023} | 2022: {y2022} | 2021: {y2021}
Field 5-year avg: 198. Johnson County 2025 avg: 187. State 2025 avg: {y2025}.

Current issues: N tissue marginal (3.6%), Zone 3 moisture below threshold, no irrigation.
Side-dress N planned: 60 lbs/acre urea by April 28.
Corn futures: $4.85/bu.

Weather scenarios:
A: Favorable (normal June-Aug rainfall) — historical probability 40%
B: Moderate stress (below-normal July, one heat event) — 35%
C: Drought stress (July-Aug deficit, multiple heat events) — 25%

Provide yield forecast for each scenario with revenue impact per acre at $4.85/bu. Identify single highest-impact management action remaining."""
        },

        # ── AGRICULTURE — SOIL ANALYSIS ───────────────────────────
        {
            "industry": "Agriculture",
            "task": "Soil Analysis",
            "context_length": "Short",
            "prompt": "Iowa soil test results: pH 5.8, P 18 ppm (low), K 145 ppm (adequate), OM 3.2%. Planning soybeans spring 2026. What amendments are needed?"
        },
        {
            "industry": "Agriculture",
            "task": "Soil Analysis",
            "context_length": "Medium",
            "prompt": f"""Iowa soybean field soil test (fall 2025, Johnson County):
pH: 5.8 (target 6.2-6.8 for soybeans)
P (Bray P1): 18 ppm (low, target 25-40 ppm)
K: 145 ppm (adequate, target 130-175 ppm)
Organic matter: 3.2%, CEC: 16 meq/100g
Zinc: 0.8 ppm (marginal, threshold 1.0 ppm)
Previous crop: Corn yielding {y2025} bu/acre (USDA NASS Iowa 2025 average)

Planting Group 3.5 soybeans spring 2026. Amendment recommendations with specific rates per acre."""
        },
        {
            "industry": "Agriculture",
            "task": "Soil Analysis",
            "context_length": "Long",
            "prompt": f"""Comprehensive Soil Assessment — 160-acre Iowa soybean field:
Previous crop: Corn at {y2025} bu/acre (Iowa 2025 USDA NASS average: {y2025} bu/ac)

Standard soil test (fall 2025):
pH 5.8, buffer pH 6.6, P 18 ppm (low), K 145 ppm (adequate)
Ca 68% base saturation, Mg 12%, Zn 0.8 ppm (marginal), OM 3.2%, CEC 16

Haney biological test: Soil health score 6.2/10, CO2 respiration 98 ppm
Compaction: 280-320 psi at 12-16 inch depth in 40% of field (threshold 300 psi)

Economics: Soybean $9.85/bu. Lime $32/ton applied. DAP (18-46-0) $620/ton. MOP (0-0-60) $395/ton.
Iowa state soybean average 2025: 57 bu/acre.

Complete amendment plan with lime rate and timing, P/K/micronutrient rates, compaction remediation strategy, and ROI calculation per amendment prioritized by yield impact."""
        },

        # ── WORKFORCE DEV — CAREER PATH ───────────────────────────
        {
            "industry": "Workforce Dev",
            "task": "Career Path Advice",
            "context_length": "Short",
            "prompt": f"First-generation professional, 2 years UX Research at nonprofit ($72K). BLS reports NYC UX Researcher median salary ${uxr['median_annual']:,}. How do I get there in 12-18 months?"
        },
        {
            "industry": "Workforce Dev",
            "task": "Career Path Advice",
            "context_length": "Medium",
            "prompt": f"""Career transition profile:
Current: UX Researcher, NYC nonprofit, 2 years, $72,000
Target: UX Researcher at tech company

BLS OES 2023 NYC Metro wage data:
- UX Researcher median: ${uxr['median_annual']:,} (25th-75th: ${uxr['p25']:,}-${uxr['p75']:,})
- NYC employment in role: {uxr['employment']:,} positions

Constraints: No CS degree, 45 LinkedIn connections (3 in tech), cannot leave current job.
Timeline: 12-18 months. Target salary: $110,000+

Provide a 3-step career transition plan with concrete actions for each step."""
        },
        {
            "industry": "Workforce Dev",
            "task": "Career Path Advice",
            "context_length": "Long",
            "prompt": f"""Career Transition — First-Generation UX Researcher to Tech:

Current situation: MS Communication Design (City College NY), UX Researcher at housing advocacy nonprofit, 2 years, $72,000.
First-generation college graduate. No family network in tech.

Skills (1-5): User interviews 4, Usability testing 3, Survey design 4, Data analysis 2, Figma 2, SQL 1, Stakeholder presentation 4.
Portfolio: 3 nonprofit case studies online. Network: 45 LinkedIn connections, 3 in tech.

BLS OES 2023 NYC Metro Market Data:
- UX Researcher: median ${uxr['median_annual']:,}, 75th percentile ${uxr['p75']:,}, {uxr['employment']:,} employed
- Data Scientist: median ${ds['median_annual']:,} (for context on adjacent roles)
- NYC tech sector employment growth: 8.3% 2022-2023 (NYC Comptroller)
- Census ACS 2022: {computer_math:,} computer/math workers employed in NYC metro
- Education earnings premium: Bachelor's degree earns ${bachelors_premium:,} more than HS grad annually (Census ACS 2022)
- Total NYC metro workforce: {total_employed:,} employed (Census ACS 2022)

Target: Mission-driven tech company (Spotify, Duolingo, Khan Academy, Etsy). Target $115K-$130K. 18-month timeline.
Constraint: Cannot take unpaid work or leave current job.

Provide an 18-month roadmap in 3 phases (0-6, 6-12, 12-18 months). For each phase: 3 concrete actions, skills to develop, portfolio targets, success metrics. Address the no-CS-degree barrier with specific evidence-based strategies."""
        },

        # ── WORKFORCE DEV — SKILL GAP ─────────────────────────────
        {
            "industry": "Workforce Dev",
            "task": "Skill Gap Analysis",
            "context_length": "Short",
            "prompt": f"Current: Python basics, Excel, project management (PMP). Target: Data Analyst. BLS NYC median ${da['median_annual']:,}. What skills am I missing and how long to close the gap?"
        },
        {
            "industry": "Workforce Dev",
            "task": "Skill Gap Analysis",
            "context_length": "Medium",
            "prompt": f"""Skill gap analysis — Operations to Data Analyst:
Current: Python (pandas), Excel (pivot tables), SQL (SELECT basics), PMP certified.
3 years operations analyst at logistics company. Current salary: ${ops['median_annual']:,} (BLS NYC ops analyst median).

Target: Data Analyst at NYC tech company.
BLS OES 2023 NYC Metro: Data Analyst median ${da['median_annual']:,}, 75th percentile ${da['p75']:,}.

Job posting requirements (based on 47 NYC postings): Advanced SQL (90%+), Python statistical analysis (70%+), Tableau or Power BI (90%+), A/B testing (50%+).

Identify top 3 skill gaps with learning plan (resource + time to proficiency) for each."""
        },
        {
            "industry": "Workforce Dev",
            "task": "Skill Gap Analysis",
            "context_length": "Long",
            "prompt": f"""Comprehensive Skill Gap Analysis — Operations to Data Analyst (NYC):

Candidate: 3 years operations analyst, logistics. Python intermediate, SQL intermediate (no window functions), Excel advanced, Tableau viewer. PMP certified.
Current compensation: ~${ops['median_annual']:,} (BLS NYC operations analyst median).

Target role market data (BLS OES 2023, NYC-Newark-Jersey City MSA):
- Data Analyst median: ${da['median_annual']:,} | Mean: ${da['mean_annual']:,}
- 25th percentile: ${da['p25']:,} | 75th percentile: ${da['p75']:,}
- NYC metro employment: {da['employment']:,} positions
- Salary premium over ops analyst: ${da['median_annual'] - ops['median_annual']:,} (median)
- Census ACS 2022: {computer_math:,} computer/math occupations in NYC metro
- Education premium: Bachelor's holders earn ${edu['bachelors']:,} median vs ${edu['hs_graduate']:,} for HS grads

Job market analysis (47 NYC postings, $90K-$120K range):
- Advanced SQL (window functions, CTEs): required in 90%+ postings
- Python statistical analysis: 70%+
- Tableau or Power BI (builder level): 90%+
- A/B testing and statistical significance: 50%+
- Dashboard building: 50%+

Constraints: 8-10 hrs/week available, $100/month budget, 9-month job search timeline, prefers project-based learning.

Prioritized skill gap roadmap for 9 months. Rank gaps by: (1) posting frequency, (2) time to proficiency, (3) salary impact. Include free/low-cost resources and one portfolio project demonstrating multiple skills simultaneously."""
        },

        # ── WORKFORCE DEV — JOB MATCH ─────────────────────────────
        {
            "industry": "Workforce Dev",
            "task": "Job Match Scoring",
            "context_length": "Short",
            "prompt": f"Candidate: 3 years data analysis, Python intermediate, SQL intermediate, Tableau proficient. Job: Senior Data Analyst, 5 years required, advanced SQL, Python ML. BLS NYC senior DA 75th percentile ${da['p75']:,}. Match score and top gaps?"
        },
        {
            "industry": "Workforce Dev",
            "task": "Job Match Scoring",
            "context_length": "Medium",
            "prompt": f"""Job match analysis:

CANDIDATE: 3 years data analysis (logistics), Python intermediate, SQL intermediate, Tableau proficient, PMP.
Current salary ~${ops['median_annual']:,} (BLS NYC operations analyst median).

JOB: Senior Data Analyst, Spotify NYC
Salary range: $115,000-$135,000 (BLS NYC 75th percentile for data analysts: ${da['p75']:,})
Required: 5+ years, advanced SQL, Python statistical libraries, consumer product analytics, Looker or Tableau.
Preferred: A/B testing at scale, ML pipeline exposure.

Provide match score (0-100), top 3 gaps, and recommendation: apply now or in 6 months?"""
        },
        {
            "industry": "Workforce Dev",
            "task": "Job Match Scoring",
            "context_length": "Long",
            "prompt": f"""Comprehensive Job Match Analysis:

CANDIDATE: Operations analyst (3 years, logistics). Python intermediate, SQL intermediate (no window functions), Tableau proficient, Excel advanced, PMP, Google Data Analytics cert. 2 GitHub projects. Strong communicator.
Compensation history: ~${ops['median_annual']:,}/year.

TARGET JOB: Senior Data Analyst — Growth, Etsy NYC
Posted salary: $110,000-$130,000
BLS OES 2023 context: NYC Data Analyst median ${da['median_annual']:,}, 75th percentile ${da['p75']:,}, mean ${da['mean_annual']:,}

Required: 4+ years, expert SQL (window functions, optimization, complex joins), Python proficiency, A/B testing and statistical significance, large dataset experience (billions of rows), translate analysis to business recommendations.
Preferred: E-commerce/marketplace experience, Looker/dbt/Airflow, statistical modeling, product + engineering collaboration.

Provide: (1) Match score by category with weights, (2) Top 3 competitive strengths, (3) Top 3 disqualifying gaps with severity, (4) Apply now vs 6 months recommendation with rationale, (5) Opening paragraph for cover letter that addresses the experience gap proactively using the salary data as context."""
        },
    ]

    return prompts

if __name__ == "__main__":
    data = load_all_data()
    prompts = build_prompts(data)
    print(f"\nGenerated {len(prompts)} prompts with real data")
    print("\nSample — Climate Tech Sensor Summary Short:")
    print(prompts[0]['prompt'])
    print("\nSample — Agriculture Yield Prediction Long:")
    print(prompts[13]['prompt'][:300] + "...")
    print("\nSample — Workforce Dev Career Path Medium:")
    print(prompts[19]['prompt'])