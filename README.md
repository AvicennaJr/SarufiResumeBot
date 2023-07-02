# A Personalized Resume Bot With Sarufi

## First Things First

You'll need the following to follow a long:

- A Bot and API Key from Sarufi.
- A Bot and API Keys from Telegram.

### Getting Your API Key From Sarufi

- Log in to your Sarufi account
- Go to your profile settings
- Scroll down to Authorization section 
- Here you'll find your API key

### Creating A Bot In Sarufi

Here we will create a `knowledge based` bot from Sarufi. Selecting this option will allow you to upload your Resume in PDF format. Just make sure that the file is less than 6MBs. You can watch this [two minute video](https://www.youtube.com/watch?v=y8ECHo7Jabg) on how to create your Sarufi bot or you could follow along with the steps below:

- Go to dashboard then 'Create New Bot'
- Here you'll be presented with two options;
    i) Create from scratch
    ii) Create from knowledge base
  Select the option to create from knowledge base.
- Fill in the bot's name, description and industry.
- You'll then be presented with the option to upload a PDF or Word document. This will contain all the personalized knowledge you'll want your Resume bot to have about you. You can upload up to five documents but since we are making a Resume bot, one document should suffice. Remember that the resume must have a file size less than 6MB.
- You can also fill the `Custom Prompts`, `Max Tokens` and `Temperature` fields as shown below:
- Finally get your Sarufi Bot ID through the bot settings menu on the top right corner


### Getting API Keys from Telegram

- Log in with your Telegram account at https://my.telegram.org/
- Go to API Development Tools and fill out the form 
- You will get your API ID and API Hash 

### Creating A Telegram Bot

To create a new Telegram bot, simply message [@BotFather](https://t.me/BotFather) on telegram with the command /newbot. You will be prompted to fill in the bot's name and username. Fill these out and you will be provided with a token as shown below.

### Saving Credentials

Save all these credentials as a Python dictionary in the `keys.py` as shown below:

```python
keys = {
    "SARUFI_API_KEY": "your-api-key",
    "SARUFI_BOT_ID": "your-sarufi-bot-id",
    "TELEGRAM_API_ID": "your-telegram-api-id",
    "TELEGRAM_API_HASH": "your-telegram-api-hash",
    "TELEGRAM_BOT_TOKEN": "your-telegram-bot-token"
}
```
### Credits

Your's truly
