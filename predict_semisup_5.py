import pandas as pd
import joblib

model = joblib.load("semisup_model.joblib")
df = pd.read_csv("Csv/features_semisup/features_semisup.csv")

df["predicted_label"] = model.transduction_

df.to_csv("Output/output_semisup.csv", index=False)
print("[+] output_semisup.csv created")
