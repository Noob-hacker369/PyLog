import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Csv/labeled/labeled.csv")

# Encode HTTP method
method_enc = LabelEncoder()
df["method_enc"] = method_enc.fit_transform(
    df["http_method"].fillna("NONE")
)

# Path length
df["path_len"] = df["path"].fillna("").apply(len)

# Query / payload indicator
df["has_query"] = (
    df["path"]
    .fillna("")
    .str.contains(r"\?|%27|--", regex=True)
    .astype(int)
)

# File-type indicators (FIXED)
df["is_php"] = (
    df["path"]
    .fillna("")
    .str.contains(".php", regex=False)
    .astype(int)
)

df["is_static"] = (
    df["path"]
    .fillna("")
    .str.contains(r"\.css|\.js|\.png|\.jpg", regex=True)
    .astype(int)
)
df["path_depth"] = df["path"].fillna("").str.count("/")

# Final feature set
X = df[["method_enc", "path_len","path_depth" ,"has_query", "is_php", "is_static"]]
y = df["label"]

features = X.copy()
features["label"] = y

features.to_csv("Csv/features_semisup/features_semisup.csv", index=False)
print("[+] features_semisup.csv created successfully")
