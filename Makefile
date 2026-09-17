.PHONY: run install setup 

run:
	poetry run streamlit run streamlit/app.py

install:
	poetry install

setup:
	poetry install
	poetry run python -c "from configs.database import engine; print('db connected')"

