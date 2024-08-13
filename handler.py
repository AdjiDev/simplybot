# lib/handler.py
"""
a python libray to build simple telegram bot more easy
by: adjisan - adjidev
github: https://github.com/adjidev
powered by: https://pypi.org/project/pyTelegramBotAPI/
"""

import telebot
import time
import requests

class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.callback_handlers = {}

    def send_text(self, chat_id, text, **kwargs):
        parse_mode = kwargs.get('parse_mode', 'Markdown')
        quoted = kwargs.get('quoted', None)
        self.bot.send_message(chat_id, text, parse_mode=parse_mode, reply_to_message_id=quoted)
    
    def send_img(self, chat_id, img_path_or_url, **kwargs):
        caption = kwargs.get('caption', None)
        if img_path_or_url.startswith('http://') or img_path_or_url.startswith('https://'):
            self.bot.send_photo(chat_id, photo=img_path_or_url, caption=caption)
        else:
            with open(img_path_or_url, 'rb') as photo:
                self.bot.send_photo(chat_id, photo=photo, caption=caption)
    
    def send_video(self, chat_id, video_path, **kwargs):
        caption = kwargs.get('caption', None)
        with open(video_path, 'rb') as video:
            self.bot.send_video(chat_id, video=video, caption=caption)
    
    def send_audio(self, chat_id, audio_path, **kwargs):
        caption = kwargs.get('caption', None)
        with open(audio_path, 'rb') as audio:
            self.bot.send_audio(chat_id, audio=audio, caption=caption)
    
    def send_docs(self, chat_id, doc_path, **kwargs):
        mime_type = kwargs.get('mimetype', 'application/octet-stream')
        with open(doc_path, 'rb') as document:
            self.bot.send_document(chat_id, document=document, mime_type=mime_type)
    
    def send_action(self, chat_id, action, **kwargs):
        delay = kwargs.get('delay', 0)
        self.bot.send_chat_action(chat_id, action)
        if delay > 0:
            time.sleep(delay)

    def send_location(self, chat_id, latitude, longitude, **kwargs):
        self.bot.send_location(chat_id, latitude, longitude)

    def send_contact(self, chat_id, phone_number, first_name, **kwargs):
        last_name = kwargs.get('last_name', None)
        self.bot.send_contact(chat_id, phone_number, first_name, last_name=last_name)

    def create_buttons(self, payloads):
        keyboard = telebot.types.InlineKeyboardMarkup()
        for button in payloads['button']:
            button_row = []
            for row in button['rows']:
                if row['type'] == 'inline':
                    button_row.append(telebot.types.InlineKeyboardButton(text=row['displayText'], callback_data=row['callback']))
                elif row['type'] == 'url':
                    button_row.append(telebot.types.InlineKeyboardButton(text=row['displayText'], url=row['link']))
            keyboard.add(*button_row)
        return keyboard

    def send_message_with_buttons(self, chat_id, text, payloads, **kwargs):
        parse_mode = kwargs.get('parse_mode', 'Markdown')
        self.bot.send_message(chat_id, text, parse_mode=parse_mode, reply_markup=self.create_buttons(payloads))

    def send_poll(self, chat_id, polling_message):
        options = [row['name'] for row in polling_message['rows']]
        self.bot.send_poll(
            chat_id, 
            question=polling_message['description'], 
            options=options,
            is_anonymous=polling_message['isAnonymous'], 
            allows_multiple_answers=polling_message.get('allowMultipleVote', False),
            type='quiz' if polling_message['isQuizVote'] else 'regular',
            correct_option_id=self.get_correct_option_id(polling_message) if polling_message['isQuizVote'] else None,
            explanation=polling_message.get('explanation', None) if polling_message['isQuizVote'] else None
        )

    def get_correct_option_id(self, polling_message):
        for index, row in enumerate(polling_message['rows']):
            if row.get('isCorrectAnswers', False):
                return index
        return None

    def handle_command(self, command, func):
        @self.bot.message_handler(commands=[command])
        def wrapper(message):
            chat_id = message.chat.id
            func(message, chat_id)
    
    def handle_callback(self, callback_data, func):
        self.callback_handlers[callback_data] = func

    def start_polling(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def handle_callback_query(call):
            callback_data = call.data
            if callback_data in self.callback_handlers:
                chat_id = call.message.chat.id
                self.callback_handlers[callback_data](call, chat_id)
        
        self.bot.polling()

def startBot(token):
    return TelegramBot(token)
