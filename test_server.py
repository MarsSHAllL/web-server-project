import unittest
import sys
import os
from io import BytesIO
from unittest.mock import patch, MagicMock

# Добавляем папку с server.py в PATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from server import RequestHandler

class TestServer(unittest.TestCase):
    def setUp(self):
        patcher_setup  = patch.object(RequestHandler, 'setup',  lambda self: None)
        patcher_handle = patch.object(RequestHandler, 'handle', lambda self: None)
        patcher_finish = patch.object(RequestHandler, 'finish', lambda self: None)
        patcher_setup.start()
        patcher_handle.start()
        patcher_finish.start()

        # Инстанцируем RequestHandler
        # request=MagicMock() достаточно, потому что setup/handle/finish ничего не делают
        self.handler = RequestHandler(
            request=MagicMock(),
            client_address=('127.0.0.1', 8080),
            server=MagicMock()
        )

        # Инициализируем атрибуты для POST
        self.handler.request_version   = 'HTTP/1.1'
        self.handler.requestline       = 'POST /submit HTTP/1.1'
        self.handler.command           = 'POST'
        self.handler.path              = '/submit'
        self.handler.headers           = {}
        self.handler.wfile             = BytesIO()

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='''
        <html>
        <body>
            <form action="/submit" method="post">
            <input name="name">
            <input name="email">
            <button type="submit">Send</button>
            </form>
            <p id="result-text"></p>
        </body>
        </html>
        ''')
    def test_form_processing(self, mock_file):
        # Подготовка POST-данных
        post_data = 'name=Alex&email=Alex@yandex.ru'
        self.handler.headers['Content-Length'] = str(len(post_data))
        self.handler.rfile = BytesIO(post_data.encode('utf-8'))

        # Заглушаем методы отправки заголовков и читаем результат
        with patch.object(self.handler, 'send_response') as mock_send_response, \
             patch.object(self.handler, 'send_header')   as mock_send_header, \
             patch.object(self.handler, 'end_headers')   as mock_end_headers:

            # Вызываем метод
            self.handler.do_POST()

            output = self.handler.wfile.getvalue().decode('utf-8')

            # Проверяем содержимое
            self.assertIn("Привет, Alex!", output)
            self.assertIn("Alex@yandex.ru", output)

            # И проверяем, что правильно ушли заголовки
            mock_send_response.assert_called_once_with(200)
            mock_send_header.assert_called_with('Content-type', 'text/html; charset=utf-8')
            mock_end_headers.assert_called_once()

if __name__ == '__main__':
    unittest.main()