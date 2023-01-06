import tkinter as tk
import openai
import tweepy

# Set up the Tkinter GUI
window = tk.Tk()
window.title("OpenAI Tweet Generator by Tyler Hodges")


# Function to run when the "Run" button is clicked
def run_script():
    # Get the API keys from the GUI
    ck = consumer_key_entry.get()
    cs = consumer_secret_entry.get()
    at = access_token_entry.get()
    ats = access_token_secret_entry.get()
    oik = openai_key_entry.get()
    prompt = prompt_entry.get()

    # Set up the Tweepy API client with the API keys
    client = tweepy.Client(consumer_key=ck,
                           consumer_secret=cs,
                           access_token=at,
                           access_token_secret=ats)

    # Configure the openai module by setting the secret key
    openai.api_key = oik

    # create a completion
    response = openai.Completion.create(
        model="text-davinci-003",
        max_tokens=150,
        prompt=prompt,
        temperature=0.9,
        top_p=1,
        stop="|<EndOfText>|")

    # Post response as tweet
    response = client.create_tweet(text=response.choices[0].text)

    # Update the GUI with the response from OpenAI
    response_label.config(text=response.data['text'])
    success_label.config(text="Tweet tweeted successfully!")


# Consumer Key label and entry
consumer_key_label = tk.Label(text="Consumer Key:")
consumer_key_label.grid(row=0, column=0)
consumer_key_entry = tk.Entry()
consumer_key_entry.grid(row=0, column=1)

# Consumer Secret label and entry
consumer_secret_label = tk.Label(text="Consumer Secret:")
consumer_secret_label.grid(row=1, column=0)
consumer_secret_entry = tk.Entry()
consumer_secret_entry.grid(row=1, column=1)

# Access Token label and entry
access_token_label = tk.Label(text="Access Token:")
access_token_label.grid(row=2, column=0)
access_token_entry = tk.Entry()
access_token_entry.grid(row=2, column=1)

# Access Token Secret label and entry
access_token_secret_label = tk.Label(text="Access Token Secret:")
access_token_secret_label.grid(row=3, column=0)
access_token_secret_entry = tk.Entry()
access_token_secret_entry.grid(row=3, column=1)

# OpenAI Key label and entry
openai_key_label = tk.Label(text="OpenAI Key:")
openai_key_label.grid(row=4, column=0)
openai_key_entry = tk.Entry()
openai_key_entry.grid(row=4, column=1)

# Prompt label and entry
prompt_label = tk.Label(text="Prompt:")
prompt_label.grid(row=5, column=0)
prompt_entry = tk.Entry()
prompt_entry.grid(row=5, column=1)

# "Run" button
run_button = tk.Button(text="Run", command=run_script)
run_button.grid(row=6, column=0)

# Success label
success_label = tk.Label(text="")
success_label.grid(row=7, column=0)

# Response label
response_label = tk.Label(text="")
response_label.grid(row=8, column=0)

# Adjust size
window.geometry("500x400")


# Run the Tkinter event loop
window.mainloop()
