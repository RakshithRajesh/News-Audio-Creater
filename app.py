from requests_html import HTMLSession
from gtts import gTTS

s = HTMLSession()
r = s.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")

news = r.html.find('a[class="DY5T1d RZIKme"]')
news_list = [x.text for x in news]

text = ""
for i in news_list:
    text += i
    text += " "

print(text)

mytext = text
language = "en"

speech = gTTS(text=mytext, lang=language, slow=False)
speech.save("speech.mp3")
