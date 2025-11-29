# 📊 P037_LLM_Data_Schema_Analyzer

## 📝 Description
A local AI-powered data analysis agent. This tool loads a dataset using Pandas, extracts the schema and sample data, and uses a local LLM (Llama 3 via Ollama) to perform an initial automated analysis of the dataset's characteristics and suggest potential data science tasks.

## ✨ Key Features
* **Pandas Integration**: Automatically extracts schema and types.
* **Local AI Privacy**: Uses Ollama (Llama 3) on local hardware (RTX 3090).
* **Automated Insights**: Generates high-level summaries without manual inspection.

## 🛠 Technology Stack
* **Python 3.10+**
* **Pandas**: Data manipulation.
* **Ollama**: Local LLM inference.
* **Tabulate**: Markdown formatting for dataframes.

## 🚀 Setup Instructions
1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Ensure Ollama is running locally with Llama 3 (`ollama pull llama3`).
4.  Add your CSV file as `analysis_data.csv`.
5.  Run the analyzer: `python data_analyzer.py`

## 👨‍💻 Author
**mmainomad-ship-it**
[GitHub Profile](https://github.com/mmainomad-ship-it)