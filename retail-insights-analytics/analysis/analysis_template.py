"""Starter analysis template.

Expected input: an approved CSV export with columns such as
Sales, Gross_Profit, Quantity, Category, Sub-Category, State, Order Date.

This script intentionally does not contain invented results. Update the file
path and column names after validating the exported dataset.
"""

from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/sales_export.csv")


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}. Add an approved CSV export first."
        )

    df = pd.read_csv(DATA_PATH)

    required = {"Sales", "Gross_Profit", "Quantity", "Category", "State", "Order Date"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {sorted(missing)}")

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

    print("Dataset shape:", df.shape)
    print("\nMissing values:")
    print(df.isna().sum().sort_values(ascending=False))

    print("\nOverall metrics:")
    print(df[["Sales", "Gross_Profit", "Quantity"]].sum(numeric_only=True))

    print("\nPerformance by category:")
    print(
        df.groupby("Category", dropna=False)[["Sales", "Gross_Profit", "Quantity"]]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    print("\nPerformance by state:")
    print(
        df.groupby("State", dropna=False)[["Sales", "Gross_Profit", "Quantity"]]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    monthly = (
        df.dropna(subset=["Order Date"])
        .assign(Month=lambda x: x["Order Date"].dt.to_period("M").astype(str))
        .groupby("Month")[["Sales", "Gross_Profit", "Quantity"]]
        .sum()
    )
    print("\nMonthly trend:")
    print(monthly)


if __name__ == "__main__":
    main()
