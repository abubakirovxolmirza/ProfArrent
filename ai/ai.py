from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
# from quiz.models import Question
from openai import OpenAI
import os
def chatbot_first(message):
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-prof-arrent-zKOsuRs7YPsO5JcIfU4XT3BlbkFJdkctDl18yT741q1Z0xjW"))

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            
            # {"role": "system", "content": "You are a laconic assistant. You reply with brief, to-the-point answers with no elaboration."},
            {"role": "user", "content": f'''I have a platform where user can express their interest and tell in which field of IT field they can work. I need to test this process. 
                I have given users these tests: When you're working on a project, what aspect do you enjoy focusing on the most?
                A. Designing the user interface and crafting the user experience.
                B. Developing the functionality and logic behind the scenes.
                C. Ensuring the security and stability of the system.
                D. Optimizing performance and scalability.
                Which programming language do you feel most comfortable using?
                A. HTML/CSS/JavaScript
                B. Java/C#/Python
                C. SQL
                D. C++/Go/Rust
                What motivates you the most in your work?
                A. Creating visually appealing and intuitive interfaces.
                B. Solving complex problems and implementing efficient algorithms.
                C. Protecting data and preventing cyber threats.
                D. Building high-performance systems that can handle heavy loads.
                Which of the following projects would you find most intriguing?
                A. Developing a responsive website with stunning animations.
                B. Building a robust and scalable e-commerce platform.
                C. Designing and implementing a secure database management system.
                D. Optimizing a network infrastructure for maximum speed and reliability.
                In a team setting, what role do you naturally gravitate towards?
                A. UI/UX designer
                B. Software developer/engineer
                C. Cybersecurity analyst
                D. Systems administrator/network engineer
                Which aspect of IT excites you the most?
                A. Creating seamless and enjoyable user experiences.
                B. Writing efficient and elegant code.
                C. Battling cyber threats and keeping systems safe.
                D. Building and maintaining robust IT infrastructures.
                When faced with a problem, what is your instinctive approach?
                A. Sketching out potential solutions and wireframes.
                B. Breaking down the problem into manageable chunks and devising algorithms.
                C. Analyzing security vulnerabilities and devising protective measures.
                D. Testing and optimizing various system configurations.. 
                When starting a new project, what do you prioritize first?
                A. Creating wireframes and mockups to visualize the user interface.
                B. Planning the architecture and outlining the structure of the codebase.
                C. Conducting risk assessments and implementing security protocols.
                D. Assessing hardware requirements and planning the network infrastructure.
                Which aspect of IT do you enjoy learning about the most?
                A. New design trends and user interaction patterns.
                B. Advanced algorithms and data structures.
                C. Emerging threats and cybersecurity protocols.
                D. Cutting-edge networking technologies and protocols.
                How do you approach debugging and troubleshooting?
                A. Testing different user scenarios to identify interface issues.
                B. Analyzing code logic and stepping through lines of code.
                C. Investigating potential security breaches and vulnerabilities.
                D. Monitoring system performance and analyzing network traffic.
                What would you consider your strongest skill?
                A. Creativity and attention to detail.
                B. Problem-solving and logical reasoning.
                C. Analytical thinking and risk assessment.
                D. Technical proficiency and system optimization.
                In which environment do you feel most comfortable working?
                A. Collaborative team settings with frequent feedback sessions.
                B. Independent work, focusing on deep problem-solving tasks.
                C. High-pressure situations requiring quick decision-making.
                D. Structured environments with defined processes and procedures.
                When considering career advancement, what aspect of IT interests you the most?
                A. Specializing further in user experience design or frontend development.
                B. Exploring new programming languages or mastering software engineering principles.
                C. Advancing into cybersecurity management or forensic analysis.
                D. Pursuing certifications in network architecture or cloud computing technologies.
                Which tech-related hobby or interest resonates with you the most?
                A. Graphic design or digital art.
                B. Competitive programming or algorithm challenges.
                C. Ethical hacking or cybersecurity competitions.
                D. Home networking setups or server administration.
             

             I am sending you now the test taker's answers to these tests: {message}.First tell me what field of IT this user is interested in. By complete information, they mean: What is the field of BU itself? What are similar industries to this industry? How can you find a future job in this field? and the last question is to write down the roadmap information for the study of this field.'''},
        ],
        temperature=0,
    )

    return response.choices[0].message.content

