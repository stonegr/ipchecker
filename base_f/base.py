import socket
import json


def check_tcp_port(kw, timeout=1):
    try:
        # socket.AF_INET 服务器之间网络通信
        # socket.SOCK_STREAM  流式socket , 当使用TCP时选择此参数
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (str(kw["host"]), int(kw["port"]))
        cs.settimeout(timeout)
        # s.connect_ex(adddress)功能与connect(address)相同，但是成功返回0，失败返回error的值。
        status = cs.connect_ex(address)
    except Exception as e:
        return {
            "status": 1,
            "message": "Connection %s:%s failed" % (kw["host"], kw["port"]),
            "info": "tcp check",
        }
    else:
        if status != 0:
            return {
                "status": 1,
                "message": "Connection %s:%s failed" % (kw["host"], kw["port"]),
                "info": "tcp check",
            }
        else:
            return {
                "status": 0,
                "message": "Connection %s:%s success" % (kw["host"], kw["port"]),
                "info": "tcp check",
            }


# 获取配置文件
def get_config(path: str):
    with open(path, "r", encoding="utf-8") as f:
        _c = json.loads(f.read())
        f.close()
    return _c


if __name__ == "__main__":
    print(check_tcp_port({"host": "114.114.114.114", "port": "53"}))
