import re
import socketserver

class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg:str, newline=True):
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
        flag = "moectf{this_is_not_the_real_flag_and_the_real_one_is_'flag.txt'}"
        pattern = re.compile(r"(?:read)|(?:pattern)|(?:write)|(?:dir)|(?:vars)|(?:locals)|(?:globals)|(?:attr)|(?:sys)|(?:import)|(?:eval)|(?:exec)|(?:input)|(?:os)|(?:help)|(?:breakpoint)|(?:[\.\\_=])|[^\x00-\xff]")
        while True:
            try:
                s = self.recv(">> ")
                if len(s) > 35 or pattern.search(s):
                    self.send("<< [ === ACCESS DENIED === ]")
                    continue
                self.send(f"<< {eval(s)}")
            except KeyboardInterrupt:
                break
            except:
                self.send("<< [ === !!!ERROR!!! === ]")

    
class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    try:
        HOST, PORT = '0.0.0.0', 9999
        print("HOST:POST " + HOST+":" + str(PORT))
        server = ForkedServer((HOST, PORT), Task)
        server.allow_reuse_address = True
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        pass
