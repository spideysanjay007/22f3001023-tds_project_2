# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "pandas",
#   "seaborn",
#   "matplotlib",
#   "numpy",
#   "requests",
#   "python-dotenv",
# ]
# ///

import os
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# OpenAI API configurations
API_BASE = "https://aiproxy.sanand.workers.dev/openai/v1"
API_KEY = os.getenv("AIPROXY_TOKEN")
MODEL = "gpt-4o-mini"

if not API_KEY:
    print("Error: Missing AIPROXY_TOKEN. Please set it in your environment variables.")
    sys.exit(1)

# Function to fetch responses from the LLM
def fetch_llm_response(prompt):
    try:
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are an AI analyst."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 800,
            "temperature": 0.7
        }
        response = requests.post(f"{API_BASE}/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"].strip()
        else:
            return "No analysis provided."
    except Exception as e:
        return f"Error: {e}"

# Function to analyze the dataset
def analyze_dataset(data):
    summary_stats = data.describe(include="all").transpose()
    missing_values = data.isnull().sum()
    correlation_matrix = data.corr(numeric_only=True)
    return summary_stats, missing_values, correlation_matrix

# Function to visualize the dataset
def generate_visualizations(data, correlation_matrix, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Correlation Matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
    plt.title("Correlation Matrix")
    plt.savefig(os.path.join(output_dir, "correlation_matrix.png"))
    plt.close()

    # Distribution Plots
    for column in data.select_dtypes(include=[np.number]).columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column].dropna(), kde=True, bins=30, color="blue")
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(output_dir, f"{column}_distribution.png"))
        plt.close()

# Function to create README with analysis and visualizations
def create_readme(data, summary_stats, missing_values, llm_analysis, output_dir):
    markdown_content = f"""
# Automated Data Analysis Report

## Introduction
This is an automated analysis of the dataset, providing summary statistics, visualizations, and insights from the data.

## Dataset Overview
- **Rows**: {data.shape[0]}
- **Columns**: {data.shape[1]}
- **Missing Values**:
{missing_values.to_string()}

## Summary Statistics
{summary_stats.to_markdown()}

## Key Insights
{llm_analysis}

## Visualizations
### Correlation Matrix
![Correlation Matrix](correlation_matrix.png)

### Distributions
"""
    for column in data.select_dtypes(include=[np.number]).columns:
        markdown_content += f"![{column} Distribution]({column}_distribution.png)\n"

    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(markdown_content)
    return readme_path

# Main function
def main(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    data = pd.read_csv(file_path, encoding="ISO-8859-1")
    summary_stats, missing_values, correlation_matrix = analyze_dataset(data)

    dataset_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(dataset_name)

    generate_visualizations(data, correlation_matrix, output_dir)

    llm_prompt = f"""
You are an AI analyst. Here is the dataset summary:
- Columns: {list(data.columns)}
- Data types: {data.dtypes.to_dict()}
- Missing values: {missing_values.to_dict()}
- Sample data: {data.head(5).to_dict(orient='records')}

Analyze the data and provide insights. Highlight any interesting trends, outliers, or relationships.
"""
    llm_analysis = fetch_llm_response(llm_prompt)
    readme_path = create_readme(data, summary_stats, missing_values, llm_analysis, output_dir)

    print(f"Analysis completed. Results saved to: {output_dir}")
    print(f"README file: {readme_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)
    main(sys.argv[1])
