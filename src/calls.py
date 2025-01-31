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
                "You are a detailed artificial intelegence and you will try harder to fill in all the information requested"
            ),
        },
        {
            "role": "user",
            "content": (
                f"Please provide information about {name} in a JSON format. Use the following structure and titles exactly: "
                "{"
                '"summary": "A brief one-paragraph summary of the person",'
                '"fields": ["List of fields he has worked in"],'
                '"yearly_revenue": "Estimated yearly revenue if available, or \'Not available\' if unknown",'
                '"online_followers": {'
                '    "total": "Total number of followers across all platforms",'
                '    "platform_breakdown": {'
                '        "Instagram": "Number of Instagram followers",'
                '        "Twitter": "Number of Twitter followers",'
                '        "YouTube": "Number of YouTube subscribers"'
                '    }'
                '},'
                '"products_released": {'
                '    "books": "Number of books published",'
                '    "courses": "Number of online courses released",'
                '    "podcasts": "Number of podcast series hosted"'
                '    "total": "total number of products released"'
                '},'
                '"reliability_score": "A percentage based on his claims cross-referenced against trusted scientific journals"'
                "} "
                f"Return only the JSON file, populated with the relavant information about {name}. "
                "If any information is not available, use an estimate as the value only for yearly revenue, in other cases you can user (not available)."
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






def influencer_leaderboard():

    settings = Settings()

    api_key = settings.api_key

    messages = [
        {
            "role": "system",
            "content": (
                "You are a detailed artificial intelegence and you will try harder to fill in all the information requested"
            ),
        },
        {
            "role": "user",
            "content": (
            """Generate a JSON file containing information on the top 5 health and fitness influencers currently. For each influencer, include:
            1. Their name
            2. Their current total online following across all platforms
            3. A trust score percentage based on a comparison between their most recent health and fitness claims and trusted medical journals

            Present the influencers in order from highest to lowest following. The JSON structure should be as follows:

            {
                "influencers": [
                    {       
                        "name": "",
                        "totalFollowing": 0,
                        "trustScore": 0
                    },
                    ...
                ]
            }

            Ensure all data is up-to-date and accurately reflects current information. Base the trust score on verifiable claims and reputable medical sources. Rank the influencers based on their given trust score.
            RETURN ONLY THE JSON FILE!"""
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


def get_claims(name):

    settings = Settings()

    api_key = settings.api_key

    messages = [
        {
            "role": "system",
            "content": (
                "You are a detailed artificial intelegence and you will try harder to fill in all the information requested"
            ),
        },
        {
            "role": "user",
            "content": (
                        f"""Generate a JSON response about {name}'s 3 most recent health claims using the following structure: {
                            
                            "claims": [
                                {
                                "Claim": "[Claim x]", 
                                "brief": "[Brief description of the claim]",
                                "source":"[Source title and date]",
                                "claim": "[Detailed description of the claim]",
                                "medicalEvidence": {
                                    "source": "[Journal or expert name]",
                                    "excerpt": "[Relevant excerpt from a medical journal or expert opinion]"
                                },
                                "verdict": "[Confirmed or Debunked]"
                                },
                                ...
                                ]
                            } 


                            Ensure that the response includes three of {name}'s most recent health claims, with accurate and up-to-date information. Maintain a neutral, fact-based tone throughout the analysis and avoid duplicate claims.
                            Return ONLY the json file."""
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