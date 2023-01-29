from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

from django.shortcuts import render
import json

def translate(request):
    dataset = {
        "ผมเป็นคนไทย": "I am Thai",
        "เขาชอบทำกิจกรรมกลางแจ้ง": "He likes outdoor activities",
        "เธอคิดถึงฉันบ่อยแล้ว": "She thinks of me often",
        "คุณชอบดนตรีมากแค่ไหน": "How much do you like music?",
        "สวัสดีค่ะ": "Hello",
        "การที่เรามาร่วมงานเป็นเรื่องดี": "It's good that we came to the event",
        "คุณจะไปเที่ยวประเทศไหน": "Which country will you travel to?",
        "ฉันต้องไปทำงาน": "I have to go to work",
        "เขาเป็นคนที่รักความสะดวก": "He is a comfort-loving person",
        "เราต้องการเพิ่มความรู้": "We want to increase knowledge",
        "เขาเป็นคนที่มีความรู้": "He is a knowledgeable person",
        "เขาเป็นคนที่มีความรู้มาก": "He is a very knowledgeable person",
        "ฉันชอบกินข้าว": "I like to eat rice",
        "ฉันชอบกินข้าวมาก": "I like to eat rice a lot",
        "เขาชอบเดินทางและเที่ยวทั่วโลก": "He likes traveling and exploring the world",
        "ฉันต้องการพักผ่อนหนึ่งวัน": "I want to take a day off",
        "วันหยุดนี้เราจะไปเที่ยวเมือง": "We will travel to the city on this holiday",
        "คุณมีอะไรที่ชอบมากที่สุด": "What do you like the most?",
        "ฉันชอบชมพรรษา": "I like watching festivals",
        "เขาเป็นคนรักสัตว์": "He is an animal-loving person",
        "คุณชอบสถานที่เที่ยวบ้าง": "Do you like visiting places sometimes?",
        "ฉันต้องเดินไปทางโรงเรียน": "I have to walk to the school",
        "เราชอบเที่ยวเมืองหลัก": "We like visiting the capital city",
        "คุณชอบอาหารไทยบ้าง": "Do you like Thai food sometimes?",
        "ฉันชอบกินข้าวมากกว่ากินข้าวเหนียว": "I like to eat rice more than to eat sticky rice",
        "เขาชอบกินข้าวมากกว่ากินข้าวเหนียว": "He likes to eat rice more than to eat sticky rice",
        "ฉันต้องการเดินทางไปที่ใหม่": "I want to travel to a new place",
        "สวัสดีวันจันทร์": "Hello Monday",
        "คุณรักสิ่งอันสวยงามหรือไม่": "Do you love beautiful things?",
        "เขาเป็นคนที่ชอบการศึกษา": "He likes learning",
        "อาหารของเราอร่อย": "Our food is delicious",
        "ฉันรักการทำกิจกรรมกลางแจ้ง": "I love outdoor activities",
        "คุณชอบกินข้าวกล่องหรือไม่": "Do you like eating boxed rice?",
        "นายขอขอบคุณ": "Thank you sir",
        "ฉันต้องการเรียนรู้ภาษาใหม่": "I want to learn a new language",
        "เขาเป็นคนที่ชอบเดินทาง": "He likes traveling",
        "ฉันเชื่อว่าวันนี้จะเป็นวันที่ดี": "I believe today will be a good day",
        "ฉันรักคุณ": "I love you",
        "คุณชอบนั่งดูละครหรือไม่": "Do you like watching dramas?",
        "คุณชอบการศึกษาวิทยาศาสตร์หรือไม่": "Do you like studying science?",
        "ฉันรักคุณ": "I love you",
        "คุณชอบอาหารไทยหรือไม่": "Do you like Thai food?",
        "ผมชอบกินข้าวกล่อง": "I like eating takeout",
        "เขาอยู่ที่บ้านตอนนี้": "He is at home now",
        "ฉันเข้าใจ": "I understand",
        "ฉันไม่เข้าใจ": "I don't understand",
        "สวัสดีวันจันทร์": "Good Monday",
        "คุณชอบวิทยุหรือเพลงออนไลน์": "Do you prefer radio or online music?",
        "ฉันกำลังเดินทางไปราชบุรี": "I am traveling to Ratchaburi",
        "การประชุมจะเริ่มต้นในอีก 15 นาที": "The meeting will start in another 15 minutes",
        "ฉันกำลังพักผ่อนอยู่ที่ชลบุรี": "I am on vacation in Chonburi",
        "เราต้องการเย็นตามร้าน": "We want to eat out",
        "ฉันรักภาพยนตร์": "I love movies",
        "คุณชอบร้านอาหารประเภทใด": "What type of restaurant do you like?",
        "ฉันรักเพลงแบบสบายๆ": "I love easy-listening music",
        "ฉันกำลังเดินทางไปราชบุรี": "I am traveling to Ratchaburi",

    }
    if request.method == "POST":
        selected_thai = request.POST.get("thai_sentence")
        english_meaning = dataset[selected_thai]
        return render(request, "result.html", {"english_meaning": english_meaning, "selected_thai": selected_thai})
    return render(request, "translate.html", {"thai_sentences": dataset.keys()})
