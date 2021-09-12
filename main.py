from sanic import Sanic
from sanic.response import *
import bot

app = Sanic(__name__)

app.static('/static', './static')

if __name__ == "__main__":
  bot.start()
  app.run(host="0.0.0.0", port=8000)
