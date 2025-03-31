from google import genai
from google.genai import types
from dotenv import dotenv_values

config = dotenv_values(".env")

client = genai.Client(api_key=config['API_KEY'])

def genarate_blog(paragraph_topic):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents='Write a paragraph about the following topic. ' + paragraph_topic,
        config=types.GenerateContentConfig(
        max_output_tokens=400,
        temperature=0.3
    )
    )
    
    retrieve_blog = response.text
    return retrieve_blog

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no. ')
    if (answer == 'Y'):
        paragraph_topic = input('What should this paragraph talk about? ')
        print(genarate_blog(paragraph_topic))
    else:
        keep_writing = False


