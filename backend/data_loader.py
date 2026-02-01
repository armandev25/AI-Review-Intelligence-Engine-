import pandas as pd
from config import MOBILE_FILE, PERSONAL_CARE_FILE, MAJOR_APPLIANCES_FILE


def load_dataset():
    frames = []

    for file in [MOBILE_FILE, PERSONAL_CARE_FILE, MAJOR_APPLIANCES_FILE]:
        df = pd.read_csv(file)
        frames.append(df)

    data = pd.concat(frames, ignore_index=True)
    return data


if __name__ == "__main__":
    df = load_dataset()
    print("Total reviews loaded:", len(df))
    print(df.head())
