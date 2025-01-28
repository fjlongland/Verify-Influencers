from openai import OpenAI
from .config import Settings

def basic_call(question):

    settings = Settings()

    api_key = settings.api_key

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
            ),
        },
        {
            "role": "user",
            "content": (
                f"{question}"
            ),
        },
    ]

    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages
    )

    answer = response.choices[0].message.content

    print(answer)




def about_influencer_call(name):

    settings = Settings()

    api_key = settings.api_key

    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user."
            ),
        },
        {
            "role": "user",
            "content": (
                f"tell me what you know about {name} but put his notable information in a json format, focuses are: a breif one paragraph summary of the person, the feilds he has worked in, his yearly revenue, how many online followers he has, and how many products he has released. return only the json file"
            ),
        },
    ]

    client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

    response = client.chat.completions.create(
        model="sonar-pro",
        messages=messages
    )

    answer = response.choices[0].message.content

    return answer