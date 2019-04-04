# serverless-chatbot-demo
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fvaibhavsingh97%2Fserverless-chatbot-demo.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fvaibhavsingh97%2Fserverless-chatbot-demo?ref=badge_shield)

This is a demo serverless bot which gives excuses.

## Demo

Try the bot here :robot: : [t.me/serverlessdemo_bot](https://t.me/serverlessdemo_bot)

## Prerequisites

1. Node.js v6.5.0 or later.
2. Serverless CLI v1.9.0 or later. You can run `npm install -g serverless` to install it.
3. An AWS account. If you don't already have one, you can sign up for a free trial that includes 1 million free Lambda requests per month.
4. [Set-up your Provider Credentials.](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

## Run

1. Clone the repository by using this link :

```bash
$ git clone https://github.com/vaibhavsingh97/serverless-chatbot-demo
```

2. Go to `serverless-chatbot-demo/`

```bash
$ cd serverless-chatbot-demo/
```

3. Get a bot from Telegram, sending this message to @BotFather

```bash
$ /newbot
```

4. Put the token received into a file called serverless.env.yml, like this

```bash
$ cat secrets.env.yml
TELEGRAM_TOKEN: <your_token>
```

5. Deploy it

```bash
$ serverless deploy
```

6. With the URL returned in the output, configure the Webhook

```bash
$ curl -X POST https://<your_url>.amazonaws.com/dev/set_webhook
```

7. With the URL returned in the output, check the Webhook is successfully set or not

```bash
$ curl -X POST https://<your_url>.amazonaws.com/dev/get_webhook_info
```

It should output the above URL returned in the output

Now, you can ask bot to get new excuses :wink:


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fvaibhavsingh97%2Fserverless-chatbot-demo.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fvaibhavsingh97%2Fserverless-chatbot-demo?ref=badge_large)