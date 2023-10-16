# region template: koito.jsonapi
import http.server
import json
import traceback


class JsonApiHandler(http.server.BaseHTTPRequestHandler):
    repsonse_headers = list()

    def get_json_payload(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        return json.loads(body.decode("utf-8"))

    def send_json_response(self, data):
        for k, v in self.repsonse_headers:
            self.send_header(k, v)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def get_method(self, method):
        name = method + "".join(x for x in self.path.replace("/", "_") if x.isalnum() or x == "_")
        print(f"{method} {self.path} -> {name}")
        return getattr(self, name, None)

    def do_GET(self):
        handler = self.get_method("get")
        if handler:
            try:
                result = handler()
            except:
                traceback.print_exc()
                self.send_response(500)
                self.send_json_response({"error": "internal error", "data": None})
            else:
                self.send_response(200)
                self.send_json_response({"error": "ok", "data": result})
        else:
            self.send_response(404)
            self.send_json_response({"error": "not found", "data": None})

    def do_POST(self):
        handler = self.get_method("post")
        if handler:
            try:
                params = self.get_json_payload()
            except:
                self.send_response(400)
                self.send_json_response({"error": "invalid json", "data": None})
            else:
                try:
                    result = handler(params)
                except:
                    traceback.print_exc()
                    self.send_response(500)
                    self.send_json_response({"error": "internal error", "data": None})
                else:
                    self.send_response(200)
                    self.send_json_response({"error": "ok", "data": result})
        else:
            self.send_response(404)
            self.send_json_response({"error": "not found", "data": None})

    def cookie(self):
        cookie = self.headers.get("Cookie")
        if cookie:
            return dict(x.strip().split("=", maxsplit=1) for x in cookie.split(";"))
        else:
            return {}

    def add_header(self, key, value):
        self.repsonse_headers.append((key, value))


# endregion

from hashlib import sha1
from random import choices
from string import ascii_lowercase

# Filesystem

with open("flag.txt", "r") as fs:
    flag = fs.read().strip()


def readfile(path):
    with open(path, "rb") as f:
        return f.read()


files = {
    "/": ("index.html", "text/html"),
    "/image.jpg": ("image.jpg", "image/jpeg"),
    "/index.js": ("index.js", "text/javascript"),
    "/pow-worker.js": ("pow-worker.js", "text/javascript"),
}

# Proof of Work

pow_salt = None
pow_hash = None
pow_partial_salt = None


def refresh_pow():
    global pow_salt, pow_hash, pow_partial_salt
    pow_salt = "".join(choices(ascii_lowercase, k=8))
    pow_hash = sha1(pow_salt.encode()).hexdigest()
    pow_partial_salt = pow_salt[4:]


refresh_pow()

# Answer

center = [118.317702, 24.612586]

# Handler


class MyHandler(JsonApiHandler):
    def get_pow(self):
        return {"partial_salt": pow_partial_salt, "hash": pow_hash}

    def post_verify(self, data):
        if data["pow"] != pow_salt:
            return {"flag": "flag{bad_pow!}"}
        refresh_pow()

        form_complete = data["x"] and data["y"] and data["date"]
        if form_complete:
            if data["date"] == "20221227":
                d2 = (center[0] - data["x"]) ** 2 + (center[1] - data["y"]) ** 2
                if d2 < 1e-4:
                    return {"flag": flag}
                elif d2 < 1e-1:
                    return {"flag": "flag{try_again!}"}
                else:
                    return {"flag": "flag{are_you_sure?}"}
            else:
                return {"flag": "flag{wrong_date!}"}
        else:
            return {"flag": "flag{complete_your_form!}"}

    def do_GET(self):
        if self.path in files:
            self.send_response(200)
            self.send_header("Content-Type", files[self.path][1])
            self.send_header("Cache-Control", "max-age=3600")
            self.end_headers()
            self.wfile.write(readfile(files[self.path][0]))
        else:
            return super().do_GET()


if __name__ == "__main__":
    server = http.server.HTTPServer(("", 9999), MyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
