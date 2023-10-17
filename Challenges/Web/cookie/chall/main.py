#region template: koito.jsonapi
import http.server
import json
import traceback

class JsonApiHandler(http.server.BaseHTTPRequestHandler):
    repsonse_headers = list()

    def get_json_payload(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body.decode('utf-8'))

    def send_json_response(self,data):
        for k,v in self.repsonse_headers:
            self.send_header(k,v)
        self.repsonse_headers.clear()
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def get_method(self,method):
        name = method + "".join(x for x in self.path.replace('/', '_') if x.isalnum() or x == '_')
        print(f"{method} {self.path} -> {name}")
        return getattr(self,name,None)

    def do_GET(self):
        handler = self.get_method('get')
        if handler:
            try:
                result = handler()
            except:
                traceback.print_exc()
                self.send_response(500)
                self.send_json_response({'error': 'internal error', 'data': None})
            else:
                self.send_response(200)
                self.send_json_response({'error':'ok','data':result})
        else:
            self.send_response(404)
            self.send_json_response({'error': 'not found', 'data': None})

    def do_POST(self):
        handler = self.get_method('post')
        if handler:
            try:
                params = self.get_json_payload()
            except:
                self.send_response(400)
                self.send_json_response({'error': 'invalid json', 'data': None})
            else:
                try:
                    result = handler(params)
                except:
                    traceback.print_exc()
                    self.send_response(500)
                    self.send_json_response({'error': 'internal error', 'data': None})
                else:
                    self.send_response(200)
                    self.send_json_response({'error':'ok','data': result})
        else:
            self.send_response(404)
            self.send_json_response({'error': 'not found', 'data': None})

    def cookie(self):
        cookie = self.headers.get('Cookie')
        if cookie:
            return dict(x.strip().split('=',maxsplit=1) for x in cookie.split(';'))
        else:
            return {}
        
    def add_header(self,key,value):
        self.repsonse_headers.append((key,value))

#endregion

import base64

with open('flag.txt') as fs:
    flag = fs.read().strip()

def encrypt(data):
    return base64.urlsafe_b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')

def decrypt(data):
    return json.loads(base64.urlsafe_b64decode(data.encode('utf-8')).decode('utf-8'))

users = {
    "koito":{
        "username":"koito",
        "password":"不是，有一说一，你真能猜到这个密码的话那确实nb",
        "role":"admin"
    },
}

class MyHandler(JsonApiHandler):
    def get_status(self):
        return {'status': 'everything is ok'}
    
    def get_flag(self):
        cookie = self.cookie()
        if "token" in cookie:
            token = cookie["token"]
            try:
                user = decrypt(token)
                if user["role"] == "admin":
                    return {'flag': flag}
                else:
                    return {'flag': 'flag{sorry_but_you_are_not_admin}'}
            except:
                return {'flag': 'flag{what_have_you_done, hacker!}'}
        else:
            return {'flag': 'flag{you_should_login_first_to_get_the_flag}'}

    def post_login(self,data):
        if "username" in data and "password" in data:
            username = data['username']
            password = data['password']
            if username in users:
                user = users[username]
                if user["password"] == password:
                    token = encrypt(user)
                    self.add_header('Set-Cookie', f"token={token};")
                    return {'status': 'ok'}
                else:
                    return {'status': 'wrong password'}
            else:
                return {'status': 'user not existed'}
        else:
            return {'status': 'error'}
        
    def post_register(self,data):
        if "username" in data and "password" in data:
            username = data['username']
            password = data['password']
            if username not in users:
                users[username] = {
                    "username":username,
                    "password":password,
                    "role":"user"
                }
                return {'status': 'ok'}
            else:
                return {'status': 'user existed'}
        else:
            return {'status': 'error'}

if __name__ == '__main__':
    server = http.server.HTTPServer(('', 9999), MyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()