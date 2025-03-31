from google import genai
from google.genai import types

# client = genai.Client(api_key="AIzaSyA5eqw2zMyAjqtI8-o5KM04aSg7y-n5Z_U")

# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents=["Explain how AI works in a few words"]
# )
# print(response.text)

client = genai.Client(api_key="AIzaSyA5eqw2zMyAjqtI8-o5KM04aSg7y-n5Z_U")

def genarate_blog(paragraph_topic):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents='Write a paragraph about the following topic. ' + paragraph_topic,
        config=types.GenerateContentConfig(
        max_output_tokens=400,
        temperature=0.3
    )
    )
    
    # Access the text from the response
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

# print(genarate_blog('Why NYC is better than your city.'))

