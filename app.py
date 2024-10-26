import sys
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Define the HTTP server
def run_server(port=8000):
    handler = SimpleHTTPRequestHandler
    handler.directory = 'templates'  # Serve files from 'templates' directory
    server_address = ('', port)
    httpd = HTTPServer(server_address, handler)
    print(f"Serving on http://localhost:{port}")
    httpd.serve_forever()

# PyQt5 Web Browser
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Python Browser')
        self.setGeometry(300, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://localhost:8000'))  # URL points to the local HTTP server
        
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)

if __name__ == '__main__':
    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=run_server, args=(8000,))
    server_thread.daemon = True
    server_thread.start()

    # Start the PyQt app
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
