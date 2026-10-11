
import unittest
from pathlib import Path
import pandas as pd

from check_dataset import DATASET_PATH, check_dataset


class TestTelecomDataset(unittest.TestCase):

    def test_dataset_file_exists(self):
        self.assertTrue(
            DATASET_PATH.exists(),
            f"Dataset not found: {DATASET_PATH}"
        )

    def test_dataset_is_not_empty(self):
        df = pd.read_csv(DATASET_PATH)
        self.assertGreater(len(df), 0)

    def test_expected_columns_exist(self):
        df = pd.read_csv(DATASET_PATH)

        expected_columns = [
            "CustomerID",
            "MonthlyCharges",
            "TenureMonths",
            "SupportTickets",
            "DataUsageGB",
            "SatisfactionScore"
        ]

        for column in expected_columns:
            with self.subTest(column=column):
                self.assertIn(column, df.columns)

    def test_dataset_check_runs(self):
        check_dataset()


if __name__ == "__main__":
    unittest.main()