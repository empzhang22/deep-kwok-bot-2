An AI chatbot powered by GPT 2.0, trained to emulate a discord user.


TODO List:
- ~~Use the bot to extract Andrew's messages~~
    - Further optimization/adjustments (for future bots)
        - Splitting the writing from each channel into its own thread and using writewith to avoid close() problem
- Train a new model on those messages: TODO
    - Use this link: https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce
    - Further optimization/adjustments:
        - Using a larger model (512 instead of 124 MB)
        - Fine-tuning "creativity" parameter in gpt2.generate to create less optimal predictions that are more creative
        - Training on more data
- Upload that model to this bot and use it to respond to messages: TODO
    - When pinged
    - With a random probability
        - ~~Requires properly setting up Intents to read all messages, not just pings~~