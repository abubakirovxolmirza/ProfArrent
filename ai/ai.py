from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
# from quiz.models import Question, Options
from openai import OpenAI
import os
def chatbot_first(message):
    # questions = Question.objects.all()
# options = Options.objects.all()

    # Generating strings for questions and options
    #question_str = "\n".join([str(question) for question in questions])
    #options_str = "\n".join([str(option) for option in options])
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            
            # {"role": "system", "content": "You are a laconic assistant. You reply with brief, to-the-point answers with no elaboration."},
            {"role": "user", "content": f'''I wrote answers to tests to determine my interest and to find out in which field I could work. Please indicate my interest based on the answers and questions of these tests. My responses are: {message}. Please tell me which field you are interested in. Give full details of this interest. Enter the information in this order:
		I wrote answers to tests to determine my interest and to find out in which field I could work. Please indicate my interest based on the answers and questions of these tests. My responses are: {message}. Please tell me which field you are interested in. Give full details of this interest. Enter the information in this order:

	1. What area of ​​life am I interested in?
	2. View the test analysis and provide information about the path to vision in this profession or interest. That is, give a list of occupations for the main stages of creating a career. Give information about the current professions in a new form and with what professions they will be combined in the future.
	3. Write my road map step by step, connecting my interests with professions.
	4. Tell me which companies have jobs now. You must mention the companies.
	5. Tell me about TOP jobs, resume builders to work in the profession you are interested in?

	Don't talk about me, start talking about your interest. Just say you. Don't speak for me.
	Answer for all questions in Uzbek, I only understand Uzbek!'''},
	 ],
        temperature=0,
    )

    return response.choices[0].message.content

def chatbot_second(message):
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            
            # {"role": "system", "content": "You are a laconic assistant. You reply with brief, to-the-point answers with no elaboration."},
            {"role": "user", "content": f'''I wrote answers to tests to determine my interest and to find out in which field I could work. Please indicate my interest based on the answers and questions of these tests. My responses are: {message}. Please tell me which field you are interested in. You can tell by keyword how close I am to this field.

	1. interest: "Mathematics", keyword: "<math>"
	2. interest: "Biology", keyword: "<bio>"
	3. interest: "Mobleography", keyword: "<mobile>"
	4. interest: "No-code", keyword: "<ncode>"
	5. interest: "Videomontage", keyword: "<vmontage>"
	6. interest: "HR (human resources)", keyword: "<hrk>"
	7. interest: "PR (Public Relations)", keyword: "<prk>"
	8. interest: "interest in SAT course", keyword: "<satt>"

	If my passion is not in the information I provide, bring another field yourself. Depending on the interest, you can send me 3 keywords of interest and the percentage of how much I can adjust. And those 3 keywords must include at least one of the interests I've given. You must choose one of the 8 professions I have given. After determining my interest. Submit your reply as:
	1. keyword="<bio>", percentage=60%
	2. keyword="<hrk>", percentage=40%
	3. keyword="<satt>", interest=30%

	I just showed you as an example. There may be other areas here. Answer in Uzbek, I only understand Uzbek'''},


        ],
        temperature=0,
    )

    return response.choices[0].message.content
