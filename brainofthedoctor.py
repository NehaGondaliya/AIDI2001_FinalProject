#Step-1:setup groq api key
import os
GROQ_API_KEY = os.environ.get("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")


#step-2:convert image to required format
import base64

#image_path="acne.jpg"
def encode_image(image_path): 
    image_file=open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#step-3:setup multimodle llm
from groq import Groq

query="Is there something wrong with my face?"
model="llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key="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")
    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content


'''
#example 2
image_path="dandruff.jpg"
image_file=open(image_path,"rb")
encoded_image=base64.b64encode(image_file.read()).decode('utf-8')


#step-3:setup multimodle llm
from groq import Groq

client = Groq(api_key="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")
query="Is there something wrong with my hair?"
model="llama-3.2-90b-vision-preview"
messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
chat_completion=client.chat.completions.create(
    messages=messages,
    model=model
)

print(chat_completion.choices[0].message.content)

'''