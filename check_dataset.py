
from pathlib import Path
import pandas as pd

# Locate the telecom dataset in the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_DIR / "Telecom_Customer_Usage_Data (1).csv"


def check_dataset():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    df = pd.read_csv(DATASET_PATH)

    if df.empty:
        raise ValueError("Dataset is empty.")

    if len(df.columns) == 0:
        raise ValueError("Dataset has no columns.")

    print("Dataset check passed!")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("Column names:")
    print(df.columns.tolist())


if __name__ == "__main__":
    check_dataset()