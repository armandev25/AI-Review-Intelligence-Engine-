import pandas as pd
import os

INPUT_FILES = {
    "mobile_electronics": r"C:\Users\arman\Downloads\ds\amazon_reviews_us_Mobile_Electronics_v1_00.tsv",
    "personal_care": r"C:\Users\arman\Downloads\ds\amazon_reviews_us_Personal_Care_Appliances_v1_00.tsv",
    "major_appliances": r"C:\Users\arman\Downloads\ds\amazon_reviews_us_Major_Appliances_v1_00.tsv"
}

OUTPUT_DIR = "../data/processed"
SAMPLE_SIZE = 5000


def process_file(name, path):
    print(f"\nProcessing {name}...")

    chunks = pd.read_csv(
        path,
        sep="\t",
        usecols=[
            "product_id",
            "product_title",
            "product_category",
            "review_body",
            "star_rating"
        ],
        chunksize=50000
    )

    collected = []

    for chunk in chunks:
        chunk = chunk.dropna()
        collected.append(chunk)

        if sum(len(c) for c in collected) >= SAMPLE_SIZE:
            break

    df = pd.concat(collected).head(SAMPLE_SIZE)

    df.columns = [
        "item_id",
        "item_name",
        "domain",
        "review_text",
        "rating"
    ]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"{name}.csv")
    df.to_csv(output_path, index=False)

    print(f"Saved -> {output_path}")


if __name__ == "__main__":
    for name, path in INPUT_FILES.items():
        process_file(name, path)
