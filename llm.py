from litellm import completion
from pydantic import BaseModel

class Response(BaseModel):
    is_news: bool
    is_weather: bool
    is_location: bool

question = input("Enter your question: ")


response = completion(
        model="ollama/llama3.2:1b", 
        messages=[
            { 
             "role":"system","content": (
            "you are an expert classifier.given a user's question,respond ONLY with a JSON object in this format: \n."
            "{\n"
            ' "is_news": true/false,\n'
            ' "is_weather": true/false,\n'
            ' "is_location": true/false\n'
            "}\n"
            "Guidelines:\n"
            "- Set is_news to true if the question is about current events or news,or recent happeninngs (for example'what happened in madurai)"
            "- set is_weather to true if the question is about weather,temperature,rainfall,or weather conditions,\n"
            "- set is_location to the location of the question if it is about a specific location or weather.\n"
            "- Do not include any explanation,commentary,or extra text.only output the JSON object.\n"
           } ),
          {"role": "user","content":question  }, 
        
        ],
            
        api_base="http://localhost:11434",
        temperature=0.1,
        max_tokens=100,
        response_format=identifier
     )
    




