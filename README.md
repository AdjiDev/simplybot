# simplybot
**A python library to create telegram bots simply and easily**

<p align="center">
  <img src="https://telegra.ph/file/c177a1300e679d0630b9d.jpg" alt="thumb" width="600" height="300">
</p>

<a href="https://t.me/rizkykianadji" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: #fff; background-color: #0088cc; text-align: center; text-decoration: none; border-radius: 5px;">
  My telegram account
</a>
<a href="https://t.me/operationemp" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: #fff; background-color: #0088cc; text-align: center; text-decoration: none; border-radius: 5px;">
  My telegram groups
</a>
<a href="https://ailibytes.xyz" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: #fff; background-color: #0088cc; text-align: center; text-decoration: none; border-radius: 5px;">
  My official sites
</a>

**Get started**
`1. Main`
 First install the main bot library
```
pip install simplybot
```
# initialize bot token
```python
from simplybot import startBot

bot = startBot('token here')
```
# example send plain text message
```
def start(message, chat_id):
    bot.send_text(chat_id, "Hello %username! I'm your friendly telegram bot.", message=message)

bot.handle_command('start', start)
```
- quoted message
```
def quotedMessage(message, chat_id):
    bot.send_text(chat_id, "This is quoted message", quoted=message.message_id)
```
`2. Sending media`
```
def send_media_messages(message, chat_id):
    # Send an image from a URL
    image_url = "https://example.com/path/to/image.jpg"
    bot.send_img(chat_id, image_url, caption="Here is an image from a URL!")

    # Send an image from a local file path
    local_image_path = "path/to/local/image.jpg"
    bot.send_img(chat_id, local_image_path, caption="Here is an image from a local file!")

    # Send a video from a local file path
    local_video_path = "path/to/local/video.mp4"
    bot.send_video(chat_id, local_video_path, caption="Check out this video!")

    # Send an audio file from a local file path
    local_audio_path = "path/to/local/audio.mp3"
    bot.send_audio(chat_id, local_audio_path, caption="Listen to this audio!")

    # Send a document from a local file path
    local_doc_path = "path/to/local/document.pdf"
    bot.send_docs(chat_id, local_doc_path, mimetype="application/pdf")
```
