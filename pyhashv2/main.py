import sys
from engine import PyHashEngine
from audit import verify_integrity, report_findings

def main():
    # Example usage: python main.py --scan /home/harsh/projects
    mode = sys.argv[1] # --baseline or --audit
    target = sys.argv[2] # directory path

    engine = PyHashEngine(target)
    
    if mode == "--baseline":
        current_data = engine.collect()
        engine.save_manifest("baseline.json")
        print("[+] Baseline created successfully.")

    elif mode == "--audit":
        print("[*] Starting Integrity Audit...")
        current_scan = engine.collect()
        # We compare the fresh scan against the saved baseline
        results = verify_integrity("baseline.json", current_scan, secret_key="YOUR_HIDDEN_SALT")
        report_findings(results)

if __name__ == "__main__":
    main()
