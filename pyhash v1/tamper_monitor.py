import time

print(" MONITOR ACTIVE: Scanning with Alert Suppression...")
alerted_files = {} 

try:
    while True:
        current_files = os.listdir('secure_vault')
        
        for filename in current_files:
            path = os.path.join('secure_vault', filename)
            current_hash = get_file_hash(path)
            
            if filename in baseline:
                if current_hash != baseline[filename]:
                    if filename not in alerted_files:
                        print(f" ALERT [{time.strftime('%H:%M:%S')}]: {filename} MODIFIED!")
                        alerted_files[filename] = True
                else:
                    if filename in alerted_files:
                        print(f" RESOLVED [{time.strftime('%H:%M:%S')}]: {filename} is back to baseline.")
                        del alerted_files[filename]
        else:
          print(f"  [{time.strftime('%H:%M:%S')}]: nothing happened")    
        time.sleep(300)

except KeyboardInterrupt:
    print("\nMonitor stopped by user.")
