import openai
# API key
openai.api_key = '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'
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # use other engines like "text-davinci-003"
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    print("Welcome to the ChatGPT Interaction Program!")
    print("Type 'exit' to end the conversation.")

    user_input = ""
    while user_input.lower() != "exit":
        user_input = input("You: ")
        if user_input.lower() != "exit":
            prompt = f"You: {user_input}\nChatGPT:"
            response = chat_with_gpt(prompt)
            print(response)
