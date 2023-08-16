import openai
import time


openai.api_key = 'sk-************************************************'

messages = []


def print_with_delay(text, delay):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)

while True:
    prompt = input('\nUser> ')
    if prompt == 'quit':
        break
    messages.append({
        'role': 'user',
        'content': prompt,
    })
    print('Generating answers . . .')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1024,
        temperature=0.8,
    )

    response = completion['choices'][0]['message']['content']


    text = f'AI> {response}'
    delay = 0.02  # Delay in seconds

    print_with_delay(text, delay)


    messages.append({
        'role': 'assistant',
        'content': response
    })


