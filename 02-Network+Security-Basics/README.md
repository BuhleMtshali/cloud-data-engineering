# 🌐🔐🕵🏽 Networking + Security Basics

## Packets, Principles, and Defender Brain 🦈🧠

Welcome to the **Networking + Security Basics** phase of my Cloud Data & Security Engineering roadmap.

This phase teaches me how systems communicate, how attackers abuse trust, how defenders reduce risk, and how security teams use logs, controls, frameworks, and investigation workflows to understand what happened.

Before advanced cloud detections.

Before multi-account threat hunting.

Before dramatic dashboards glowing red at 03:17.

I need to understand identity, encryption, traffic, vulnerabilities, risk, logs, and response.

Security is not a collection of scary tool names. It is the practice of understanding assets, threats, controls, evidence, and consequences.

We are building the defender brain now 🧠🔍

---

## 🎓 Roadmap Certification Checkpoint

**CompTIA Security+**

This phase aligns the practical labs with foundational security concepts covered by the roadmap’s Security+ checkpoint.

The exam vocabulary matters, but the mini-projects make the vocabulary real.

---

## 🎯 What This Phase Covers

### 🔐 Core Security Principles

- CIA triad
- Authentication and MFA
- Identity and access concepts
- Hashing and password security
- Encryption basics
- Access control and least privilege

### 📜 Logging, SIEM, and Monitoring

- SIEM fundamentals
- Windows logs and syslog
- Basic log parsing
- Splunk introduction
- Security dashboards
- Cloud logging introduction with CloudTrail

### 🧠 Threats, Intelligence, and Detection

- Threat intelligence
- IOC tracking with OTX or MISP concepts
- MITRE ATT&CK mapping
- Detection-rule fundamentals
- Sigma rules
- Brute-force detection patterns

### 🚨 Investigation and Response

- Incident-response lifecycle
- NIST incident-response flow
- Threat-hunting basics
- SOC investigation practice
- Alert and evidence workflow

### 🌐 Network Defense

- Wireshark and packet analysis
- Firewalls
- VPNs
- Zero Trust concepts
- Network traffic awareness

### 🛡️ Vulnerability, AppSec, and Governance

- Vulnerability management
- Nessus introduction
- OWASP Top 10
- Security policies
- ISO 27001 introduction
- NIST Risk Management Framework
- Risk registers
- Linux hardening with Lynis
- Windows security basics

---

## 🧰 Why This Matters

Data platforms and cloud systems are security systems whether the project plan admits it or not.

They contain identities, secrets, APIs, databases, storage, network paths, logs, and business data. Every one of those can be misconfigured, abused, exposed, or misunderstood.

This phase builds the ability to ask better questions:

- Who should have access?
- What evidence would an attack leave?
- What does normal activity look like?
- Which control reduces the risk?
- How would I investigate this alert?
- What is the business impact?

That is the difference between memorising security terms and actually beginning to think like a defender.

---

## 🗺️ Roadmap Learning Path

1. Learn the CIA triad and foundational security principles
2. Understand authentication, MFA, hashing, passwords, and encryption
3. Map the flow of logs into a SIEM
4. Parse Windows and Linux log samples
5. Track indicators of compromise
6. Map suspicious behaviour to MITRE ATT&CK
7. Learn incident-response and threat-hunting workflows
8. Inspect packets with Wireshark
9. Design basic firewall, VPN, and Zero Trust notes
10. Apply IAM and least privilege
11. Review vulnerabilities, OWASP risks, governance, and risk
12. Harden Linux and Windows systems
13. Write a Sigma rule and investigate a brute-force scenario
14. Combine everything in a mini SIEM project

---

## 📁 What You’ll Find in This Folder

```text
02-networking-security-basics/
├── README.md
└── day-projects/
    ├── day-01-cia-triad/
    ├── day-02-authentication-and-mfa/
    ├── day-03-hashing-and-passwords/
    ├── day-04-encryption-basics/
    ├── day-05-siem-architecture/
    ├── day-06-windows-and-syslog-parsing/
    ├── day-07-threat-intelligence-and-iocs/
    ├── day-08-mitre-attack-mapping/
    ├── day-09-incident-response/
    ├── day-10-threat-hunting/
    ├── day-11-wireshark-packet-analysis/
    ├── day-12-firewalls-vpns-zero-trust/
    ├── day-13-iam-least-privilege/
    ├── day-14-vulnerability-management/
    ├── day-15-owasp-and-appsec/
    ├── day-16-governance-risk-and-policy/
    ├── day-17-security-monitoring/
    ├── day-18-linux-and-windows-hardening/
    ├── day-19-sigma-detection-rule/
    ├── day-20-soc-investigation/
    ├── day-21-cloudtrail-introduction/
    └── day-22-mini-siem-capstone/
```

