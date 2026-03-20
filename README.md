# reCEPTION-guard
AI Hook Guard is a hybrid security system for Solidity hooks that detects vulnerabilities, scores risk, and suggests fixes before deployment, while also offering Solidity guard modules like access control, reentrancy protection, and delta validation to help developers build safer smart contracts.

# AI Hook Guard

AI Hook Guard is a hybrid smart contract security project with:

- a Python analyzer for detecting risky hook patterns before deployment
- a Solidity security framework for building safer Uniswap-style hooks
- Foundry tests demonstrating vulnerable and protected behaviors

## Features

### Python analyzer
- Reentrancy detection
- Unsafe external call detection
- Missing PoolManager verification detection
- Incorrect delta accounting detection
- State corruption risk detection
- Risk scoring and patch recommendations

### Solidity security framework
- PoolManager access control
- Reentrancy protection
- Delta validation
- Demo secure hook implementation

## Project structure

- `ai_hook_guard/` Python analysis SDK
- `contracts/` Solidity guard framework
- `test/` Foundry tests
- `examples/` Python test script

## Run Python example

```bash
python -m examples.test_guard
