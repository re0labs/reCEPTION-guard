# reCEPTION-guard

#### [Website](https://reception.re-labs.io/) | [Pitchdeck](https://drive.google.com/file/d/1EzFJzVdejq8URAUaYuzT9ZngMDU1ovjZ/view?usp=sharing) | [Demo Video]()


```**For evaluation:** this repository supports an offline mode and does not require an OpenAI API key to run the core demo. ```

# AI Hook Guard

AI Hook Guard is a hybrid security system for Solidity hooks that detects vulnerabilities, scores risk, and suggests fixes before deployment, while also offering Solidity guard modules like access control, reentrancy protection, and delta validation to help developers build safer smart contracts.

This repository includes an **offline-capable version** for evaluation.  
The judge does **not** need an OpenAI API key to run the core demo.

---

## Offline Evaluation Version

This project can run in **offline mode**, which means:

- no OpenAI API key is required
- the Python analyzer still detects vulnerabilities
- risk scoring still works
- recommendations and patch suggestions still work
- the explanation layer falls back to a built-in local summary

This allows the project to be tested directly from the repository without external API credentials.

---

## Project Overview

AI Hook Guard is a hybrid smart contract security project with:

- a **Python analyzer** for detecting risky hook patterns before deployment
- a **Solidity security framework** for building safer hook-based contracts
- **Foundry tests** demonstrating vulnerable and protected behaviors

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
- Local offline explanation mode

### Solidity security framework
- PoolManager access control
- Reentrancy protection
- Delta validation
- Demo secure contract implementation
- Demo vulnerable contract implementation

---

## Project structure

- `ai_hook_guard/` → Python analysis SDK
- `contracts/` → Solidity guard framework
- `test/` → Foundry tests
- `examples/` → Python example scripts
- `run_guard_demo.py` → simple offline demo entry point

---

## Quick Start for Judge (Offline Mode)

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd AI-SDK.relabsV01
