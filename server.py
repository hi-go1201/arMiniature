#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import http.server as s
import json

class MyHandler(s.BaseHTTPRequestHandler):
    def do_POST(self):

        # リクエスト取得
        content_len  = int(self.headers.get("content-length"))
        body = json.loads(self.rfile.read(content_len).decode('utf-8'))

        # レスポンス処理
        #body["answer"] = "晴れです。"
        #self.send_response(200)
        self.send_response(200, "ok")
        self.send_header('Content-type', 'application/json;charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:8000')
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Headers', 'Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')
        self.end_headers()
        body_json = json.dumps(body, sort_keys=False, indent=4, ensure_ascii=False) 
        self.wfile.write(body_json.encode("utf-8"))
        print(body_json)

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

# サーバ起動
host = '0.0.0.0'
port = 3333
httpd = s.HTTPServer((host, port), MyHandler)
httpd.serve_forever()