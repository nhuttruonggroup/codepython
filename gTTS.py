from gtts import gTTS
import os

# Văn bản bạn muốn chuyển đổi thành giọng nói
text = "Xin chào, đây là ví dụ về ứng dụng Text-to-Speech bằng Python."

# Tạo đối tượng gTTS
tts = gTTS(text)

# Lưu giọng nói thành một tệp âm thanh
tts.save("output.mp3")

# Phát tệp âm thanh bằng máy tính
os.system("mpg321 output.mp3")
