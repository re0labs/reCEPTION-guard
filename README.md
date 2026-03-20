# reCEPTION-guard

#### [Website](https://reception.re-labs.io/) | [Pitchdeck](https://drive.google.com/file/d/1EzFJzVdejq8URAUaYuzT9ZngMDU1ovjZ/view?usp=sharing) | [Demo Video](https://drive.google.com/file/d/15yUrV_xFOKiHhtgf83bEdw6FBIt6E3p9/view?usp=sharing)

# AI Hook Guard

**For evaluation:** this repository supports an offline mode and does **not** require an OpenAI API key to run the core demo.

AI Hook Guard is a hybrid security system for Solidity hooks that detects vulnerabilities, scores risk, and suggests fixes before deployment, while also offering Solidity guard modules like access control, reentrancy protection, and delta validation to help developers build safer smart contracts.

---

## Overview

AI Hook Guard combines two security layers:

1. **Python analysis layer**  
   Detects risky patterns in Solidity hook code before deployment.

2. **Solidity protection layer**  
   Provides safer smart contract patterns and modules for hook-based systems.

This project also includes **Foundry tests** that demonstrate the difference between vulnerable and protected contract behavior.

---

## Offline Evaluation Mode

This repository includes an **offline-capable version** for judging and local testing.

The offline mode allows the project to run **without an OpenAI API key**.

In offline mode:

- vulnerability detectors still run
- risk scoring still works
- recommendations and patch suggestions still work
- the explanation layer falls back to a local built-in summary

This means the core functionality can be evaluated directly from the repository without external API credentials.

---

## Features

### Python analyzer
- Reentrancy detection
- Unsafe external call detection
- Missing PoolManager verification detection
- Incorrect delta accounting detection
- State corruption risk detection
- Risk scoring
- Patch recommendations
- Offline local explanation mode

### Solidity security framework
- PoolManager access control
- Reentrancy protection
- Delta validation
- Secure demo contract
- Vulnerable demo contract

### Testing
- Foundry test suite for secure and vulnerable examples
- Demonstrates both unsafe and protected behaviors
- Useful for education, validation, and demos

---

## Project Structure

```text
AI-SDK.relabsV01/
├── ai_hook_guard/          # Python analysis SDK
├── contracts/              # Solidity security framework
├── test/                   # Foundry tests
├── examples/               # Python example scripts
├── run_guard_demo.py       # Simple offline demo script
├── foundry.toml            # Foundry configuration
├── requirements.txt        # Python dependencies
└── README.md 


## Quick Start 

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-SDK.relabsV01

## Quick Start for Judge

### 2. Install Python dependencies

pip install -r requirements.txt

### 3. Run the offline demo

python run_guard_demo.py

### 4. Run SOLIDITY TESTS

forge build
forge test -vv

