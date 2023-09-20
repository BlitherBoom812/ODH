import http.server
import socketserver
import json


# 设置服务器的 IP 地址和端口
host = "localhost"
port = 8765

# 创建一个简单的请求处理程序
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # 检查请求路径是否为 /
        if self.path == "/":
            # 获取请求的内容长度
            content_length = int(self.headers['Content-Length'])
            # 读取请求的数据
            post_data = self.rfile.read(content_length)
            # 将请求数据解码为字符串
            post_data_str = post_data.decode('utf-8')
            # 解析请求数据为 JSON 对象
            post_data_json = json.loads(post_data_str)
            print(post_data_json)
            try:
                message = {'hello' : 'python server'}
                self.send_response(200)
            except BaseException as e:
                print(e)
                message = {'error' : 'invalid json'}
                self.send_response(400)
            # 设置响应的 Content-Type 为 application/json
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # 构建要返回的 JSON 响应
            response = message
            response_json = json.dumps(response)
            
            # 发送响应数据
            self.wfile.write(response_json.encode('utf-8'))
        else:
            self.send_error(404)
# 创建服务器对象，并指定请求处理程序
with socketserver.TCPServer((host, port), MyRequestHandler) as server:
    print(f"Server started at http://{host}:{port}")
    # 启动服务器，一直运行直到停止
    server.serve_forever()