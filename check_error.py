import os
import platform
import time

def is_accessible(path):
    return os.access(path, os.R_OK)

def scan_system(start_path='/'):
    error_log = []
    print(f"Scanning started on {platform.system()} {platform.release()} from {start_path}")
    print("-" * 50)
    
    file_count = 0
    start_time = time.time()

    for root, dirs, files in os.walk(start_path, topdown=True, onerror=None):
        # Skip very large system directories if needed
        # Example: if 'proc' in root: continue
        
        # Check directories
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not is_accessible(dir_path):
                error_log.append(f"[DIR INACCESSIBLE] {dir_path}")

        # Check files
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if not os.path.exists(file_path):
                error_log.append(f"[MISSING] {file_path}")
            elif not is_accessible(file_path):
                error_log.append(f"[FILE INACCESSIBLE] {file_path}")
            else:
                try:
                    with open(file_path, 'rb') as f:
                        f.read(1024)  # Attempt to read first 1KB
                except Exception as e:
                    error_log.append(f"[CORRUPT/ERROR] {file_path} - {str(e)}")
            file_count += 1

    duration = time.time() - start_time
    print(f"\nScan completed in {duration:.2f} seconds. Files scanned: {file_count}")
    print(f"Errors found: {len(error_log)}")

    if error_log:
        with open("error_report.txt", "w") as log_file:
            for error in error_log:
                log_file.write(error + "\n")
        print("Error report saved to: error_report.txt")
    else:
        print("No file access issues found.")

# Choose OS root path based on system
default_root = "C:\\" if platform.system() == "Windows" else "/"

# Start scanning
scan_system(default_root)
