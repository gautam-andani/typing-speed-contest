import openai
import json


def random_para_generator(paragraph_words):
       apikey = "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"        #It's an expired key so no need to worry
       openai.api_key = apikey
       openai.Model.list()

       completion = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[
       {"role": "user", "content": f"Generate a random paragraph for typing speed measure of about {paragraph_words} words."}
       ]
       )

       a=completion.choices[0].message
       return a['content']
