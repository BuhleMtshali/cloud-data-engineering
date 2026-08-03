# ☁️🏗️⚙️ Cloud Foundations

## Learn the Sky Map Before Building the Sky City 🌍🗺️

Welcome to the **Cloud Foundations** phase of my Cloud Data & Security Engineering roadmap.

This phase introduces the services, architecture patterns, operational controls, and security boundaries that make cloud systems work.

The cloud is not a magical computer floating above Johannesburg with infinite RAM.

It is a collection of regions, availability zones, networks, identities, APIs, managed services, billing decisions, logs, and shared responsibilities.

This phase teaches me how those pieces fit together before I start building serious data platforms and security systems on top of them.

---

## 🎓 Roadmap Certification Checkpoint

**AWS Certified Solutions Architect - Associate**

The roadmap aligns this phase with architecture fundamentals: choosing services, designing networks, protecting access, building for availability, and understanding operational trade-offs.

---

## 🎯 What This Phase Covers

### ☁️ Core Cloud Concepts

- Cloud-computing fundamentals
- AWS global infrastructure
- Regions and availability zones
- Shared responsibility model
- Cloud-cost hygiene and AWS Budgets

### 🖥️ Compute, Storage, and Databases

- EC2 fundamentals
- S3 storage and secure buckets
- RDS managed databases
- Athena serverless querying
- Glue data catalog fundamentals

### 🔑 Identity and Network Security

- IAM deep dive
- Least-privilege policies
- Security groups
- VPC fundamentals
- Route tables
- Public and private subnets
- NAT concepts

### 📜 Monitoring and Auditability

- CloudWatch metrics, logs, and dashboards
- CloudTrail audit logs
- AWS security-service overview
- GuardDuty and Security Hub introduction

### 🛠️ Cloud Automation

- AWS CLI
- Boto3
- Lambda
- SNS and SQS
- Event-driven workflows

### 🏗️ Infrastructure and Platform Foundations

- Terraform fundamentals
- Variables and modules
- Docker multi-container concepts
- Kubernetes introduction
- Azure fundamentals and multi-cloud comparison
- Architecture review and documentation

---

## 🧰 Why This Matters

Cloud data and security projects fail in expensive ways when the foundation is vague.

A pipeline can be technically correct and still be dangerous because:

- IAM is too broad
- A bucket is public
- Network paths are misunderstood
- Logs are missing
- Costs are unbounded
- Resources cannot be reproduced
- The architecture has no failure plan

This phase builds the habit of seeing cloud systems as architectures rather than menus of services.

Clicking “Launch Instance” is easy.

Explaining why the instance exists, who can reach it, how it is monitored, what it costs, and what happens when it fails is engineering 🧠☁️

---

## 🗺️ Roadmap Learning Path

1. Learn cloud concepts and AWS global infrastructure
2. Launch and understand EC2
3. Create and secure S3 storage
4. Build least-privilege IAM policies
5. Control traffic with security groups
6. Design a VPC with public and private subnets
7. Understand routes and NAT
8. Create monitoring and audit trails
9. Use AWS CLI and Boto3
10. Build serverless functions and notification flows
11. Explore RDS, Athena, and Glue
12. Deploy infrastructure with Terraform
13. Review Docker, Kubernetes, and Azure fundamentals
14. Add cost controls and shared-responsibility documentation
15. Review AWS security services
16. Build and publish a secure cloud logging project

---

## 📁 What You’ll Find in This Folder

```text
04-cloud-foundations/
├── README.md
└── day-projects/
    ├── day-01-cloud-concepts/
    ├── day-02-aws-global-infrastructure/
    ├── day-03-ec2-basics/
    ├── day-04-s3-secure-bucket/
    ├── day-05-iam-least-privilege/
    ├── day-06-security-groups/
    ├── day-07-vpc-design/
    ├── day-08-routes-nat-public-private-subnets/
    ├── day-09-cloudwatch-monitoring/
    ├── day-10-cloudtrail-auditing/
    ├── day-11-aws-cli-and-boto3/
    ├── day-12-lambda-sns-sqs/
    ├── day-13-rds-athena-glue/
    ├── day-14-terraform-foundations/
    ├── day-15-docker-and-kubernetes-overview/
    ├── day-16-azure-fundamentals/
    ├── day-17-cost-and-shared-responsibility/
    ├── day-18-cloud-security-services/
    └── day-19-to-21-cloud-capstone/
```

