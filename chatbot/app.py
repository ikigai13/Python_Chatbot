from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch
import os

# Keep track of chat history
chat_history = []

# Merged model folder
MERGED_MODEL_PATH = r"C:\Users\nixon\test\Ikigai_Merge_Model"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MERGED_MODEL_PATH)

# Load merged model
model = AutoModelForCausalLM.from_pretrained(
    MERGED_MODEL_PATH,
    torch_dtype=torch.float16
).to("cuda")  # move model to GPU
# Ensure model is in evaluation mode
model.eval()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Check for quit
    if user_message.strip().lower() in ["quit", "exit", "stop"]:
        return jsonify({"reply": "Goodbye! Chat ended."})

    # Build prompt: just instruction + user message
    system_instruction = ("""
                          
    You are a friendly Python tutor for complete beginners.

    - Always greet the user warmly and introduce yourself as a Python tutor when they say hi or first start the conversation.
    - Always explain concepts in very simple, beginner-friendly language first.
    - After every explanation show the Python code, provide a short code example on a new line.
    - Always format code examples inside triple backticks with "python".
    - STRICLY Do not mix explanation and code in the same block of text. Always put the code after the explanation, clearly labeled as an example.
    - Keep examples short and easy to run.
    
    - The format should look like this:
    
    Question: <question text here>
    Answer: <answer text here>
    Python code example:
    
    ```python
    # code goes here
    ```
    
    """)
    
    prompt = f"{system_instruction}\nUser: {user_message}\nAssistant:"

    # Encode input and move to GPU
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    # Generate output
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=500,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            # num_beams = 2,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )

    # Decode output
    bot_reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    bot_reply_clean = bot_reply.split("Assistant:")[-1].strip()

    return jsonify({"reply": bot_reply_clean})

if __name__ == "__main__":
    app.run(debug=True)