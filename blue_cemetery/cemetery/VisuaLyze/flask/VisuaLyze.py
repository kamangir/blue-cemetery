from flask import Flask, request

from blueness import module

from blue_sandbox import env
from blue_sandbox import NAME, VERSION
from blue_sandbox.VisuaLyze.order import VisuaLyzeOrder
from blue_sandbox.logger import logger

NAME = module.name(__file__, NAME)

app = Flask(__name__)


@app.route("/")
def index():
    order = VisuaLyzeOrder(example_name="onlinefoods")
    return order.render()


@app.route("/VisuaLyze", methods=["POST"])
def process():
    order = VisuaLyzeOrder(
        prompt=request.form["prompt"].split("\n"),
        description=request.form["description"].split("\n"),
        data_filename=request.form["data_filename"],
        complete=True,
    )

    return order.render()


if __name__ == "__main__":
    logger.info(f"{NAME}.{VERSION} is running.")
    app.run(debug=True, port=env.VISUALYZE_PORT)
