import pandas as pd

df = pd.read_csv("Csv/parsed/parsed.csv")

ip_counts = df["source_ip"].value_counts()

def assign_label(row):
    path = str(row["path"]).lower()
    attack = str(row["attack_type"]).lower()

    if attack in ["sqli", "phpinfo", "xss"]:
        return 1

    if "?" in path and any(x in path for x in [
        "'", "%27", "--", "union", "select",
        " or ", "%20or%20", " and ", "%20and%20"
    ]):
        return 9  #sqli attack

    if "=" in path and any(x in path for x in [
        "sleep", "%28", "%29", "ls", "cat", "echo", "/bin/"
    ]):
        return 8 #command injuction

    if "=" in path and any(x in path for x in [
        "<script", "%3cscript", "<>", "<></>"
    ]):
        return 5 #xss

    if path in ["/", "/style.css", "/robots.txt", "/favicon.ico"]:
        return 0 #normal

    return -1  #somting abnormal


def prepare(func=assign_label):
    df["label"] = df.apply(func, axis=1)

    df["freq_label"] = df["source_ip"].fillna("0.0.0.0").map(
        lambda ip: 2 if ip_counts.get(ip, 0) >= 15 else 0
    )

    df.to_csv("Csv/labeled/labeled.csv", index=False)

    print("Label counts:")
    print(df["label"].value_counts())

    print("\nFrequency label counts:")
    print(df["freq_label"].value_counts())

if __name__ == "__main__":
    prepare()
