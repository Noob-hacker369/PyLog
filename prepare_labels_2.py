import pandas as pd

df = pd.read_csv("Csv/parsed/parsed.csv")

def assign_label(row):
    path = str(row["path"]).lower()
    attack = str(row["attack_type"]).lower()

    if attack in ["sqli", "phpinfo", "robots"]:
        return 1        # attack
    if path in ["/", "/style.css", "/robots.txt", "/favicon.ico"]:
        return 0        # normal
    return -1           # unlabeled

df["label"] = df.apply(assign_label, axis=1)


df.to_csv("Csv/labeled/labeled.csv", index=False)
print(df["label"].value_counts())
