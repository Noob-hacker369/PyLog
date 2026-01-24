import pandas as pd
import numpy as np
import joblib

def predict():
    # Load data
    df = pd.read_csv("Csv/features_semisup/features_semisup.csv")

    # Load model & scaler
    model = joblib.load("Model/semisup_model.joblib")
    scaler = joblib.load("Model/semisup_scaler.joblib")

    FEATURES = [
        "method_enc",
        "path_len",
        "path_depth",
        "has_query",
        "has_values",
        "is_php",
        "is_static",
        "freq_label"
    ]

    # Prepare feature matrix
    X_df = df[FEATURES].fillna(0)

    # Preserve feature names
    X_scaled = pd.DataFrame(
        scaler.transform(X_df),
        columns=scaler.feature_names_in_
    )

    # Sanitize numeric issues
    X_scaled = X_scaled.replace([np.inf, -np.inf], 0).fillna(0)

    # Batched prediction
    BATCH_SIZE = 10000
    predictions = []

    for i in range(0, len(X_scaled), BATCH_SIZE):
        batch = X_scaled.iloc[i:i + BATCH_SIZE].values
        preds = model.predict(batch)
        predictions.extend(preds)

    # Attach predictions
    df["predicted_label"] = predictions

    # Safety: replace NaN predictions
    df["predicted_label"] = df["predicted_label"].fillna(-1)

    # Save output
    df.to_csv("Output/semisup_output.csv", index=False)

    print("[+] Semi-supervised prediction complete")
    return True


if __name__ == "__main__":
    predict()
