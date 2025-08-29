# Python Chatbot

This is my first project on building an NLP/LLM-based chatbot model.  
The process starts with creating a synthetic dataset, then training the model using LoRA.  

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
    git clone https://github.com/ikigai13/Python_Chatbot.git
    cd Python_Chatbot

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt

2. Start the Flask app:
    cd chatbot
    python app.py
