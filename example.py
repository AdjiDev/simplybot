from lib.handler import startBot

bot = startBot('token-here')

def handle_start(message, chat_id):
    bot.send_text(chat_id, "Hello! I'm a Telegram bot.")

bot.handle_command('start', handle_start)

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

bot.handle_command('quiz', quiz)

bot.start_polling()
