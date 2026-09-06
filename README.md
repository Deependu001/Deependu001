<div align="center">

<a href="https://github.com/Deependu001">
  <img src="./assets/header.gif" width="100%" alt="Deependu Mondal // Cybersecurity Engineer" />
</a>

<p align="center">
  <a href="https://linkedin.com/in/deependu-mondal-105825328/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://tryhackme.com/p/Deependu001">
    <img src="https://img.shields.io/badge/TryHackMe-Deependu001-red?style=flat-square&logo=tryhackme&logoColor=white" alt="TryHackMe" />
  </a>
  <a href="https://medium.com/@deependumondal001">
    <img src="https://img.shields.io/badge/Field_Notes-Medium-000000?style=flat-square&logo=medium&logoColor=white" alt="Medium" />
  </a>
  <a href="mailto:mondaldeependu@gmail.com">
    <img src="https://img.shields.io/badge/Email-mondaldeependu%40gmail.com-blue?style=flat-square&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

</div>

---

### 01 // PROFESSIONAL SUMMARY

I am an engineering undergraduate specializing in Artificial Intelligence (AGEMC, 2024–2028) with a focused concentration on **Offensive Security**, **Application Security (AppSec)**, and **Security Tooling Engineering**. 

My core engineering thesis:
> *"I build practical security tooling to dissect how software boundaries fail, automate vulnerability identification, and engineer deterministic detections before adversaries exploit them."*

Rather than viewing offensive and defensive disciplines as disconnected silos, my work operates across the complete vulnerability lifecycle:

```text
Reconnaissance ➔ Attack Surface Discovery ➔ Vulnerability Discovery ➔ Exploitation Modeling ➔ Detection Engineering ➔ Threat Intelligence ➔ Remediation
```

---

### 02 // CORE SECURITY FOCUS & TECHNICAL PIPELINE

| Discipline | Engineering Vector | Operational Scope |
| :--- | :--- | :--- |
| **Offensive Security** | Attack Surface Discovery & Probing | Active reconnaissance, web/API parameter fuzzing, authentication bypass validation, and controlled exploit verification. |
| **Application Security** | Vulnerability Auditing & AST Analysis | Automated OWASP Top 10 auditing, schema validation, rate-limit testing, and broken object level authorization (BOLA) detection. |
| **Security Engineering** | Threat Detection & Client Isolation | Building local heuristic engines, client-side execution sandboxes (Manifest V3), packet inspection harnesses, and structured SARIF/JSON reporting. |
| **Threat Intelligence** | Indicator Ingestion & Classification | Automated enrichment of IOC feeds, behavioral heuristic scoring, and correlating telemetry against MITRE ATT&CK techniques. |

---

### 03 // FEATURED SECURITY SYSTEMS

#### 01. `ThreatIntel-Engine` // Autonomous Threat Intelligence & IOC Classification System
> **Problem:** Security Operations teams face high indicator noise, fragmented feeds (AlienVault, VirusTotal, MISP), and slow contextualization during incident triage.  
> **Security Objective:** Automate ingestion, deduplication, behavioral scoring, and MITRE ATT&CK mapping for network observables with actionable telemetry output.

* **Architecture:** Modular ingestion worker (`Python` / `AsyncIO`) ➔ Feed normalizer ➔ Heuristic scoring pipeline (Entropy + ASN + WHOIS age) ➔ SQLite/PostgreSQL datastore ➔ Fast REST API (`FastAPI`) with structured JSON export.
* **Security Capabilities:** Automated scoring of high-risk CIDRs, domain typosquatting detection (Levenshtein & visual homoglyph distance), and contextual IOC enrichment without unthrottled upstream API exhaustion.
* **Engineering Decisions:** Implemented token-bucket rate limiting across external API connectors; built persistent disk caching for repeated IOC queries to minimize external egress and operational latency.
* **Limitations:** Contextual enrichment is dependent on external threat feed uptime and API rate allowances; scoring weights require periodic baseline calibration against benign corporate traffic.
* **Repository:** `https://github.com/Deependu001/threatintel-engine` *(In active development)*

---

#### 02. `APISentry` // Automated OWASP API & Web Vulnerability Auditor
> **Problem:** Microservice-heavy architectures frequently expose undocumented endpoints, broken object-level authorization (BOLA/IDOR), and stateful logic flaws that static code analyzers miss.  
> **Security Objective:** Provide a deterministic, reproducible CLI engine that parses OpenAPI/Swagger specifications or crawls HTTP endpoints to probe for high-severity authorization and injection vulnerabilities.

* **Architecture:** Target Parser (OpenAPI/Swagger v2/v3 + HTML Crawler) ➔ Request Mutator & State Machine ➔ Security Probe Engine (SQLi, SSRF, IDOR, Header Misconfigurations) ➔ Anomaly Classifier (HTTP status, timing differentials, response payload length) ➔ SARIF/Markdown Reporter.
* **Security Capabilities:** Deterministic validation of BOLA by testing cross-tenant object identifiers; active parameter pollution and boundary fuzzing; verification of missing authentication tokens on private routes.
* **Engineering Decisions:** Designed a stateful token-replay engine that maintains dual authenticated sessions (Tenant A vs. Tenant B) to mathematically demonstrate authorization boundary violations with zero human guesswork.
* **Limitations:** Does not execute complex JavaScript SPAs natively (requires headless Chromium integration for dynamic client-rendered routes); destructive payloads are strictly excluded by default to prevent database corruption.
* **Repository:** `https://github.com/Deependu001/apisentry` *(In active development)*

---

