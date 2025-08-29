# Python Chatbot

## Introduction

This project is my first step into building an NLP/LLM-based chatbot. It demonstrates the end-to-end process of generating synthetic data, fine-tuning a language model using LoRA, and testing it via a simple web application. The goal is to showcase practical experience in NLP workflows as part of my learning and portfolio development.

## Project Workflow

### 1. Synthetic Data Generation
- Used **Jupyter Notebook** and **Ollama/Qwen2.5:3B** to generate synthetic data
- Input data was extracted from PDFs and converted into Q&A format
- Data was preprocessed and filtered to ensure high quality

### 2. Model Training
- Training was done on **Google Colab** using **Hugging Face Transformers**
- Base model: `meta-llama/Llama-3.2-1B-Instruct`
- Preprocessed synthetic data was fine-tuned using **LoRA**

### 3. Web Application (Testing)
- Created a simple **Flask app** with **HTML, CSS, and Bootstrap**
- Allows basic testing and interaction with the trained model

## Project Structure
```
notebooks/                    # Jupyter notebooks
  ├─ GenerateSyntheticData.ipynb   # creates a synthetic dataset for training
  └─ Model_Training.ipynb          # fine-tunes the model using LoRA  

data/                       # datasets
  ├─ instruction.json             # main dataset after generation
  ├─ instructionquality.json      # dataset filtered with an LLM for quality
  └─ qualityresults.json          # dataset + explanations  

requirements.txt            # list of dependencies  
README.md                   # project documentation  
```

## How to Run
1. Clone this repository  
    ```
    git clone https://github.com/ikigai13/Python_Chatbot.git
    cd Python_Chatbot
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the notebooks
  - Open notebooks/GenerateSyntheticData.ipynb to generate the dataset.
  - Open notebooks/Model_Training.ipynb to fine-tune the model.

4. (Optional) Run the Flask app for testing
    ```
    cd chatbot
    python app.py
    ```
