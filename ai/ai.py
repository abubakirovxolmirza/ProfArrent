from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Text
# from quiz.models import Question, Options
from openai import OpenAI
import os
def chatbot_first(message):
    # questions = Question.objects.all()
# options = Options.objects.all()

    text = Text.objects.values_list("text")
    system = Text.objects.values_list("system")
    #question_str = "\n".join([str(question) for question in questions])
    #options_str = "\n".join([str(option) for option in options])
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            
            {"role": "system", "content": f'''{system}'''},
            {"role": "user", "content": f'''{text} {message}'''},
	 ],
        temperature=0,
    )

    return response.choices[0].message.content

def chatbot_second(message):
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))
    text = Text.objects.values_list("text2")
    system = Text.objects.values_list("system")
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            
           {"role": "system", "content": f'''{system}'''},
           {"role": "user", "content": f'''{text} {message}'''},
        ],
        temperature=0,
    )

    return response.choices[0].message.content
