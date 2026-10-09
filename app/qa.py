import ollama

# Testing the Ollama Connection##
""" def ask_llm(question: str) ->str:
    response = ollama.chat(
        model="llama3.2:latest", 
        messages=[
            {
                "role":'user', 
                "content": question
            }
        ]
    )

    return response["message"]["content"]

if __name__ == "__main__":
    answer = ask_llm("Answer in one sentence: What is Python?")
    print(answer) """


def answer_question(question: str, context: str) ->str:
    prompt = f"""
Use only the context below to answer the question: 

Context: 
{context}

Question:
{question}

If the answer is not supported by the context, say: 
"I don't know based on the provided context."
"""

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return response["message"]["content"]

if __name__ == "__main__":
    context = """
Python Lists are mutable sequences. This means their contents can be changed after the list is created.
"""
    question = "Who created Python"
    answer = answer_question(question, context)
    print(answer)
