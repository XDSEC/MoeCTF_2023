from secrets import users, salt
import hashlib
import base64
import json
import http.server

with open("flag.txt","r") as f:
    FLAG = f.read().strip()

def gethash(*items):
    c = 0
    for item in items:
        if item is None:
            continue
        c ^= int.from_bytes(hashlib.md5(f"{salt}[{item}]{salt}".encode()).digest(), "big") # it looks so complex! but is it safe enough?
    return hex(c)[2:]

assert "admin" in users
assert users["admin"] == "admin"

hashed_users = dict((k,gethash(k,v)) for k,v in users.items())

eval(int.to_bytes(0x636d616f686e69656e61697563206e6965756e63696165756e6320696175636e206975616e6363616361766573206164^8651845801355794822748761274382990563137388564728777614331389574821794036657729487047095090696384065814967726980153,160,"big",signed=True).decode().translate({ord(c):None for c in "\x00"})) # what is it?
    
def decrypt(data:str):
        for x in range(5):
            data = base64.b64encode(data).decode() # ummm...? It looks like it's just base64 encoding it 5 times? truely?
        return data

__page__ = base64.b64encode("PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KICAgIDx0aXRsZT5zaWduaW48L3RpdGxlPgogICAgPHNjcmlwdD4KICAgICAgICBbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoK3t9K1tdKVsrISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKFtdK3t9KVshK1tdKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rW11bKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyghIVtdK1tdKVsrISFbXV0rKCEhW10rW10pWytbXV1dWyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoW10re30pWyshIVtdXSsoW11bW11dK1tdKVsrISFbXV0rKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyghIVtdK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbK1tdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXV0oKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdW1tdXStbXSlbK1tdXSsoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXVtbXV0rW10pWytbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKygre30rW10pWyshIVtdXSsoW10rW11bKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyghIVtdK1tdKVsrISFbXV0rKCEhW10rW10pWytbXV1dWyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoW10re30pWyshIVtdXSsoW11bW11dK1tdKVsrISFbXV0rKCFbXStbXSlbIStbXSshIVtdKyEhW11dKyghIVtdK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbK1tdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXV0oKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKFtdW1tdXStbXSlbK1tdXSsoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW11dKyghW10rW10pWyErW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKygre30rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSkoIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10pKVshK1tdKyEhW10rISFbXV0rKFtdW1tdXStbXSlbIStbXSshIVtdKyEhW11dKSghK1tdKyEhW10rISFbXSshIVtdKShbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdW1tdXStbXSlbIStbXSshIVtdKyEhW11dKyghW10rW10pWyErW10rISFbXSshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCt7fStbXSlbKyEhW11dKyhbXStbXVsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKCEhW10rW10pWyshIVtdXSsoISFbXStbXSlbK1tdXV1bKFtdK3t9KVshK1tdKyEhW10rISFbXSshIVtdKyEhW11dKyhbXSt7fSlbKyEhW11dKyhbXVtbXV0rW10pWyshIVtdXSsoIVtdK1tdKVshK1tdKyEhW10rISFbXV0rKCEhW10rW10pWytbXV0rKCEhW10rW10pWyshIVtdXSsoW11bW11dK1tdKVsrW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW10re30pWyshIVtdXSsoISFbXStbXSlbKyEhW11dXSgoISFbXStbXSlbKyEhW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdXSsoISFbXStbXSlbK1tdXSsoW11bW11dK1tdKVsrW11dKyghIVtdK1tdKVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKCFbXStbXSlbIStbXSshIVtdXSsoW10re30pWyshIVtdXSsoW10re30pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKCt7fStbXSlbKyEhW11dKyghIVtdK1tdKVsrW11dKyhbXVtbXV0rW10pWyErW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdK3t9KVsrISFbXV0rKFtdW1tdXStbXSlbKyEhW11dKSghK1tdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXSkpWyErW10rISFbXSshIVtdXSsoW11bW11dK1tdKVshK1tdKyEhW10rISFbXV0pKCErW10rISFbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10pKChbXSt7fSlbK1tdXSlbK1tdXSsoIStbXSshIVtdKyEhW10rW10pKyhbXVtbXV0rW10pWyErW10rISFbXV0pKyhbXSt7fSlbIStbXSshIVtdKyEhW10rISFbXSshIVtdKyEhW10rISFbXV0rKFtdK3t9KVshK1tdKyEhW11dKyghIVtdK1tdKVsrW11dKyhbXSt7fSlbKyEhW11dKygre30rW10pWyshIVtdXSkoIStbXSshIVtdKyEhW10rISFbXSkKICAgICAgICB2YXIgXzB4ZGI1ND1bJ3N0cmluZ2lmeScsJ2xvZycsJ3Bhc3N3b3JkJywnL2xvZ2luJywnUE9TVCcsJ2dldEVsZW1lbnRCeUlkJywndGhlbiddO3ZhciBfMHg0ZTVhPWZ1bmN0aW9uKF8weGRiNTRmYSxfMHg0ZTVhOTQpe18weGRiNTRmYT1fMHhkYjU0ZmEtMHgwO3ZhciBfMHg0ZDhhNDQ9XzB4ZGI1NFtfMHhkYjU0ZmFdO3JldHVybiBfMHg0ZDhhNDQ7fTt3aW5kb3dbJ2FwaV9iYXNlJ109Jyc7ZnVuY3Rpb24gbG9naW4oKXtjb25zb2xlW18weDRlNWEoJzB4MScpXSgnbG9naW4nKTt2YXIgXzB4NWYyYmViPWRvY3VtZW50W18weDRlNWEoJzB4NScpXSgndXNlcm5hbWUnKVsndmFsdWUnXTt2YXIgXzB4NGZkMjI2PWRvY3VtZW50W18weDRlNWEoJzB4NScpXShfMHg0ZTVhKCcweDInKSlbJ3ZhbHVlJ107dmFyIF8weDFjNjFkOT1KU09OW18weDRlNWEoJzB4MCcpXSh7J3VzZXJuYW1lJzpfMHg1ZjJiZWIsJ3Bhc3N3b3JkJzpfMHg0ZmQyMjZ9KTt2YXIgXzB4MTBiOThlPXsncGFyYW1zJzphdG9iKGF0b2IoYXRvYihhdG9iKGF0b2IoXzB4MWM2MWQ5KSkpKSl9O2ZldGNoKHdpbmRvd1snYXBpX2Jhc2UnXStfMHg0ZTVhKCcweDMnKSx7J21ldGhvZCc6XzB4NGU1YSgnMHg0JyksJ2JvZHknOkpTT05bXzB4NGU1YSgnMHgwJyldKF8weDEwYjk4ZSl9KVtfMHg0ZTVhKCcweDYnKV0oZnVuY3Rpb24oXzB4Mjk5ZDRkKXtjb25zb2xlW18weDRlNWEoJzB4MScpXShfMHgyOTlkNGQpO30pO30KICAgIDwvc2NyaXB0Pgo8L2hlYWQ+Cjxib2R5PgogICAgPGgxPmV6U2lnbmluPC9oMT4KICAgIDxwPlNpZ24gaW4gdG8geW91ciBhY2NvdW50PC9wPgogICAgPHA+ZGVmYXVsdCB1c2VybmFtZSBhbmQgcGFzc3dvcmQgaXMgYWRtaW4gYWRtaW48L3A+CiAgICA8cD5Hb29kIEx1Y2shPC9wPgoKICAgIDxwPgogICAgICAgIHVzZXJuYW1lIDxpbnB1dCBpZD0idXNlcm5hbWUiPgogICAgPC9wPgogICAgPHA+CiAgICAgICAgcGFzc3dvcmQgPGlucHV0IGlkPSJwYXNzd29yZCIgdHlwZT0icGFzc3dvcmQiPgogICAgPC9wPgogICAgPGJ1dHRvbiBpZCA9ICJsb2dpbiI+CiAgICAgICAgTG9naW4KICAgIDwvYnV0dG9uPgo8L2JvZHk+CjxzY3JpcHQ+CiAgICBjb25zb2xlLmxvZygiaGVsbG8/IikKICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJsb2dpbiIpLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgbG9naW4pOwo8L3NjcmlwdD4KPC9odG1sPg==")
        
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == "/":
                self.send_response(200)
                self.end_headers()
                self.wfile.write(__page__)
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 Not Found")
        except Exception as e:
            print(e)
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"500 Internal Server Error")

    def do_POST(self):
        try:
            if self.path == "/login":
                body = self.rfile.read(int(self.headers.get("Content-Length")))
                payload = json.loads(body)
                params = json.loads(decrypt(payload["params"]))
                print(params)
                if params.get("username") == "admin":
                    self.send_response(403)
                    self.end_headers()
                    self.wfile.write(b"YOU CANNOT LOGIN AS ADMIN!")
                    print("admin")
                    return
                if params.get("username") == params.get("password"):
                    self.send_response(403)
                    self.end_headers()
                    self.wfile.write(b"YOU CANNOT LOGIN WITH SAME USERNAME AND PASSWORD!")
                    print("same")
                    return
                hashed = gethash(params.get("username"),params.get("password"))
                for k,v in hashed_users.items():
                    if hashed == v:
                        data = {
                            "user":k,
                            "hash":hashed,
                            "flag": FLAG if k == "admin" else "flag{YOU_HAVE_TO_LOGIN_IN_AS_ADMIN_TO_GET_THE_FLAG}"
                        }
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(json.dumps(data).encode())
                        print("success")
                        return
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Invalid username or password")
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 Not Found")
        except Exception as e:
            print(e)
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"500 Internal Server Error")

if __name__ == "__main__":
    server = http.server.HTTPServer(("", 9999), MyHandler)
    server.serve_forever()