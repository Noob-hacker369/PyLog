import pandas as pd
from sklearn.semi_supervised import LabelSpreading
import joblib

df = pd.read_csv("Csv/features_semisup/features_semisup.csv")

X = df[["method_enc", "path_len","path_depth" ,"has_query", "is_php", "is_static"]]
y = df["label"]

model = LabelSpreading(
    kernel="rbf",
    gamma=20,
    max_iter=100
)

model.fit(X, y)   # ← semi-supervised training

joblib.dump(model, "Model/semisup_model.joblib")
print("[+] Semi-supervised model trained")