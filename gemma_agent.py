import ollama

# Define the model name (Gemma, already pulled in Ollama)
model_name = "gemma:2B"

def ask_gemma(prompt):
    """
    Send a prompt to the Gemma model via Ollama and return the response.
    """
    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

# Example for testing (you can remove this block when integrating with agents)
if _name_ == "_main_":
    question = "Give a daily health tip for elderly care."
    print("Gemma says:", ask_gemma(question))

    