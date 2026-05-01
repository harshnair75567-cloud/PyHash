import json
import hmac
import hashlib

def verify_integrity(baseline_path, current_scan, secret_key):
    with open(baseline_path, 'r') as f:
        baseline = json.load(f)

    changes = {"added": [], "modified": [], "deleted": []}

    for rel_path, data in baseline.items():
        if rel_path not in current_scan:
            changes["deleted"].append(rel_path)
        else:
            if current_scan[rel_path]["hash"] != data["hash"]:
                changes["modified"].append(rel_path)

    for rel_path in current_scan:
        if rel_path not in baseline:
            changes["added"].append(rel_path)

    return changes

def report_findings(changes):
    if not any(changes.values()):
        print("\n[✓] Integrity Verified: No changes detected.")
        return

    print("\n[!] ALERT: Integrity Breach Detected!")
    for change_type, files in changes.items():
        if files:
            print(f"  {change_type.upper()}:")
            for f in files:
                print(f"    - {f}")
