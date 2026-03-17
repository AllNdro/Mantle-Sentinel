# MantleSentinel

AI-powered DeFi automation agent on Mantle.

## 🚀 Overview

MantleSentinel monitors token prices on Mantle DEX and automatically executes swaps when predefined conditions are met.

Example:
- Monitor MNT
- If price drops ≥10%
- Swap to mETH
- Send Telegram notification

---

## ⚙️ Features

- Natural language strategy input
- Real-time price monitoring
- Automated swap execution
- Telegram notifications
- Mantle smart contract integration

---

## 🏗 Architecture

User → AI Agent → Strategy Engine → Execution Bot → Smart Contract → DEX → Telegram

---

## 📦 Installation

```bash
git clone https://github.com/AllNdro/mantle-sentinel.git
cd mantle-sentinel
pip install -r requirements.txt
