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
            {"role": "user", "content": f'''I have a platform where user can express their interest and tell in which field of IT field they can work. I need to test this process. 
                I have given users these tests:1. Loyihani amalga oshirishda qaysi jihatga ko'proq e'tibor berishni yoqtirasiz?
   A. Foydalanuvchi interfeysi va foydalanuvchi tajribasini yaratish.
   B. Funksionallik va sahna ortidagi logikani rivojlantirish.
   C. Tizim xavfsizligi va barqarorligini ta'minlash.
   D. Ishlash va kengayuvchanlikni optimallashtirish.

2. Qaysi dasturlash tilidan ko'proq foydalanish qulay?
   A. HTML/CSS/JavaScript
   B. Java/C#/Python
   C. SQL
   D. C++/Go/Rust

3. Sizni ishingizda eng ko'p nima motivatsiya qiladi?
   A. Ko'rkam va intuitiv interfeyslar yaratish.
   B. Murakkab muammolarni hal qilish va samarali algoritmlar ishlab chiqish.
   C. Ma'lumotlarni himoya qilish va kiberxavfsizlikka qarshi kurashish.
   D. Og'ir yuklarni ko'tara oladigan yuqori samarali tizimlar qurish.

4. Qaysi loyiha sizni eng qiziqarli qiladi?
   A. Chiroyli animatsiyalarga ega moslashuvchan veb-sayt yaratish.
   B. Mustahkam va kengaytiriladigan elektron tijorat platformasini qurish.
   C. Xavfsiz ma'lumotlar bazasini boshqarish tizimini loyihalash va amalga oshirish.
   D. Maksimal tezlik va ishonchlilik uchun tarmoq infratuzilmasini optimallashtirish.

5. Jamoaviy ishda qaysi rolga ko'proq moyil bo'lasiz?
   A. UI/UX dizayner
   B. Dasturiy ta'minot ishlab chiquvchisi/muhandisi
   C. Kiberxavfsizlik tahlilchisi
   D. Tizim administratori/tarmoq muhandisi

6. IT sohasida qaysi jihat sizni ko'proq qiziqtiradi?
   A. Foydalanuvchi uchun qulay va yoqimli tajribalar yaratish.
   B. Samarali va chiroyli kod yozish.
   C. Kiberxavfsizlik tahdidlari bilan kurashish va tizimlarni xavfsiz saqlash.
   D. Barqaror IT infratuzilmalarini qurish va saqlash.

7. Muammo bilan yuzlashganda qanday yondashuvni afzal ko'rasiz?
   A. Mumkin bo'lgan yechimlar va chizmalarni chizish.
   B. Muammoni boshqarish oson bo'lgan qismlarga ajratish va algoritmlar ishlab chiqish.
   C. Xavfsizlik zaifliklarini tahlil qilish va himoya choralarini ishlab chiqish.
   D. Turli tizim konfiguratsiyalarini sinab ko'rish va optimallashtirish.

8. Sizni qaysi texnologiya ko'proq qiziqtiradi?
   A. Veb-dizayn va foydalanuvchi tajribasi
   B. Sun'iy intellekt va mashina o'rganish
   C. Kiberxavfsizlik va kriptografiya
   D. Bulutli hisoblash va tarmoq

9. Ishlayotgan tizimingizning xavfsizligini qanday ta'minlaysiz?
   A. Foydalanuvchi ma'lumotlarini shifrlash.
   B. Qattiq autentifikatsiya va ruxsatnomalarni o'rnatish.
   C. Xavfsizlik zaifliklarini muntazam skanerlash.
   D. Zaxira nusxalarini muntazam ravishda yaratish.

10. Dasturiy ta'minot ishlab chiqishda qaysi metodologiyani afzal ko'rasiz?
    A. Agile
    B. Scrum
    C. Kanban
    D. Waterfall

11. Dasturiy ta'minot loyihangizni qanday boshqarasiz?
    A. Jira yoki Trello kabi vositalardan foydalanish.
    B. Kod versiyalari va branchlar bilan ishlash.
    C. Testlarni avtomatlashtirish va CI/CD jarayonlarini o'rnatish.
    D. Foydalanuvchilar bilan muloqot qilish va ularning fikr-mulohazalarini qabul qilish.

12. Qaysi dasturlash vositalaridan foydalanishni yoqtirasiz?
    A. Visual Studio Code yoki Sublime Text
    B. Eclipse yoki IntelliJ IDEA
    C. MySQL Workbench yoki SQL Server Management Studio
    D. Terminal va komanda qatori vositalari

13. Qaysi operatsion tizim bilan ishlashni afzal ko'rasiz?
    A. Windows
    B. macOS
    C. Linux
    D. BSD

14. Siz uchun muhim bo'lgan mahoratlar qaysilar?
    A. Dizayn va animatsiya
    B. Algoritmlar va ma'lumotlar tuzilmalari
    C. Xavfsizlik va shifrlash
    D. Tarmoq va tizim boshqaruvi

15. Qaysi soha sizni ko'proq qiziqtiradi?
    A. Veb-dasturlash
    B. Mobil dasturlash
    C. Ma'lumotlar bazasi boshqaruvi
    D. Bulutli hisoblash

16. Qaysi texnologiya tendensiyasi sizni ko'proq hayajonlantiradi?
    A. Sun'iy intellekt va mashina o'rganish
    B. Blokcheyn va kriptovalyutalar
    C. Internet of Things (IoT)
    D. Katta ma'lumotlar va tahlil             

17. Qaysi dasturlash paradigmasi sizni qiziqtiradi?
    A. Obyektga yo'naltirilgan dasturlash
    B. Funktsional dasturlash
    C. Imperativ dasturlash
    D. Deklarativ dasturlash

18. Tizim xavfsizligi uchun qanday choralar ko'rasiz?
    A. Antivirus dasturlarini yangilab turish.
    B. Firefall va IDS/IPS tizimlarini sozlash.
    C. Xavfsizlik tekshirishlarini o'tkazish va tahlil qilish.
    D. Foydalanuvchi huquqlarini boshqarish va cheklash.

19. Yangi texnologiyalarni qanday o'rganasiz?
    A. Onlayn kurslar va videodarslar orqali.
    B. Kitoblar va bloglar o'qish orqali.
    C. Amaliy loyihalar va tajribalar orqali.
    D. Seminarlar va konferensiyalar orqali.

20. IT sohasida o'z karyerangizni qanday rivojlantirmoqchisiz?
    A. Dizayn va UX bo'yicha mutaxassis bo'lish.
    B. Ilg'or dasturlash va algoritmlar bo'yicha mutaxassis bo'lish.
    C. Xavfsizlik bo'yicha mutaxassis bo'lish.
    D. Tizim boshqaruvi va tarmoq bo'yicha mutaxassis bo'lish.


             I am sending you now the test taker's answers to these tests: {message}.First tell me what field of IT this user is interested in. By complete information, they mean: What is the field of BU itself? What are similar industries to this industry? How can you find a future job in this field? and the last question is to write down the roadmap information for the study of this field.Return the answer in Uzbek.'''},
        ],
        temperature=0,
    )

    return response.choices[0].message.content

