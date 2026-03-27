import os
import hashlib
def get_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        sha256_hash.update(f.read())
    return sha256_hash.hexdigest()
os.makedirs('secure_vault', exist_ok=True)
with open('secure_vault/config.txt', 'w') as f:
    f.write('System Status: Secure\nBuild: 1.0.4')
baseline = {}
files = os.listdir('secure_vault')
for filename in files:
    path = os.path.join('secure_vault', filename)
    baseline[filename] = get_file_hash(path)

print(" BASELINE SECURED.")
print(f"Recorded {len(baseline)} file fingerprints.")
