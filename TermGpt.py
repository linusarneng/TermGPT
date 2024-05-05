import openai

# Lägg till din OpenAI API-nyckel här
openai.api_key = 'ur api key'

def chat_with_gpt(prompt, max_tokens=150, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Använd davinci-modellen
        messages=[{"role": "system", "content": "You are a helpful assistant"}, #content": "You are a helpful assistant
                  {"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].message['content']

def main():
    print("""\033[94m _____                    ____ ____ _____ 
|_   _|__ _ __ _ __ ___  / ___|  _ \_   _|
  | |/ _ \ '__| '_ ` _ \| |  _| |_) || |  
  | |  __/ |  | | | | | | |_| |  __/ | |  
  |_|\___|_|  |_| |_| |_|\____|_|    |_|   Version 1.0\033[0m""")

    print("")
    print("Welcome to TermGPT! Write 'exit' to quit.")

    while True:
        print("")
        user_input = input("\033[94mYou:\033[0m ")
        if user_input.lower() == 'exit':
            print("Good bye!")
            break
        response = chat_with_gpt(user_input)
        print("")
        print("\033[32mChatGPT:\033[0m", response)

if __name__ == "__main__":
    main()
