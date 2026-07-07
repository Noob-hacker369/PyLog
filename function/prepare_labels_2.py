import pandas as pd


def assign_label(row):
    path = str(row["path"]).lower()
    attack = str(row["attack_type"]).lower()

    if attack in ["sqli", "phpinfo", "xss"]:
        return 1

    if "?" in path and any(x in path for x in [
        "'", "%27", "--", "union", "select",
        " or ", "%20or%20", " and ", "%20and%20"
    ]):
        return 9  # SQLi

    if "=" in path and any(x in path for x in [
        "sleep", "%28", "%29", "ls", "cat", "echo", "/bin/"
    ]):
        return 8  # Command Injection

    if "=" in path and any(x in path for x in [
        "<script", "%3cscript", "<>", "<></>"
    ]):
        return 5  # XSS

    if path in ["/", "/style.css", "/robots.txt", "/favicon.ico"]:
        return 0  # Normal

    return -1


def prepare(func=assign_label):

    # Always reload fresh parsed file
    df = pd.read_csv("Csv/parsed/parsed.csv")

    # Label assignment
    df["label"] = df.apply(func, axis=1)

    # Compute IP frequency ONCE
    ip_counts = df["source_ip"].value_counts()

    # Vectorized frequency scoring (NO row-wise calls)
    df["freq_label"] = df["source_ip"].map(
        lambda ip: (
            3 if ip_counts.get(ip, 0) >= 100 else
            2 if ip_counts.get(ip, 0) >= 30 else
            1 if ip_counts.get(ip, 0) >= 10 else
            0
        )
    )

    # Save labeled data
    df.to_csv("Csv/labeled/labeled.csv", index=False)

    print("Label counts:")
    print(df["label"].value_counts())

    print("\nFrequency label counts:")
    print(df["freq_label"].value_counts())

    return True


if __name__ == "__main__":
    prepare()