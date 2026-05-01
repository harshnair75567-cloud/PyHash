PyHash is a Python-based security tool designed to detect unauthorized file tampering, malware injections, and backdoor creations in real-time. By utilizing the SHA-256 cryptographic algorithm, it ensures that any modification to sensitive system files—no matter how small—is immediately flagged.

 Project Overview
The project is divided into two distinct versions representing the evolution from a basic script to a modular security tool.

PyHash v1: The Foundation
This version focuses on the core mechanics of baseline comparison.

baseline_setup.py: Generates the initial "gold standard" cryptographic hashes for a target directory.

tamper_monitor.py: The active monitoring agent that compares current file states against the baseline.

attack_tester.py: A utility designed to simulate file modifications to verify that the monitoring system triggers alerts correctly.

PyHash v2: Modular Blue Team Tooling
The second iteration refines the process into a modular architecture suitable for integration into larger security labs.

main.py: The orchestrator and entry point for the application.

engine.py: The core cryptographic processing unit that handles high-speed hashing and comparison logic.

audit.py: Generates detailed forensic reports on file changes, providing visibility into exactly what was altered and when.

 Technical Features
Cryptographic Integrity: Uses SHA-256 to ensure collision-resistant file verification.

Modular Architecture: Separates the hashing engine from the reporting logic for easier maintenance and scalability.

Blue Team Focused: Designed specifically for students and professionals looking to understand defensive security operations.

 Getting Started
Prerequisites
Python 3.11+ (Optimized for modern standard libraries)

Recommended: Standard libraries (hashlib, os, time)

Usage
Generate Baseline: Run the setup script to index your protected files.

Start Monitoring: Launch the monitor to track real-time changes.

Audit Results: Review generated logs to investigate potential security breaches.

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.
