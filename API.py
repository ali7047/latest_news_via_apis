import requests
from datetime import datetime, timedelta
from send_email import send_email


def headlines(query):
# "https://newsapi.org/v2/everything?q=tesla&from=2025-02-09&sortBy=publishedAt&"
       yesterday_date = datetime.now() - timedelta(days=1)
       yesterday_date = yesterday_date.strftime('%Y-%m-%d')

       get_api = (f"https://newsapi.org/v2/everything?"
                  f"q={query}&from={yesterday_date}&sortBy=publishedAt&"
                  f"apiKey=51c09eb062c24b8f8227225fddc0768e&"
                  f"language=en")

       api_call = requests.get(get_api)

       count, news_headlines = 0, ""
       for article in api_call.json()["articles"][:20]:
              count += 1
              title = article["title"].title()
              description = article["description"] if article["description"] else ""
              link = article["url"]
              result = f"{count}-> {title}:\n{description}\n{link}"
              news_headlines = news_headlines + result +"\n\n"

       return news_headlines


if __name__ == "__main__":
       news = headlines("tesla")
       send_email(news)

