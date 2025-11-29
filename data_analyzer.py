# Step 1: Imports
import pandas as pd  # For data manipulation
import ollama  # For local LLM interaction
from io import StringIO  # To capture text output from Pandas

# Step 2: Data/Input Preparation
df = pd.read_csv("analysis_data.csv")  # Load the dataset
print(
    f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns."
)  # Confirm load


# Step 3: Function Definition
def analyze_data_schema(df):
    """Extracts metadata from the DataFrame and queries Llama 3 for analysis."""
    # We will add the logic inside this function in the next steps
    # Step 4 (Part 1): Prepare Data Context
    buffer = StringIO()
    df.info(buf=buffer)  # Write schema info to the buffer
    data_info = buffer.getvalue()  # Get string from buffer
    data_head = df.head(3).to_markdown(index=False)  # Get sample rows
    # Step 4 (Part 2): Construct Prompts
    system_msg = (
        "You are a Senior Data Scientist. "
        "Analyze the provided Pandas DataFrame schema and sample data. "
        "Output a professional report in Markdown with these strict sections:\n"
        "1. **Dataset Domain**: Infer the industry or topic.\n"
        "2. **Feature Analysis**: Distinguish between numerical and categorical features.\n"
        "3. **Target Hypothesis**: Guess which column is the likely target for prediction.\n"
        "4. **Recommended Actions**: Suggest 3 specific technical tasks (e.g., 'One-hot encode X', 'Check correlation between Y and Z')."
    )
    user_msg = f"Schema:\n{data_info}\n\nSample:\n{data_head}"

    # Step 4 (Part 3): Call Local LLM
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )
    return response["message"]["content"]


# Step 5: Main Execution Block
if __name__ == "__main__":
    print("Analyzing data with Llama 3...")
    result = analyze_data_schema(df)  # Run the analysis
    print("\n--- AI Analysis ---\n" + result)  # Display the report
