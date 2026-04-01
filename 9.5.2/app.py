
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html_content = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Привет из Docker</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    background-color: #f0f8ff;
                    text-align: center;
                }
                img {
                    max-width: 300px;
                    height: auto;
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <h1>Задание 9.5.2</h1>
            <img src="https://i.pinimg.com/originals/2b/b9/91/2bb9914c137fc0a435d71ef5e804016a.png">
            <p>В задании не указано что именно должно быть в образе, поэтому держите котика..</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8080) 
    httpd = server_class(server_address, handler_class)
    print("Запуск сервера на порту 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

