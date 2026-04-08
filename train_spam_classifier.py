import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def main() -> None:
    # 1. Load dataset using pandas
    df = pd.read_csv("spam.csv", encoding="latin-1")

    # 2. Keep only columns v1 and v2
    df = df[["v1", "v2"]]

    # 3. Rename columns to label and text
    df = df.rename(columns={"v1": "label", "v2": "text"})

    # 4. Convert labels: ham = 0, spam = 1
    df["label"] = df["label"].map({"ham": 0, "spam": 1})

    # 5. Drop null values and duplicates
    df = df.dropna().drop_duplicates()

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["label"],
        test_size=0.2,
        random_state=42,
        stratify=df["label"],
    )

    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Output: print accuracy score
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")


if __name__ == "__main__":
    main()
