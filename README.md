# simplybot
**A python library to create telegram bots simply and easily**
<div style="align: center;">
  <a href="https://t.me/rizkykianadji" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: #fff; background-color: #0088cc; text-align: center; text-decoration: none; border-radius: 5px;">
    <img src="https://img.shields.io/badge/Telegram-Join%20Chat-blue" alt="My Telegram Account" style="vertical-align: middle; border: none;">
  </a>

  <a href="https://t.me/operationemp" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: #fff; background-color: #0088cc; text-align: center; text-decoration: none; border-radius: 5px; margin-left: 10px;">
    <img src="https://img.shields.io/badge/Telegram-Groups-blue" alt="My Telegram Groups" style="vertical-align: middle; border: none;">
  </a>

  <a href="https://ailibytes.xyz" style="display: inline-block; padding: 10px 20px; font-size: 16px; font-weight: bold; color: #fff; background-color: #0088cc; text-align: center; text-decoration: none; border-radius: 5px; margin-left: 10px;">
    <img src="https://img.shields.io/badge/Website-Visit%20Now-blue" alt="My Official Sites" style="vertical-align: middle; border: none;">
  </a>
</div>

<p align="center">
  <img src="https://telegra.ph/file/c177a1300e679d0630b9d.jpg" alt="thumb" width="600" height="300">
</p>

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
# other
```python
# send quiz & polling message
def quiz(message, chat_id):
    polling_message = {
        'description': 'What is the capital of France?',
        'rows': [
            {
                'name': 'Paris',
                'isCorrectAnswers': True
            },
            {
                'name': 'London',
                'isCorrectAnswers': False
            },
            {
                'name': 'Berlin',
                'isCorrectAnswers': False
            }
        ],
        'isAnonymous': False,
        'isQuizVote': True,
        'allowMultipleVote': False,
        'explanation': 'The capital of France is Paris.'
    }
    bot.send_poll(chat_id, polling_message)

# send contact
bot.send_contact(chat_id, '+1234567890', 'John')
# send location
bot.send_location(chat_id, 37.7749, -122.4194)
```