def chatbot_second(message):
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "sk-prof-arrent-zKOsuRs7YPsO5JcIfU4XT3BlbkFJdkctDl18yT741q1Z0xjW"))

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            
            # {"role": "system", "content": "You are a laconic assistant. You reply with brief, to-the-point answers with no elaboration."},
            {"role": "user", "content": f'''I have a platform where user can express their interest and tell in which field of IT field they can work. I need to test this process. 
                I have given users these tests: When you're working on a project, what aspect do you enjoy focusing on the most?
                A. Designing the user interface and crafting the user experience.
                B. Developing the functionality and logic behind the scenes.
                C. Ensuring the security and stability of the system.
                D. Optimizing performance and scalability.
                Which programming language do you feel most comfortable using?
                A. HTML/CSS/JavaScript
                B. Java/C#/Python
                C. SQL
                D. C++/Go/Rust
                What motivates you the most in your work?
                A. Creating visually appealing and intuitive interfaces.
                B. Solving complex problems and implementing efficient algorithms.
                C. Protecting data and preventing cyber threats.
                D. Building high-performance systems that can handle heavy loads.
                Which of the following projects would you find most intriguing?
                A. Developing a responsive website with stunning animations.
                B. Building a robust and scalable e-commerce platform.
                C. Designing and implementing a secure database management system.
                D. Optimizing a network infrastructure for maximum speed and reliability.
                In a team setting, what role do you naturally gravitate towards?
                A. UI/UX designer
                B. Software developer/engineer
                C. Cybersecurity analyst
                D. Systems administrator/network engineer
                Which aspect of IT excites you the most?
                A. Creating seamless and enjoyable user experiences.
                B. Writing efficient and elegant code.
                C. Battling cyber threats and keeping systems safe.
                D. Building and maintaining robust IT infrastructures.
                When faced with a problem, what is your instinctive approach?
                A. Sketching out potential solutions and wireframes.
                B. Breaking down the problem into manageable chunks and devising algorithms.
                C. Analyzing security vulnerabilities and devising protective measures.
                D. Testing and optimizing various system configurations.. 
                When starting a new project, what do you prioritize first?
                A. Creating wireframes and mockups to visualize the user interface.
                B. Planning the architecture and outlining the structure of the codebase.
                C. Conducting risk assessments and implementing security protocols.
                D. Assessing hardware requirements and planning the network infrastructure.
                Which aspect of IT do you enjoy learning about the most?
                A. New design trends and user interaction patterns.
                B. Advanced algorithms and data structures.
                C. Emerging threats and cybersecurity protocols.
                D. Cutting-edge networking technologies and protocols.
                How do you approach debugging and troubleshooting?
                A. Testing different user scenarios to identify interface issues.
                B. Analyzing code logic and stepping through lines of code.
                C. Investigating potential security breaches and vulnerabilities.
                D. Monitoring system performance and analyzing network traffic.
                What would you consider your strongest skill?
                A. Creativity and attention to detail.
                B. Problem-solving and logical reasoning.
                C. Analytical thinking and risk assessment.
                D. Technical proficiency and system optimization.
                In which environment do you feel most comfortable working?
                A. Collaborative team settings with frequent feedback sessions.
                B. Independent work, focusing on deep problem-solving tasks.
                C. High-pressure situations requiring quick decision-making.
                D. Structured environments with defined processes and procedures.
                When considering career advancement, what aspect of IT interests you the most?
                A. Specializing further in user experience design or frontend development.
                B. Exploring new programming languages or mastering software engineering principles.
                C. Advancing into cybersecurity management or forensic analysis.
                D. Pursuing certifications in network architecture or cloud computing technologies.
                Which tech-related hobby or interest resonates with you the most?
                A. Graphic design or digital art.
                B. Competitive programming or algorithm challenges.
                C. Ethical hacking or cybersecurity competitions.
                D. Home networking setups or server administration.
             

             I am sending you now the test taker's answers to these tests: {message}. Second, provide complete information on the field of interest for this user. By complete information, they mean: What is the field of BU itself? What are similar industries to this industry? How can you find a future job in this field? and the last question is to write down the roadmap information for the study of this field.'''},
        ],
        temperature=0,
    )

    return response.choices[0].message.content