#### 03. `PhishingGuard` // Client-Side Runtime Isolation & Payload Interception
> **Problem:** Cloud-reliant antiphishing tools leak full user browsing history to third-party servers, introducing severe privacy and compliance vulnerabilities while failing against newly registered zero-day domains.  
> **Security Objective:** Intercept and neutralize deceptive DOM overlays, cloaked input forms, and spoofed punycode domains directly inside browser execution sandboxes under Manifest V3 without external telemetry egress.

* **Architecture:** Background Service Worker (Declarative Net Request) ➔ MutationObserver Content Script ➔ Shadow DOM Traversal Engine ➔ Heuristic Scorer (Levenshtein distance, brand entropy, credential input visibility) ➔ Client-side Explanatory Modal.
* **Security Capabilities:** Deep nested Shadow DOM traversal; real-time Punycode/homoglyph resolution; offline heuristic evaluation with **zero outbound user metadata transmission**.
* **Verification & Test Harness:** Backed by **104 automated unit and synthetic attack test cases** verifying boundary defense and zero false-positive regressions on top-ranking domains.
* **Repository:** `https://github.com/Deependu001/PhishingGuard`

---

### 04 // TECHNICAL SKILLS & VERIFIABLE CAPABILITIES

```text
┌─── CAPABILITY MATRIX ─────────────────────────────────────────────────────────────────────┐
│ APPLICATION SECURITY    OWASP Top 10 · OWASP API Top 10 · BOLA/IDOR · CSRF · Input Fuzzing│
│ OFFENSIVE SECURITY      Reconnaissance · Nmap · Burp Suite · Metasploit · Exploit Modeling│
│ PROTOCOLS & NETWORK     TCP/IP · Wireshark · tcpdump · Raw Sockets · DNS/HTTP Internals   │
│ SYSTEMS & RUNTIMES      Linux Internals (Debian/Arch) · POSIX Shell · C/C++ · Manifest V3 │
│ BACKEND & TOOLING       Python · FastAPI · AsyncIO · SQLite · PostgreSQL · Docker · Git   │
│ VERIFICATION & TESTING  pytest · Automated Synthetic Harnesses · SARIF · Structured JSON  │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 05 // SYSTEMATIC SECURITY METHODOLOGY

Every security tool, audit, and laboratory experiment I conduct adheres to a repeatable engineering methodology:

1. **Threat Modeling & Surface Mapping:** Identify trust boundaries, untrusted input ingress vectors, assets, and attacker motivation using STRIDE and attack tree decomposition.
2. **Deterministic Validation:** Vulnerabilities must be reliably reproducible with minimal proof-of-concept scripts rather than theoretical speculation.
3. **Detection Engineering:** For every attack vector validated, write corresponding detection criteria (Suricata/Snort signatures, YARA rules, or application-level log markers).
4. **Actionable Remediation Guidance:** Every reported finding must contain a concrete architectural fix (e.g., parameter binding, server-side session authorization, secure header baselines) with documented trade-offs.

---

### 06 // LAB RESEARCH & TECHNICAL WRITEUPS

I document hands-on security evaluations, vulnerability breakdowns, and lab challenges to bridge the gap between offensive exploitation and defensive engineering:

| Target / Subject | Research Focus | Primary Finding & Engineering Takeaway | Link |
| :--- | :--- | :--- | :--- |
| **TryHackMe Labs** | PrivEsc & Network Exploitation | Systematic exploitation of Linux misconfigurations, sudo rights, and SUID binaries; wrote automation scripts to flag vulnerable cron jobs. | [Lab Profile ↗](https://tryhackme.com/p/Deependu001) |
| **DOM Sandbox Security** | Manifest V3 & Client Isolation | Analyzing how deceptive overlays exploit Shadow DOM isolation to evade traditional regex-based DOM scanners. | [Read on Medium ↗](https://medium.com/@deependumondal001) |
| **Adversarial Invariants** | Probabilistic AI Vulnerability Surfaces | Dissecting how high-entropy character permutations induce classification bypasses in heuristic and ML security filters. | [Read on Medium ↗](https://medium.com/@deependumondal001) |

---

### 07 // ENGINEERING STANDARDS

To ensure tools are production-ready rather than disposable academic scripts, all repository releases are expected to meet:

* **Reproducibility:** Single-command setup via Docker or virtual environment harnesses (`requirements.txt` / `Dockerfile`).
* **Safe by Default:** Dry-run modes, strict scope restrictions (CIDR/domain whitelists), and zero out-of-bounds scanning.
* **Structured Logging & Egress:** Standardized output via JSON / SARIF for effortless pipeline integration with SIEMs or CI/CD systems.
* **Rigorous Documentation:** Comprehensive README architecture covering threat models, architectural flow, setup, limitations, and responsible use policies.

---

### 08 // PROFESSIONAL CONTACT & VERIFICATION

* **LinkedIn:** [linkedin.com/in/deependu-mondal-105825328](https://linkedin.com/in/deependu-mondal-105825328/)
* **Email:** [mondaldeependu@gmail.com](mailto:mondaldeependu@gmail.com)
* **TryHackMe Labs:** [tryhackme.com/p/Deependu001](https://tryhackme.com/p/Deependu001)
* **Technical Dispatches:** [medium.com/@deependumondal001](https://medium.com/@deependumondal001)
* **Location:** Kolkata, India (IST / UTC+5:30)

<br />

<div align="center">
  <sub><code>ENGINEERING DOSSIER // DEEPENDU MONDAL // SECURITY OPERATIONS &amp; TOOLING ARCHITECTURE</code></sub>
</div>
