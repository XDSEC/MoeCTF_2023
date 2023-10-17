import socketserver
from chall import chall

class Task(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.request.settimeout(60)
        
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg: str, newline=True):
        try:
            msg = msg.encode()
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        line = self._recvall().decode()
        if len(line) == 0:
            raise KeyboardInterrupt
        return line

    def handle(self):
        try:
            chall(self.recv,self.send)
        except KeyboardInterrupt:
            pass


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.timeout = 60


if __name__ == "__main__":
    try:
        HOST, PORT = '0.0.0.0', 9999
        print("HOST:POST " + HOST+":" + str(PORT))
        server = ForkedServer((HOST, PORT), Task)
        server.allow_reuse_address = True
        server.serve_forever()
    except KeyboardInterrupt:
        pass
