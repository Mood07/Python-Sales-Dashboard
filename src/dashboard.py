import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename="supermarket_sales.csv"):
    """
    Load CSV using a robust path system that works anywhere.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # src/
    data_path = os.path.join(base_dir, "..", "data", filename)
    data_path = os.path.abspath(data_path)

    print("Trying to load CSV from:")
    print(" →", data_path)

    try:
        df = pd.read_csv(data_path)
        print("\n✔ Dataset loaded successfully.\n")
        return df
    except FileNotFoundError:
        print("\n❌ Error: CSV file not found at:")
        print(" →", data_path)
        return None


def ensure_output_dir():
    """
    Create assets/visuals directory if it does not exist.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    visuals_dir = os.path.join(base_dir, "..", "assets", "visuals")
    visuals_dir = os.path.abspath(visuals_dir)

    os.makedirs(visuals_dir, exist_ok=True)
    return visuals_dir


def basic_overview(df):
    print("=== DATASET SHAPE ===")
    print(df.shape, "\n")

    print("=== COLUMNS ===")
    print(df.columns, "\n")

    print("=== DESCRIPTIVE STATISTICS (Numeric) ===")
    print(df.describe(), "\n")


def total_sales_by_branch(df, visuals_dir):
    if "Branch" not in df.columns or "Total" not in df.columns:
        print("Missing columns for branch sales analysis.\n")
        return

    sales_by_branch = df.groupby("Branch")["Total"].sum().sort_values(ascending=False)

    print("=== TOTAL SALES BY BRANCH ===")
    print(sales_by_branch, "\n")

    plt.figure()
    sales_by_branch.plot(kind="bar")
    plt.title("Total Sales by Branch")
    plt.xlabel("Branch")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    output_path = os.path.join(visuals_dir, "total_sales_by_branch.png")
    plt.savefig(output_path)
    print(f"✔ Saved: {output_path}\n")
    plt.show()


def avg_rating_by_product_line(df, visuals_dir):
    if "Product line" not in df.columns or "Rating" not in df.columns:
        print("Missing columns for rating analysis.\n")
        return

    avg_rating = df.groupby("Product line")["Rating"].mean().sort_values(ascending=False)

    print("=== AVERAGE RATING BY PRODUCT LINE ===")
    print(avg_rating, "\n")

    plt.figure()
    avg_rating.plot(kind="bar")
    plt.title("Average Rating by Product Line")
    plt.xlabel("Product Line")
    plt.ylabel("Average Rating")
    plt.tight_layout()

    output_path = os.path.join(visuals_dir, "avg_rating_by_product_line.png")
    plt.savefig(output_path)
    print(f"✔ Saved: {output_path}\n")
    plt.show()


def main():
    df = load_data("supermarket_sales.csv")
    if df is None:
        return

    visuals_dir = ensure_output_dir()

    basic_overview(df)
    total_sales_by_branch(df, visuals_dir)
    avg_rating_by_product_line(df, visuals_dir)


if __name__ == "__main__":
    main()
