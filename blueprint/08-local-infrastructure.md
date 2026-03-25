# Section 8: Local Agent Infrastructure

> **Journey Step:** Step 4 — Build

---

## The principle

An AI agent is only as capable as the infrastructure it runs on. This section defines the reference architecture for the local agent environment — the hardware, operating system, network configuration, application stack, and monitoring inputs that together constitute a production-ready local AI deployment for an SME IT Manager.

This is a verified, deployable reference. Every component listed has been selected for being open source or low-cost, operationally maintainable by a small team, and aligned with the data sovereignty standard in Section 2.

The architecture is hybrid by design. Local infrastructure handles all data-sensitive processing. Frontier cloud models are used as a deliberate, governed exception for specific tasks — principally complex code generation and architectural reasoning, where locally-hosted models are not yet producing the required output quality and where the data involved is classified as Internal or Public.

---

## Hardware reference specification

The local agent server is dedicated hardware. Not a VM on shared infrastructure. Not a repurposed workstation. A server with defined specifications, managed as a production system, backed up on a schedule, and documented in the asset register.

### Minimum viable specification
Suitable for lightweight model inference. Adequate for Phi-3 Mini, Llama 3 8B, and equivalent models.

| Component | Minimum Specification |
|-----------|----------------------|
| CPU | 8-core x86-64, modern generation (Intel i7/Xeon or AMD Ryzen/EPYC) |
| RAM | 32 GB ECC DDR4 |
| GPU | NVIDIA GPU with 8 GB VRAM minimum (RTX 3060 or equivalent) |
| Primary storage | 500 GB NVMe SSD |
| Secondary storage | 2 TB HDD or NAS mount |
| Network | 1 Gbps wired, dedicated NIC |
| OS | Ubuntu Server 22.04 LTS or Debian 12 |

### Recommended production specification
Suitable for mid-range model inference (Llama 3 70B, Mistral Large) and concurrent agent workloads.

| Component | Recommended Specification |
|-----------|--------------------------|
| CPU | 16-core server-grade processor |
| RAM | 64 GB ECC DDR4 or DDR5 |
| GPU | NVIDIA GPU with 24–48 GB VRAM (RTX 4090, RTX 6000 Ada, or A100 40 GB) |
| Primary storage | 1 TB NVMe SSD (RAID 1 recommended) |
| Secondary storage | 4–8 TB dedicated storage (RAID 5 or NAS) |
| Network | Dual 1 Gbps or 10 Gbps wired |
| OS | Ubuntu Server 22.04 LTS |
| UPS | Online UPS with sufficient runtime for clean shutdown |

> **On GPU selection:** VRAM is the binding constraint for local model inference. A model that does not fit in VRAM will either fail to load or fall back to CPU inference with unacceptable latency for interactive tasks. Buy the GPU tier appropriate for the model tier you need. Upgrading GPU is easier than re-architecting around insufficient VRAM.

---

## Operating system and hardening

**Base OS: Ubuntu Server 22.04 LTS**

Key hardening steps applied to the base installation:
- Disable root SSH login — key-based authentication only
- Configure UFW (Uncomplicated Firewall) — default deny inbound, allow only defined service ports
- Enable unattended-upgrades for security patches
- Install and configure fail2ban for SSH brute-force protection
- Configure NTP to a reliable time source — critical for log correlation
- Enable audit logging via auditd
- Full disk encryption where the physical security of the hardware cannot be guaranteed

---

## Application stack — what runs where

### Bare metal (runs directly on the host)
- **Ollama** — local model inference server
- **OpenClaw** — agent orchestration platform
- **NVIDIA drivers and CUDA toolkit**

### Docker Compose (containerised services)
- Apache / MariaDB / PHP stack (LAMP)
- ISPConfig control panel
- Grafana + Prometheus (monitoring)
- Gitea (local Git — no public Git, all repositories self-hosted)
- Portainer (Docker management UI — optional)

This separation keeps the GPU-dependent inference stack on bare metal where it performs best, while application and monitoring services benefit from container isolation and easy update management.

---

## Network architecture and physical security

### Architecture principle

The OpenClaw agent server is dedicated, standalone hardware. It does not share a chassis, hypervisor, or network segment with any other business service.