---

## 🧪 Portfolio Artifacts From This Phase

- `notes/cia-triad-security-principles.md`
- `diagrams/authentication-and-mfa-flow.png`
- `labs/password-hashing-notes.md`
- `labs/file-encryption-demo/README.md`
- `diagrams/siem-architecture.png`
- `parsers/windows-syslog-parser.py`
- `threat-intel/ioc-tracker.csv`
- `mitre/attack-mapping-sheet.md`
- `incident-response/ir-flowchart.png`
- `threat-hunting/brute-force-hunt.md`
- `wireshark/packet-analysis-notes.md`
- `network-security/firewall-rules-diagram.png`
- `zero-trust/zero-trust-notes.md`
- `iam/least-privilege-design.json`
- `vulnerability-management/sample-report.md`
- `appsec/secure-login-checklist.md`
- `governance/acceptable-use-policy.md`
- `risk/risk-register.csv`
- `monitoring/basic-security-dashboard.png`
- `hardening/linux-lynis-report.md`
- `hardening/windows-security-baseline.md`
- `detections/brute-force-sigma-rule.yml`
- `investigations/brute-force-case-report.md`
- `cloud-logging/cloudtrail-audit-notes.md`
- `capstone/mini-siem-lab/README.md`

This phase turns theory into evidence: diagrams, rules, reports, hardening notes, parsed logs, and an investigation trail.

The defender brain now has paperwork, and surprisingly, the paperwork is useful 📋🔥

---

## 🧠 Skills Gained Here

By the end of this phase, I should be able to:

- Explain confidentiality, integrity, and availability
- Distinguish authentication from authorization
- Explain MFA, hashing, encryption, and password risks
- Describe how logs move into a SIEM
- Parse basic Windows and Linux logs
- Track and enrich indicators of compromise
- Map suspicious behaviour to MITRE ATT&CK
- Describe the incident-response lifecycle
- Conduct a beginner threat hunt
- Inspect packet captures at a foundational level
- Explain firewalls, VPNs, and Zero Trust
- Design a basic least-privilege access model
- Document vulnerabilities and business risk
- Recognise common OWASP issues
- Draft basic policies and a risk register
- Harden beginner Linux and Windows environments
- Write and explain a Sigma detection rule
- Investigate a simple brute-force scenario

---

## 🌍 Real-World Connection

This phase connects directly to:

- SOC analyst work
- Cloud security operations
- Incident response
- Threat intelligence
- Detection engineering
- IAM reviews
- Vulnerability management
- Governance, risk, and compliance
- Endpoint and server hardening
- Cloud logging and monitoring

A cloud or data engineer who understands security builds safer systems.

A security engineer who understands networks and logs investigates faster.

This phase starts connecting both sides of that bridge 🌉🔐

---

## 🏁 Phase Capstone: Mini SIEM Lab

The capstone combines multiple tools and concepts into a small end-to-end security workflow:

1. Generate or collect safe sample Linux, Windows, or cloud logs
2. Parse and normalize selected fields
3. Identify a suspicious brute-force pattern
4. Write a detection rule
5. Map the behaviour to MITRE ATT&CK
6. Display the activity in a simple dashboard
7. Document triage steps
8. Write a concise incident report
9. Recommend hardening and monitoring improvements

The project should demonstrate the full loop:

```text
Telemetry → Parsing → Detection → Triage → Investigation → Response → Improvement
```

---

## ✅ Phase Completion Checklist

- [ ] I can explain the main security principles in my own words
- [ ] I understand authentication, MFA, hashing, and encryption
- [ ] I diagrammed a SIEM logging pipeline
- [ ] I parsed sample Windows or Linux logs
- [ ] I built an IOC tracker
- [ ] I mapped suspicious activity to MITRE ATT&CK
- [ ] I documented an incident-response workflow
- [ ] I completed a beginner threat hunt
- [ ] I inspected traffic in Wireshark
- [ ] I documented firewall, VPN, and Zero Trust concepts
- [ ] I designed a least-privilege access example
- [ ] I produced vulnerability, risk, and hardening artifacts
- [ ] I wrote and tested a Sigma rule
- [ ] I completed a SOC investigation report
- [ ] I published the mini SIEM capstone

---

## 🔜 What Comes Next

Next is **Data Engineering Foundations**.

The defender brain stays online, but now the focus shifts to building reliable data systems: formats, pandas, SQL, PostgreSQL, ETL, APIs, validation, logging, retries, and Docker.

Because a detection platform is only as good as the pipelines feeding it 📊🚰

[⬅️ Previous Phase: Tech Foundations](../01-tech-foundations/README.md) | [Main Roadmap](../README.md) | [Next Phase: Data Engineering Foundations ➡️](../03-data-engineering-foundations/README.md)
