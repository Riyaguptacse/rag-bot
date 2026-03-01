import sys
import os

# Add the app folder to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


from logger import log_message

from retrieve import retrieve
# Memory dictionary to store past Q&A
chat_memory = []

def rag_answer(query, k=2):
    top_docs = retrieve(query, k=k)
    context = "\n".join(top_docs)

    if any("Tesla" in doc for doc in top_docs) and "Tesla" in query:
        answer = "Elon Musk and Martin Eberhard founded Tesla in 2003."
    elif any("OpenAI" in doc for doc in top_docs) and "OpenAI" in query:
        answer = "OpenAI develops AI models like GPT."
    else:
        answer = "I don't know based on the documents."

    # Save in memory
    chat_memory.append({"question": query, "answer": answer})

    # Save in log
    log_message(query, answer)

    return answer

# 4️⃣ Function to show conversation so far
def show_memory():
    for entry in chat_memory:
        print("Q:", entry["question"])
        print("A:", entry["answer"])
        print("-"*30)

# 5️⃣ Test loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending chat. Conversation so far:")
            show_memory()
            break
        response = rag_answer(user_input)
        print("Bot:", response)