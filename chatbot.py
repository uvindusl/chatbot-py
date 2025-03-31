from google import genai

# client = genai.Client(api_key="AIzaSyA5eqw2zMyAjqtI8-o5KM04aSg7y-n5Z_U")

# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents=["Explain how AI works in a few words"]
# )
# print(response.text)

client = genai.Client(api_key="AIzaSyA5eqw2zMyAjqtI8-o5KM04aSg7y-n5Z_U")

def genarate_blog(paragraph_topic):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents='Write a paragraph about the following topic. ' + paragraph_topic
    )

    retrieve_blog = response
    return retrieve_blog

print(genarate_blog('Why NYC is better than your city.'))