import re
import pandas as pd

log_file = "Input/input.log"

# Regex patterns
request_pattern = re.compile(
    r'(?P<date>\d{4}-\d{2}-\d{2})\s+'
    r'(?P<time>\d{2}:\d{2}:\d{2}),\d+\s+'
    r'\(glastopf\.glastopf\)\s+'
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+requested\s+'
    r'(?P<method>GET|POST)\s+'
    r'(?P<path>\S+)',
    re.IGNORECASE
)

attack_pattern = re.compile(
    r'Glaspot:\s+(?P<attack>[\w_]+)\s+attack\s+method\s+from\s+'
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)',
    re.IGNORECASE
)

rows = []

with open(log_file, "r", errors="ignore") as f:
    for line in f:
        req = request_pattern.search(line)
        atk = attack_pattern.search(line)

        if req:
            rows.append({
                "date": req.group("date"),
                "time": req.group("time"),
                "source_ip": req.group("ip"),
                "http_method": req.group("method"),
                "path": req.group("path"),
                "attack_type": "unknown",
                "raw_log": line.strip()
            })

        elif atk:
            rows.append({
                "date": "",
                "time": "",
                "source_ip": atk.group("ip"),
                "http_method": "",
                "path": "",
                "attack_type": atk.group("attack"),
                "raw_log": line.strip()
            })

df = pd.DataFrame(rows)
df.to_csv("Csv/parsed/parsed.csv", index=False)

print("[+] parsed.csv created")
print(df.head())