from flask import Flask
from birthday_wisher import runner
import asyncio
app = Flask(__name__)

@app.route("/run")
def hello_world():
    asyncio.run(runner())
    return "Running"


if __name__ == "__main__":
        app.run()
