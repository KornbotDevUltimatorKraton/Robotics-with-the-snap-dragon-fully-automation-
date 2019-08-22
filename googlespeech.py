from google_speech import Speech

# say "Hello World"
text = "機器人系統"
lang3 = "zh"
lang2 = "th"
lang1 = "en"
sox_effects = ("speed", "1.14")
#speech = Speech(text, lang)
speech = Speech("Hello Welcome to smart toilet we keep your picture data as user identification",lang1)
speech.play(sox_effects)
speech = Speech("สวัสดีค่ะ ยินดีต้อนรับสู่ห้องนำ้อัจฉริยะค่ะ เราขอเก็บข้อมูลรูปภาพของคุณเพื่อใช้ในการระบุตัวผู้ใช้งาน",lang2)  # Thai language for the speech synt$
speech.play(sox_effects)
speech = Speech("您好，歡迎來到智能浴室。我們希望收集您的圖像數據以便識別",lang3)

#speech.play(sox_effects) # Speech fully play    
#speech.play()
# you can also apply audio effects while playing (using SoX)
# see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
#sox_effects = ("speed", "1.08")
speech.play(sox_effects)

