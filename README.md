# noCartInsights

ecommerce performance analysis using brazilian olist dataset.

## Overview

this project analyzes ~100k orders from brazil's largest online marketplace to uncover insights about sales, customers, sellers, and delivery performance.

## Tech stack

- **python 3.12** - data processing
- **pandas / numpy** - data manipulation
- **sqlalchemy + postgresql** - database & SQL analysis
- **scipy** - statistical testing (t-test, ANOVA, chi-square)
- **streamlit** - interactive dashboard
- **poetry** - dependency management

## Project structure

```
noCartInsights/
├── analysis/           # statistical tests
│   ├── t-test.ipynb
│   ├── anova.ipynb
│   └── chi-square.ipynb
├── configs/            # database & settings
├── data/               # raw, cleaned, feature engineered csvs
├── sql/                # SQL analysis queries
├── streamlit/          # dashboard app
└── pyproject.toml      # dependencies
```



## running

```bash
# run streamlit dashboard
make run

# or directly
poetry run streamlit run streamlit/app.py
```




