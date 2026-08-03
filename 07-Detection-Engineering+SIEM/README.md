# 📜🚨🕵🏽 Detection Engineering + SIEM

## The Logs Are Talking, Build Better Ears 👂🏽📊

Welcome to the **Detection Engineering + SIEM** phase of my Cloud Data & Security Engineering roadmap.

Prevention matters, but prevention eventually misses something.

When that happens, the quality of the logs, detections, alert logic, triage process, and investigation notes determines whether the suspicious activity becomes a useful signal or disappears into a dashboard-shaped swamp.

This phase focuses on the complete detection lifecycle:

```text
Collect → Parse → Normalize → Detect → Triage → Investigate → Tune → Document
```

The goal is not to create the loudest alert.

The goal is to create an alert that is explainable, testable, useful, and worth waking someone up for 🚨😴

---

## 🎓 Roadmap Certification Checkpoint

**Microsoft Security, Compliance, and Identity Fundamentals (SC-900)**

The roadmap uses this phase to reinforce security, compliance, identity, and monitoring concepts while the hands-on work focuses on practical detection engineering.

---

## 🎯 What This Phase Covers

### 📡 SIEM and Log Foundations

- SIEM fundamentals review
- Splunk and ELK concepts
- Log-source inventory
- AWS, Linux, and Windows logs
- Source mapping
- Cloud-log ingestion

### 🐍 Parsing and Analysis

- Python log parsing
- Regular expressions
- Jupyter notebooks for security analysis
- Field extraction and investigation workflow

### 📜 Detection Engineering

- Detection-engineering lifecycle
- Sigma rules
- MITRE ATT&CK mapping
- Rule testing
- Detection documentation

### 🚨 Alert Operations

- Alert triage
- Investigation worksheets
- False positives
- Detection tuning
- Detection quality

### 🏹 Threat Hunting and Incident Reporting

- Threat-hunting workflow
- Suspicious-activity hunts
- Incident-report writing
- Evidence and timeline notes

### 🧠 Threat Intelligence and Dashboarding

- Threat-intelligence feeds
- IOC-ingestion scripts
- Grafana or QuickSight dashboards
- Incident and detection metrics

---

## 🧰 Why This Matters

Security teams drown when telemetry is abundant but meaning is scarce.

A useful detection engineer understands both the data and the threat:

- Where did the event come from?
- Which fields can be trusted?
- What behaviour does the rule represent?
- Which ATT&CK technique does it map to?
- What is the likely false-positive pattern?
- What evidence should the analyst inspect next?
- How will the rule be tested and maintained?

This phase sits directly at the intersection of data engineering and security operations.

It is where logs become security decisions.

---

## 🗺️ Roadmap Learning Path

1. Review SIEM architecture and terminology
2. Build a log-source map for AWS, Linux, and Windows
3. Parse sample logs with Python and regex
4. Write a Sigma detection rule
5. Map three behaviours to MITRE ATT&CK
6. Build an alert-triage worksheet
7. Tune a noisy alert
8. Run a threat-hunting workflow
9. Write an incident report
10. Ingest cloud logs into a SIEM-style stack
11. Build an IOC-ingestion script
12. Analyze security data in Jupyter
13. Create an incident dashboard
14. Build and publish the phase detection lab

---

## 📁 What You’ll Find in This Folder

```text
07-detection-engineering-siem/
├── README.md
└── day-projects/
    ├── day-01-siem-foundations/
    ├── day-02-log-source-mapping/
    ├── day-03-python-log-parser/
    ├── day-04-sigma-detection-rule/
    ├── day-05-mitre-attack-mapping/
    ├── day-06-alert-triage/
    ├── day-07-false-positive-tuning/
    ├── day-08-threat-hunting/
    ├── day-09-incident-report-writing/
    ├── day-10-cloud-log-ingestion/
    ├── day-11-threat-intel-ingestion/
    ├── day-12-jupyter-security-analysis/
    ├── day-13-incident-dashboard/
    └── day-14-to-15-detection-capstone/
```

