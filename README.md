# simplybot
**A python library to create telegram bots simply and easily**

<p align="center">
  <img src="https://telegra.ph/file/c177a1300e679d0630b9d.jpg" alt="thumb" width="600" height="300">
</p>

[![My Telegram Account](https://via.placeholder.com/150x50.png?text=My+Telegram+Account)](https://t.me/rizkykianadji)

[![My Telegram Groups](https://via.placeholder.com/150x50.png?text=My+Telegram+Groups)](https://t.me/operationemp)

[![My Official Sites](https://via.placeholder.com/150x50.png?text=My+Official+Sites)](https://ailibytes.xyz)


**Get started**

- First install the main bot library
```
pip install simplybot
```
# Example
```python
# initialize bot token
from simplybot import startBot

bot = startBot('token here')
# example send plain text message
def start(message, chat_id):
    bot.send_text(chat_id, "Hello %username! I'm your friendly telegram bot.", message=message)

# quoted message
bot.handle_command('start', start)
def quotedMessage(message, chat_id):
    bot.send_text(chat_id, "This is quoted message", quoted=message.message_id)

bot.handle_command('start', start)
bot.handle_command('quoted', quotedMessage)

bot.start_polling() # start the bot
```
# sending media
```python
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
# markup/callback message
```python
def start(message, chat_id):

    # Define the buttons
    payloads = {
        'button': [
            {
                'rows': [
                    {
                        'type': 'inline',
                        'displayText': 'Option 1',
                        'callback': 'option_1'
                    },
                    {
                        'type': 'inline',
                        'displayText': 'Option 2',
                        'callback': 'option_2'
                    },
                ]
            }
        ]
    }

    # Send the message with buttons
    bot.send_message_with_buttons(chat_id, "Click button below", payloads)

def handle_option_1(call, chat_id):
    # Respond to Option 1 button press
    bot.send_text(chat_id, "You selected Option 1!")

def handle_option_2(call, chat_id):
    # Respond to Option 2 button press
    bot.send_text(chat_id, "You selected Option 2!")
```