All other services (OpenBrain/PostgreSQL, ISPConfig, LAMP stack, Gitea, Grafana, Prometheus, Vault) run on the business virtualisation layer as separate virtual machines, on LAN-facing infrastructure managed alongside other business-critical systems.

This separation serves two purposes:
1. **Network security:** The agent server executes code autonomously and has direct connections to external APIs. A compromise of the agent server cannot propagate directly to business-critical data systems.
2. **Physical security:** The agent server can be physically powered off in seconds by a single person. When the agents need to be stopped, they stop. No software process can prevent a physical shutdown.

### Infrastructure layout

```
DEDICATED AGENT HARDWARE (physical, standalone)
┌──────────────────────────────────────────────────┐
│  OpenClaw (bare metal)                           │
│  Ollama (bare metal, GPU)                        │
│  Claude Code CLI / Codex CLI                     │
│  UFW: tight inbound/outbound rules               │
│  Physical kill: power off = all agents stop      │
└──────────────────────────────────────────────────┘
              │  LAN (restricted VLAN)
              │  Outbound: OpenBrain API, Gitea, Grafana
              │  Outbound: OpenRouter HTTPS (governed)
              │  Outbound: M365/Google APIs (governed exceptions)
              │  Inbound: IT Manager workstation only

BUSINESS VIRTUALISATION LAYER (Proxmox / VMware)
┌──────────────────────────────────────────────────┐
│  VM: OpenBrain (PostgreSQL + pgvector)            │
│      Port 8000 (MCP), Port 5432 (PostgreSQL)     │
│  VM: Application Server (ISPConfig, Apache, etc) │
│  VM: Development Services (Gitea)                │
│  VM: Monitoring Stack (Grafana, Prometheus, Loki) │
│  VM: Security Services (HashiCorp Vault)         │
└──────────────────────────────────────────────────┘
```

### Agent server network rules

**Inbound (permitted):**
- SSH from IT Manager workstation IP only
- HTTPS to OpenClaw interface from IT Manager workstation IP only

**Outbound (permitted):**
- HTTPS to OpenBrain VM (ports 8000 MCP, 5432 PostgreSQL)
- HTTPS to Gitea VM (port 3000)
- HTTPS to Vault VM (port 8200)
- HTTPS to Grafana AlertManager VM (port 9093)
- HTTPS to OpenRouter (api.openrouter.ai, port 443)
- HTTPS to graph.microsoft.com (M365 API, governed)
- HTTPS to admin.googleapis.com (Google Workspace API, governed)
- HTTPS to package repositories (defined list only)

**All other traffic: denied and logged.**

### Physical security requirements

- Agent server in a locked physical location accessible only to the IT Manager and a named deputy
- Power button accessible without unlocking any software system
- UPS providing runtime sufficient for a clean shutdown (not continued operation)
- IT Manager and deputy are the only individuals with physical location key or code
- Physical shutdown procedure documented in the DR runbook

---

## Implementation checklist

- [ ] Procure dedicated hardware meeting at minimum the minimum viable specification
- [ ] Install Ubuntu Server 22.04 LTS and apply all hardening steps
- [ ] Install NVIDIA drivers and CUDA toolkit — verify GPU is detected
- [ ] Install Ollama and pull the first model tier (Phi-3 Mini or Llama 3 8B)
- [ ] Deploy Docker Compose application stack — Apache, MariaDB, Gitea, Grafana, Prometheus
- [ ] Install HashiCorp Vault — initialise and store root token securely
- [ ] Configure UFW with the rules defined in the network architecture
- [ ] Place agent server on a dedicated VLAN or network segment
- [ ] Configure the virtualisation layer VMs — OpenBrain, Gitea, monitoring stack
- [ ] Document the physical security arrangement and the shutdown procedure

---

## Tools & Skills

| Tool | Use |
|------|-----|
| [`tools/open-brain-context.md`](../tools/open-brain-context.md) | OpenBrain runs on the business virtualisation layer — not the agent server |

**Related sections:** [Section 3 — AI Agent Architecture](03-ai-agent-architecture.md) · [Section 11 — Backup & DR](11-backup-disaster-recovery.md)
