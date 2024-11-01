import os
from wcferry import Wcf
import queue
from robot import get_response

_SENDER = [
    "wxid_a1ud4j5yi1sb22",  # 老婆婆
    "yck13540292813",  # 自己
]
def main():
    os.path.exists("logs") or os.makedirs("logs")
    wcf = Wcf()
    wcf.enable_receiving_msg()

    while True:
        try:
            msg = wcf.get_msg()
        except queue.Empty:
            continue
        if msg.sender in _SENDER:
            print(msg.sender, msg.content)
            try:
                response = get_response(msg.content)
                print(response)
                wcf.send_text(response, msg.sender)
            except Exception as e:
                wcf.send_text("出错了，请稍后再试", msg.sender)


if __name__ == "__main__":
    main()
