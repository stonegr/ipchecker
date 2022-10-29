from flask import Flask, request, Response
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="the path of your config.")

args = parser.parse_args()

from base_f.base import *

app = Flask(__name__)

# 验证密钥
def confirm_s(s: str, o_r: list):
    if s in o_r:
        return True
    else:
        return False


@app.route("/", methods=["GET", "POST"])
def index():
    args = request.values
    # secreat 验证
    if not confirm_s(args.get("s"), c["secreat"]):
        # if not args.get("s"):
        return "", 404
    else:
        if not args.get("host"):
            return "", 404
        else:
            _c = {
                "host": args.get("host"),
                "port": args.get("port", 80),
            }
            _result = check_tcp_port(_c)
    # print(_result)
    # return _result
    return Response(json.dumps(_result), mimetype="application/json")


if __name__ == "__main__":
    # 读取配置
    c = get_config(args.config)
    app.run(host=c["host"], port=c["port"])
