# LLaMA-Assisted Infrastructure Automation with Ansible

This project demonstrates how to combine **Ansible** with **AI-powered log analysis** using **Meta’s LLaMA** to streamline infrastructure automation workflows on Azure.

---

## Overview

- Run an Ansible playbook via **Azure Pipeline** to configure a client VM.
- Capture execution logs.
- Analyze logs with **LLaMA** for clear, human-readable insights.
- Helps validate automation outcomes without manually digging through logs.

---

## Repository Structure

├── ansible/  <br />
│ ├── hosts.ini # Inventory file  <br />
│ └── playbook.yml # Ansible playbook  <br />
├── scripts/  <br />
│ └── analyse_logs_llama.py # LLaMA log analysis script  <br />
├── ansible_log.txt # Sample Ansible log  <br />
├── analysis_output.txt # Sample LLaMA output  <br />
└── README.md

---

## Usage

1. Update `hosts.ini` with the client VM IP and credentials.
2. Run the playbook:
   
ansible-playbook -i ansible/hosts.ini ansible/playbook.yml

3. Analyse the logs:

python3 scripts/analyse_logs_llama.py ansible_log.txt > analysis_output.txt

Learning Outcomes:
- Automating infrastructure with Ansible.
- Using AI models to interpret automation logs.
- Enhancing DevOps workflows with AI-assisted insights.