---

## 🧪 Portfolio Artifacts From This Phase

- `notes/siem-architecture.md`
- `log-sources/aws-linux-windows-source-map.md`
- `parsers/python-log-parser.py`
- `parsers/field-normalization-notes.md`
- `detections/suspicious-authentication.yml`
- `mitre/three-technique-mapping.md`
- `triage/alert-triage-worksheet.md`
- `tuning/noisy-alert-before-after.md`
- `hunts/suspicious-activity-hunt.md`
- `incidents/sample-incident-report.md`
- `pipelines/cloud-log-ingestion/`
- `threat-intel/ioc-ingestion-script.py`
- `notebooks/security-analysis.ipynb`
- `dashboards/incident-dashboard.png`
- `capstone/cloud-detection-lab/`

These artifacts prove that I can move from raw events to investigation-ready security signals.

Not every log deserves an alert. Not every alert deserves panic. Context is the whole meal 🍽️📜

---

## 🧠 Skills Gained Here

By the end of this phase, I should be able to:

- Explain how a SIEM collects and processes data
- Inventory and map security log sources
- Parse logs with Python and regex
- Identify useful detection fields
- Write and explain Sigma rules
- Map detections to MITRE ATT&CK
- Triage alerts consistently
- Identify and reduce false positives
- Conduct a structured threat hunt
- Write a professional incident report
- Ingest cloud logs into an analytical stack
- Automate IOC ingestion
- Use Jupyter for security analysis
- Build dashboards that support investigation
- Document rule assumptions, limitations, and tests

---

## 🌍 Real-World Connection

This phase connects directly to:

- Detection engineering
- SOC analysis
- Threat hunting
- Security data engineering
- Incident response
- SIEM content engineering
- Cloud security monitoring
- Threat-intelligence operations
- Security analytics

Detection engineering is where the roadmap’s hybrid skill set becomes especially valuable.

The data-engineering side understands pipelines and fields.

The security side understands behaviour and risk.

Together, they build useful signals instead of expensive noise 🔔

---

## 🏁 Phase Capstone: Cloud Detection Lab

The capstone should include:

1. AWS, Linux, or Windows sample logs
2. A documented log-source map
3. A Python parser and normalized output
4. At least one Sigma rule
5. MITRE ATT&CK mapping
6. A simulated or safe suspicious scenario
7. Alert-triage steps
8. False-positive analysis and tuning
9. A threat-intelligence enrichment step
10. A Jupyter analysis notebook
11. An incident dashboard
12. A final investigation report
13. Rule-testing notes and known limitations

Suggested flow:

```text
Log Sources → Ingestion → Parsing → Detection → Enrichment
            → Dashboard → Triage → Investigation → Tuning
```

---

## ✅ Phase Completion Checklist

- [ ] I documented SIEM architecture
- [ ] I built a log-source map
- [ ] I parsed logs with Python
- [ ] I wrote a Sigma rule
- [ ] I mapped detections to MITRE ATT&CK
- [ ] I completed an alert-triage worksheet
- [ ] I tuned a noisy alert
- [ ] I conducted a threat hunt
- [ ] I wrote an incident report
- [ ] I ingested cloud logs
- [ ] I built an IOC-ingestion script
- [ ] I analyzed events in Jupyter
- [ ] I created an incident dashboard
- [ ] I published the complete detection lab

---

## 🔜 What Comes Next

Next is **DevSecOps + Advanced Automation**.

The detections and controls now move into delivery workflows: CI/CD, code scanning, dependencies, Terraform automation, container hardening, policy as code, secret scanning, remediation, runbooks, and security bots.

Less repetitive clicking. More reliable automation 🤖⚙️

[⬅️ Previous Phase: Cloud Security Engineering](../06-cloud-security-engineering/README.md) | [Main Roadmap](../README.md) | [Next Phase: DevSecOps + Advanced Automation ➡️](../08-devsecops-advanced-automation/README.md)