---

## 🧪 Portfolio Artifacts From This Phase

- `notes/cloud-computing-models.md`
- `diagrams/aws-global-infrastructure.png`
- `labs/ec2-launch-and-access.md`
- `labs/secure-s3-bucket/`
- `iam/least-privilege-policy.json`
- `network/security-group-review.md`
- `diagrams/vpc-public-private-subnets.png`
- `network/route-table-and-nat-lab.md`
- `monitoring/cloudwatch-dashboard.png`
- `audit/cloudtrail-review.md`
- `automation/aws-cli-script.sh`
- `automation/boto3-s3-uploader.py`
- `serverless/lambda-alert-function.py`
- `messaging/sns-sqs-event-flow.png`
- `databases/rds-log-metadata-lab.md`
- `analytics/athena-s3-query.sql`
- `catalog/glue-catalog-lab.md`
- `terraform/ec2-deployment/`
- `terraform/modular-infrastructure/`
- `containers/multi-container-notes.md`
- `kubernetes/k8s-foundations.md`
- `multicloud/aws-vs-azure-notes.md`
- `governance/aws-budget-alert.md`
- `security/shared-responsibility-matrix.md`
- `architecture/secure-cloud-design.png`
- `capstone/secure-cloud-logging-system/`

---

## 🧠 Skills Gained Here

By the end of this phase, I should be able to:

- Explain cloud-computing and shared-responsibility concepts
- Navigate AWS regions and availability zones
- Launch and manage basic EC2 workloads
- Create and secure S3 buckets
- Design basic IAM policies
- Configure security groups
- Diagram a VPC with public and private subnets
- Explain route tables and NAT
- Create CloudWatch monitoring
- Use CloudTrail for audit visibility
- Automate AWS tasks with CLI and Boto3
- Build a simple Lambda function
- Explain SNS and SQS event flows
- Use RDS, Athena, and Glue at a foundational level
- Deploy simple infrastructure with Terraform
- Explain Docker, Kubernetes, and Azure at an introductory level
- Apply cost controls and architecture-review thinking

---

## 🌍 Real-World Connection

This phase connects directly to:

- Cloud engineering
- Cloud data engineering
- Cloud security operations
- Solutions architecture
- Platform engineering
- DevOps automation
- FinOps and governance
- Serverless development
- Infrastructure as code

Every later cloud project assumes this foundation exists.

Without it, architecture becomes service-name soup 🥣☁️

---

## 🏁 Phase Capstone: Secure Cloud Logging and Alerting System

The phase capstone should combine AWS and Python into a small but complete cloud system:

1. Generate or collect safe application or infrastructure logs
2. Store data securely in S3
3. Apply IAM least privilege
4. Enable audit logging
5. Process or respond to an event with Lambda
6. Send a notification through SNS
7. Create a CloudWatch view or dashboard
8. Document the network, identity, storage, monitoring, and cost decisions
9. Include an architecture diagram
10. Publish the project with setup, teardown, and lessons learned

Suggested flow:

```text
Workload/Event → Cloud Logging → S3 or CloudWatch → Lambda → SNS Alert
```

---

## ✅ Phase Completion Checklist

- [ ] I understand AWS global infrastructure
- [ ] I launched and documented EC2
- [ ] I built and secured an S3 bucket
- [ ] I wrote a least-privilege IAM policy
- [ ] I configured security groups
- [ ] I designed a VPC with public and private subnets
- [ ] I understand route tables and NAT
- [ ] I built CloudWatch monitoring
- [ ] I reviewed CloudTrail logs
- [ ] I used AWS CLI and Boto3
- [ ] I built a Lambda and notification workflow
- [ ] I explored RDS, Athena, and Glue
- [ ] I deployed infrastructure with Terraform
- [ ] I documented cost and shared responsibility
- [ ] I published the secure cloud logging capstone

---

## 🔜 What Comes Next

Next is **Cloud Data Engineering**.

The cloud services stop being isolated labs and begin forming complete pipelines: data lakes, ingestion, catalogs, queries, orchestration, transformations, quality checks, warehouses, and observability.

The sky map is learned. Time to build the plumbing ☁️🚰

[⬅️ Previous Phase: Data Engineering Foundations](../03-data-engineering-foundations/README.md) | [Main Roadmap](../README.md) | [Next Phase: Cloud Data Engineering ➡️](../05-cloud-data-engineering/README.md)
