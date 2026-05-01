import hashlib
import json
from pathlib import Path
from datetime import datetime
#hello
class PyHashEngine:
    def __init__(self, target_dir, algorithm="sha256"):
        self.target_dir = Path(target_dir).resolve()
        self.algorithm = algorithm
        self.manifest = {}

    def get_file_hash(self, file_path):
        """Hashes files in 4KB chunks to keep your 2-core VM stable."""
        hasher = hashlib.new(self.algorithm)
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except (PermissionError, OSError):
            return None

    def collect(self):
        """Recursively scans the directory and builds the manifest."""
        print(f"[*] Scanning: {self.target_dir}")
        for path in self.target_dir.rglob("*"):
            if path.is_file():
                rel_path = str(path.relative_to(self.target_dir))
                file_hash = self.get_file_hash(path)
                if file_hash:
                    self.manifest[rel_path] = {
                        "hash": file_hash,
                        "last_seen": datetime.now().isoformat()
                    }
        return self.manifest

    def save_manifest(self, output_file="baseline.json"):
        with open(output_file, "w") as f:
            json.dump(self.manifest, f, indent=4)
        print(f"[+] Manifest saved to {output_file}")