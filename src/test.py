from wcferry import Wcf
import queue

wcf = Wcf()
wcf.enable_receiving_msg()

while True:
    try:
        msg = wcf.get_msg()
    except queue.Empty:
        continue
    print(msg.sender, msg.content)