def chatbot_second(message):
    #questions = Question.objects.all()
    #options = Options.objects.all()

    
    #question_str = "\n".join([str(question) for question in questions])
    #options_str = "\n".join([str(option) for option in options])
    MODEL = "gpt-3.5-turbo"
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            
            # {"role": "system", "content": "You are a laconic assistant. You reply with brief, to-the-point answers with no elaboration."},
            {"role": "user", "content": f'''I have a platform where user can express their interest and tell in which field of IT field they can work. I need to test this process. 
                I have given users these tests: 1. Loyihani amalga oshirishda qaysi jihatga ko'proq e'tibor berishni yoqtirasiz?
   A. Foydalanuvchi interfeysi va foydalanuvchi tajribasini yaratish.
   B. Funksionallik va sahna ortidagi logikani rivojlantirish.
   C. Tizim xavfsizligi va barqarorligini ta'minlash.
   D. Ishlash va kengayuvchanlikni optimallashtirish.

2. Qaysi dasturlash tilidan ko'proq foydalanish qulay?
   A. HTML/CSS/JavaScript
   B. Java/C#/Python
   C. SQL
   D. C++/Go/Rust

3. Sizni ishingizda eng ko'p nima motivatsiya qiladi?
   A. Ko'rkam va intuitiv interfeyslar yaratish.
   B. Murakkab muammolarni hal qilish va samarali algoritmlar ishlab chiqish.
   C. Ma'lumotlarni himoya qilish va kiberxavfsizlikka qarshi kurashish.
   D. Og'ir yuklarni ko'tara oladigan yuqori samarali tizimlar qurish.

4. Qaysi loyiha sizni eng qiziqarli qiladi?
   A. Chiroyli animatsiyalarga ega moslashuvchan veb-sayt yaratish.
   B. Mustahkam va kengaytiriladigan elektron tijorat platformasini qurish.
   C. Xavfsiz ma'lumotlar bazasini boshqarish tizimini loyihalash va amalga oshirish.
   D. Maksimal tezlik va ishonchlilik uchun tarmoq infratuzilmasini optimallashtirish.

5. Jamoaviy ishda qaysi rolga ko'proq moyil bo'lasiz?
   A. UI/UX dizayner
   B. Dasturiy ta'minot ishlab chiquvchisi/muhandisi
   C. Kiberxavfsizlik tahlilchisi
   D. Tizim administratori/tarmoq muhandisi

6. IT sohasida qaysi jihat sizni ko'proq qiziqtiradi?
   A. Foydalanuvchi uchun qulay va yoqimli tajribalar yaratish.
   B. Samarali va chiroyli kod yozish.
   C. Kiberxavfsizlik tahdidlari bilan kurashish va tizimlarni xavfsiz saqlash.
   D. Barqaror IT infratuzilmalarini qurish va saqlash.

7. Muammo bilan yuzlashganda qanday yondashuvni afzal ko'rasiz?
   A. Mumkin bo'lgan yechimlar va chizmalarni chizish.
   B. Muammoni boshqarish oson bo'lgan qismlarga ajratish va algoritmlar ishlab chiqish.
   C. Xavfsizlik zaifliklarini tahlil qilish va himoya choralarini ishlab chiqish.
   D. Turli tizim konfiguratsiyalarini sinab ko'rish va optimallashtirish.

8. Sizni qaysi texnologiya ko'proq qiziqtiradi?
   A. Veb-dizayn va foydalanuvchi tajribasi
   B. Sun'iy intellekt va mashina o'rganish
   C. Kiberxavfsizlik va kriptografiya
   D. Bulutli hisoblash va tarmoq

9. Ishlayotgan tizimingizning xavfsizligini qanday ta'minlaysiz?
   A. Foydalanuvchi ma'lumotlarini shifrlash.
   B. Qattiq autentifikatsiya va ruxsatnomalarni o'rnatish.
   C. Xavfsizlik zaifliklarini muntazam skanerlash.
   D. Zaxira nusxalarini muntazam ravishda yaratish.

10. Dasturiy ta'minot ishlab chiqishda qaysi metodologiyani afzal ko'rasiz?
    A. Agile
    B. Scrum
    C. Kanban
    D. Waterfall

11. Dasturiy ta'minot loyihangizni qanday boshqarasiz?
    A. Jira yoki Trello kabi vositalardan foydalanish.
    B. Kod versiyalari va branchlar bilan ishlash.
    C. Testlarni avtomatlashtirish va CI/CD jarayonlarini o'rnatish.
    D. Foydalanuvchilar bilan muloqot qilish va ularning fikr-mulohazalarini qabul qilish.

12. Qaysi dasturlash vositalaridan foydalanishni yoqtirasiz?
    A. Visual Studio Code yoki Sublime Text
    B. Eclipse yoki IntelliJ IDEA
    C. MySQL Workbench yoki SQL Server Management Studio
    D. Terminal va komanda qatori vositalari

13. Qaysi operatsion tizim bilan ishlashni afzal ko'rasiz?
    A. Windows
    B. macOS
    C. Linux
    D. BSD

14. Siz uchun muhim bo'lgan mahoratlar qaysilar?
    A. Dizayn va animatsiya
    B. Algoritmlar va ma'lumotlar tuzilmalari
    C. Xavfsizlik va shifrlash
    D. Tarmoq va tizim boshqaruvi

15. Qaysi soha sizni ko'proq qiziqtiradi?
    A. Veb-dasturlash
    B. Mobil dasturlash
    C. Ma'lumotlar bazasi boshqaruvi
    D. Bulutli hisoblash

16. Qaysi texnologiya tendensiyasi sizni ko'proq hayajonlantiradi?
    A. Sun'iy intellekt va mashina o'rganish
    B. Blokcheyn va kriptovalyutalar
    C. Internet of Things (IoT)
    D. Katta ma'lumotlar va tahlil 

17. Qaysi dasturlash paradigmasi sizni qiziqtiradi?
    A. Obyektga yo'naltirilgan dasturlash
    B. Funktsional dasturlash
    C. Imperativ dasturlash
    D. Deklarativ dasturlash

18. Tizim xavfsizligi uchun qanday choralar ko'rasiz?
    A. Antivirus dasturlarini yangilab turish.
    B. Firefall va IDS/IPS tizimlarini sozlash.
    C. Xavfsizlik tekshirishlarini o'tkazish va tahlil qilish.
    D. Foydalanuvchi huquqlarini boshqarish va cheklash.

19. Yangi texnologiyalarni qanday o'rganasiz?
    A. Onlayn kurslar va videodarslar orqali.
    B. Kitoblar va bloglar o'qish orqali.
    C. Amaliy loyihalar va tajribalar orqali.
    D. Seminarlar va konferensiyalar orqali.

20. IT sohasida o'z karyerangizni qanday rivojlantirmoqchisiz?
    A. Dizayn va UX bo'yicha mutaxassis bo'lish.
    B. Ilg'or dasturlash va algoritmlar bo'yicha mutaxassis bo'lish.
    C. Xavfsizlik bo'yicha mutaxassis bo'lish.
    D. Tizim boshqaruvi va tarmoq bo'yicha mutaxassis bo'lish.
             

             I am sending you now the test taker's answers to these tests: {message}. Second, provide complete information on the field of interest for this user. By complete information, they mean: What is the field of BU itself? What are similar industries to this industry? How can you find a future job in this field? and the last question is to write down the roadmap information for the study of this field.Return the answer in Uzbek.'''},
        ],
        temperature=0,
    )

    return response.choices[0].message.content
