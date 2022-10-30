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
            if is_ip(args.get("host")):
                _c = {
                    "host": args.get("host"),
                    "port": args.get("port", 80),
                }
            else:
                _host = getIP(args.get("host"))
                if is_ip(_host):
                    _c = {
                        "host": _host,
                        "port": args.get("port", 80),
                    }
                else:
                    return "", 404

            _result = check_tcp_port(_c)
    # print(_result)
    # return _result
    return Response(json.dumps(_result), mimetype="application/json")


if __name__ == "__main__":
    if not args.config:
        parser.print_help()
    else:
        # 读取配置
        c = get_config(args.config)
        app.run(host=c["host"], port=c["port"])
