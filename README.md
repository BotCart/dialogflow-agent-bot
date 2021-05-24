# Chatwoot Agent Bot Implementation using DialogFlow

![chat-958d13cc16f58d1649ab8a35bb579586](https://user-images.githubusercontent.com/73185/107608463-129ff600-6c62-11eb-84f4-1dc1ebdbf1de.gif)

This repo contains a sample python api which acts an agent bot.
It relies on google dialogflow to for its NLP processing and makes use of bot messages in chatwoot to deliver a rich experiance.

## Getting Started on Local

### Set up Dialogflow

1) Create a google cloud Project [ Unless you already have one]
2) Create a Dialogflow ES Bot under the project
3) Go to small talk and enable the small talk
4) Go to Intents and import the given intenets in `dialogflow_intents` folder in this repo.

### Setup Chatwoot installation
1) Create an AgentBot by running the following in your chatwoot rails console
```
bot = AgentBot.create!(name: "Booking Bot", outgoing_url: "http://localhost:4000")
AgentBotInbox.create!(inbox: Inbox.first, agent_bot: bot)
# returns the token
bot.access_token.token

# if you want to update the image of the bot
avatar_resource = LocalResource.new("your image url")
AgentBot.first.avatar.attach(io: avatar_resource.file, filename: avatar_resource.tmp_filename, content_type: avatar_resource.encoding)
```
### Setting Up the Repo
1) Clone the repo to your local
2) Copy `.env.example` to `.env` and update the values as mentions
3) run `python manage.py runserver 0.0.0.0:8000`
