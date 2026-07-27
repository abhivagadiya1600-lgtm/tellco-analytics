tellco-analytics/
├── .github/
│   └── workflows/
│       └── unittests.yml      # CI/CD workflow definition
├── src/                       # Main source code directory
│   ├── __init__.py
│   ├── data_prep.py          # Data cleaning & imputation logic
│   ├── eda.py                # Exploratory Data Analysis helpers
│   ├── feature_store.py      # Feature engineering & storage
│   └── models.py             # K-Means & Regression algorithms
├── tests/                     # Unit tests directory
│   ├── __init__.py
│   ├── test_data_prep.py
│   └── test_models.py
├── app/                       # Dashboard directory
│   └── main.py               # Streamlit or Flask application
├── data/                      # Local data storage (added to .gitignore)
│   └── xDR_data.csv
├── .gitignore
├── Dockerfile                 # Container setup
├── requirements.txt           # Python dependencies
├── setup.py                   # Packaging configuration
└── README.md                  # Project overview & documentation
