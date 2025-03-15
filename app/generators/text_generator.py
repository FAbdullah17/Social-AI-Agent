import ollama
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def generate_text(prompt: str) -> str:
    """
    Generates text using DeepSeek 7B via Ollama.
    
    Args:
        prompt (str): The input prompt.
    
    Returns:
        str: The generated text.
    """
    try:
        response = ollama.chat(
            model="deepseek-r1:7b", 
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]
    except Exception as e:
        logger.error("Error generating text with Ollama: %s", e)
        raise

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    generated_text = generate_text(prompt)
    print("Generated Text:\n", generated_text)