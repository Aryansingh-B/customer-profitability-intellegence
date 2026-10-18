
"""Basic data-quality checks for the Sample Superstore CSV.
Run from the project root: python data_quality_check.py
Or pass a path: python data_quality_check.py "data/raw/your_file.csv"
"""

from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parent
DEFAULT_CSV = ROOT / "data" / "raw" / "Sample - Superstore.csv"


def load_csv(path):
    for encoding in ("utf-8-sig", "cp1252", "latin1"):
        try:
            return pd.read_csv(path, encoding=encoding)
        except UnicodeDecodeError:
            pass
    raise ValueError("Could not decode CSV using utf-8-sig, cp1252, or latin1.")


def find_column(df, expected):
    lookup = {str(c).strip().casefold(): c for c in df.columns}
    return lookup.get(expected.casefold())


def main():
    path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_CSV

    if not path.is_absolute():
        path = ROOT / path

    path = path.resolve()

    if not path.is_file():
        print(f"Error: CSV file not found: {path}")
        return 1

    df = load_csv(path)

    print("\n=== DATA QUALITY CHECK ===")
    print(f"File: {path}")
    print(f"Rows: {len(df):,} | Columns: {len(df.columns):,}")
    print("\nColumns:", ", ".join(map(str, df.columns)))

    missing = df.isna().sum().sort_values(ascending=False)
    print("\nMissing values by column:")
    print(
        missing[missing > 0].to_string()
        if (missing > 0).any()
        else "No missing values found."
    )

    print(f"\nExact duplicate rows: {df.duplicated().sum():,}")

    for name in ("Order Date", "Ship Date"):
        col = find_column(df, name)
        if col is not None:
            dates = pd.to_datetime(df[col], errors="coerce")
            print(f"{name} parse failures: {dates.isna().sum():,}")
            if dates.notna().any():
                print(f"{name} range: {dates.min().date()} to {dates.max().date()}")

    for name in ("Sales", "Profit", "Quantity", "Discount"):
        col = find_column(df, name)
        if col is None:
            continue

        values = pd.to_numeric(df[col], errors="coerce")
        print(
            f"\n{name}: non-numeric/missing={values.isna().sum():,}, "
            f"min={values.min()}, max={values.max()}"
        )

        if name == "Sales":
            print(f"Negative sales rows: {(values < 0).sum():,}")
        elif name == "Profit":
            print(f"Loss-making rows (Profit < 0): {(values < 0).sum():,}")
        elif name == "Quantity":
            print(f"Non-positive quantity rows: {(values <= 0).sum():,}")
        elif name == "Discount":
            print(
                f"Discount outside 0-1 rows: "
                f"{((values < 0) | (values > 1)).sum():,}"
            )

    order_col = find_column(df, "Order ID")
    if order_col is not None:
        ids = df[order_col].astype("string").str.strip()
        print(f"\nBlank Order ID rows: {(ids.isna() | ids.eq('')).sum():,}")
        print(
            "Distinct Order IDs after trimming: "
            f"{ids[ids.notna() & ids.ne('')].nunique():,}"
        )

    print("\nNote: investigate unusual values and duplicates before removing anything.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
