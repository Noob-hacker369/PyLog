import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib



def iforest():
    df = pd.read_csv("Output/semisup_output.csv")

    behavior_features = df[
        [
            "path_len",
            "path_depth",
            "has_query",
            "has_values",
            "freq_label"
        ]
    ]

    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42
    )

    df["behavior_anomaly"] = model.fit_predict(behavior_features)

    joblib.dump(model, "Model/iforest_model.joblib")

    df.to_csv("Output/final_output.csv", index=False)
    print("[+] Final output generated")
