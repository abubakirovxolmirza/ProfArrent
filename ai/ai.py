from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
# from quiz.models import Question
from openai import OpenAI
import os
def chatbot_response(message):
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-prof-arrent-zKOsuRs7YPsO5JcIfU4XT3BlbkFJdkctDl18yT741q1Z0xjW"))

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            # {"role": "system", "content": "You are a laconic assistant. You reply with brief, to-the-point answers with no elaboration."},
            {"role": "user", "content": f"I am interested in these things {message}, which IT field can you choose for me based on my interest?"},
        ],
        temperature=0,
    )

    return response.choices[0].message.content
