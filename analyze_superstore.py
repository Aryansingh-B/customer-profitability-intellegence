"""Generate sales/profit summaries from the Sample Superstore CSV.
Run from project root: python python/analyze_superstore.py
Or pass a CSV path as the first argument.
"""
from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parent
DEFAULT_CSV = ROOT / "data" / "raw" / "Sample - Superstore.csv"
OUT = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"


def load_csv(path):
    for encoding in ("utf-8-sig", "cp1252", "latin1"):
        try:
            return pd.read_csv(path, encoding=encoding)
        except UnicodeDecodeError:
            pass
    raise ValueError("Could not decode CSV using utf-8-sig, cp1252, or latin1.")


def col(df, name, required=False):
    lookup = {str(c).strip().casefold(): c for c in df.columns}
    result = lookup.get(name.casefold())
    if result is None and required:
        raise KeyError(f"Required column '{name}' not found. Available columns: {list(df.columns)}")
    return result


def main():
    path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_CSV
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"CSV not found: {path}\nPut it in data/raw/ or pass the correct path.")

    OUT.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    df = load_csv(path)
    df.columns = [str(c).strip() for c in df.columns]

    sales, profit = col(df, "Sales", True), col(df, "Profit", True)
    order = col(df, "Order ID")
    date = col(df, "Order Date")
    dimensions = [
        ("Category", "profitability_by_category.csv"),
        ("Sub-Category", "profitability_by_subcategory.csv"),
        ("Region", "profitability_by_region.csv"),
        ("Customer Name", "profitability_by_customer.csv"),
        ("Product Name", "profitability_by_product.csv"),
    ]
    df[sales] = pd.to_numeric(df[sales], errors="coerce")
    df[profit] = pd.to_numeric(df[profit], errors="coerce")
    total_sales, total_profit = df[sales].sum(), df[profit].sum()
    margin = total_profit / total_sales * 100 if total_sales else 0
    order_count = df[order].nunique() if order else None

    for dimension, filename in dimensions:
        group_col = col(df, dimension)
        if group_col:
            result = df.groupby(group_col, dropna=False)[[sales, profit]].sum().reset_index()
            result["Profit Margin %"] = result[profit].div(result[sales].replace(0, float("nan"))) * 100
            result.sort_values(profit, ascending=False).to_csv(OUT / filename, index=False)

    discount = col(df, "Discount")
    if discount:
        df[discount] = pd.to_numeric(df[discount], errors="coerce")
        df["Discount Band"] = df[discount].map(lambda x: f"{x:.0%}" if pd.notna(x) else "Unknown")
        result = df.groupby("Discount Band", dropna=False)[[sales, profit]].sum().reset_index()
        result["Profit Margin %"] = result[profit].div(result[sales].replace(0, float("nan"))) * 100
        result.to_csv(OUT / "profitability_by_discount_band.csv", index=False)

    if date:
        df[date] = pd.to_datetime(df[date], errors="coerce")
        monthly = df.loc[df[date].notna()].copy()
        monthly["Order Month"] = monthly[date].dt.to_period("M").dt.to_timestamp()
        monthly.groupby("Order Month")[[sales, profit]].sum().reset_index().to_csv(
            OUT / "monthly_sales_profit.csv", index=False
        )

    lines = [
        "# Automated Superstore Analysis Summary", "",
        f"- Input file: `{path.name}`", f"- Rows analyzed: {len(df):,}",
        f"- Total Sales: ${total_sales:,.2f}", f"- Total Profit: ${total_profit:,.2f}",
        f"- Profit Margin: {margin:.2f}%",
        f"- Distinct Orders: {order_count:,}" if order_count is not None else "- Distinct Orders: Order ID column not found",
        "", "## Lowest-profit sub-categories"
    ]
    subcat = col(df, "Sub-Category")
    if subcat:
        grouped = df.groupby(subcat, dropna=False)[profit].sum().sort_values()
        lines.extend(f"- {name}: ${value:,.2f}" for name, value in grouped.head(5).items())
    lines += ["", "## Lowest-profit regions"]
    region = col(df, "Region")
    if region:
        grouped = df.groupby(region, dropna=False)[profit].sum().sort_values()
        lines.extend(f"- {name}: ${value:,.2f}" for name, value in grouped.items())
    lines += ["", "## Notes", "- Figures reflect this exact input file.",
              "- Reconcile with SQL and Power BI using the same rows and filters.",
              "- Negative profit identifies a loss but does not explain its cause."]
    report_path = REPORTS / "automated_analysis_summary.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\nAnalysis complete")
    print(f"Rows: {len(df):,}\nTotal Sales: ${total_sales:,.2f}\nTotal Profit: ${total_profit:,.2f}\nProfit Margin: {margin:.2f}%")
    if order_count is not None:
        print(f"Distinct Orders: {order_count:,}")
    print(f"CSV summaries saved in: {OUT}")
    print(f"Summary report saved to: {report_path}")


if __name__ == "__main__":
    main()
