from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Обработка favicon.ico
        if self.path == '/favicon.ico':
            self.send_response(204)  # No Content
            self.end_headers()
            return
            
        # Главная страница
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
            return
                
        # Для всех остальных путей
        self.send_error(404, "Not found")

    def do_POST(self):
        # Обработка отправки формы
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(post_data)
            
            # Проверка наличия данных
            if 'name' not in data or 'email' not in data:
                self.send_error(400, "Missing form data")
                return
                
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            response = f"Привет, {data['name'][0]}! Твой email: {data['email'][0]}"
            
            # Чтение и обновление HTML
            with open('index.html', 'r', encoding='utf-8') as file:
                content = file.read()
                # Исправленный вызов replace
                updated_content = content.replace(
                    '<p id="result-text"></p>',
                    f'<p id="result-text">{response}</p>'
                )
                self.wfile.write(updated_content.encode('utf-8'))
        else:
            self.send_error(404, "Not found")

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()