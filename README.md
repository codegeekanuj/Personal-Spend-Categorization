# Personal Spend Categorization

**Author:** Anuj Tripathi  
**Project type:** Machine learning — text classification for personal finance

Automatically assign **spending categories** to bank transaction descriptions (merchant names, transfer memos, etc.). The pipeline turns raw transaction text into labels such as groceries, housing, or transport so you can summarize expenses without manual tagging.

## Models compared

| Model | Role |
|-------|------|
| Random Forest | Bag-of-words + stemmed tokens (strong baseline) |
| Logistic Regression | Linear text classifier |
| Naive Bayes | Fast probabilistic baseline |
| Neural network (TensorFlow) | Embedding + dense layers on text |

Reported test accuracy on the bundled sample dataset (replace with your own labels for production use):

| Model | Accuracy |
|-------|----------|
| Random Forest | ~0.94 |
| Neural Network | ~0.93 |
| Logistic Regression | ~0.92 |
| Naive Bayes | ~0.91 |

## Category labels

| Id | Category |
|----|----------|
| 0 | Automobile and transport |
| 1 | Housing and real estate |
| 2 | Groceries |
| 3 | Recreation and leisure |
| 4 | Health and well-being |
| 5 | Hobby and knowledge |
| 6 | Clothes and equipment |
| 7 | Cash and credit |
| 8 | Financial services |
| 9 | Other |

## Repository layout

| Path | Description |
|------|-------------|
| `notebooks/01_classical_text_classifiers.ipynb` | NLTK preprocessing, TF-IDF/count features, RF / LR / NB |
| `notebooks/02_neural_spend_classifier.ipynb` | Keras text vectorization + embedding model |
| `data/transactions_dataset.csv` | Labeled transactions (`Text`, `CategoryId`) |
| `src/paths.py` | Dataset path helper |
| `src/categories.py` | Id → category name mapping |

## Setup

```bash
cd spend-categorization
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m nltk.downloader stopwords
jupyter notebook
```

## Dataset

- Default file: **`data/transactions_dataset.csv`**
- Columns: **`Text`** (string), **`CategoryId`** (integer 0–9)
- A **starter sample** is included so notebooks run out of the box; swap in your own labeled exports for real budgeting workflows.

See [`data/README.md`](data/README.md) for format details.

## License

MIT — see [LICENSE](LICENSE).

## Acknowledgements

Problem inspired by open-source transaction categorization work; this repo is a reworked portfolio layout, paths, and documentation for local use.
