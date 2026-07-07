# PyLog

A Python-based log analysis tool with a desktop GUI, built on **pandas** for data processing and **scikit-learn** for machine-learning-driven log classification/analysis.

## Overview

PyLog lets you load raw log files, run them through an analysis pipeline, and view the results — all from a lightweight desktop interface built with `customtkinter`. It's designed for quick, local log triage without needing a full log-management stack.

## Features

- 🖥️ Desktop GUI (built with CustomTkinter)
- 📊 Log parsing and analysis powered by pandas
- 🤖 ML-based analysis/classification via scikit-learn, with trained models persisted using joblib
- 📁 Organized input/output pipeline (`Input/`, `Output/`, `data/`, `Csv/`)

## Project Structure

```
PyLog/
├── Csv/            # CSV data files
├── Input/          # Input log files for analysis
├── Model/          # Trained ML models
├── Output/         # Analysis results/output
├── assets/         # UI assets (icons, images, etc.)
├── data/           # Working data (input/output subfolders created at runtime)
├── function/       # Helper/utility functions
├── src/            # Application source code
│   ├── interface/  # GUI (app_ui.py — SkillApp)
│   └── backend/    # Processing logic (model_i.py, model_ii.py)
├── main.py         # Application entry point
├── maping.txt      # Mapping/reference data
└── requirement.txt # Python dependencies
```

## Requirements

- Python 3.x
- Dependencies (see `requirement.txt`):
  - `pandas`
  - `scikit-learn`
  - `joblib`
  - `customtkinter`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anushit-cybersec/PyLog.git
   cd PyLog
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

## Usage

Run the application:

```bash
python main.py
```

This launches the PyLog GUI. On startup, it automatically creates the required working folders (`data/input`, `data/output`, `assets`) if they don't already exist. From the interface, you can:

1. Load a log file for analysis
2. Run the analysis pipeline
3. View the generated results

## How It Works

- `main.py` initializes the required folders and starts the `SkillApp` GUI, wiring up two callbacks:
  - `process_log_file` — parses and processes the uploaded log file
  - `generate_results` — analyzes the processed data and displays/exports results
- Processed logs and outputs are organized under `Input/`, `Output/`, `Csv/`, and `data/`.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

No license has been specified for this repository yet. Check with the repository owner before reuse.
