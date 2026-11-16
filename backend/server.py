import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(FRONTEND_DIR), **kwargs)

    def _json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if urlparse(self.path).path.startswith("/api/"):
            return self._json(404, {"error": "не знайдено"})
        super().do_GET()

    def do_POST(self):
        if urlparse(self.path).path != "/api/user-point":
            return self._json(404, {"error": "не знайдено"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 4096:
                raise ValueError("некоректний розмір запиту")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            coords = payload.get("user_point")
            if not isinstance(coords, list) or len(coords) != 2:
                raise ValueError("очікувався список [latitude, longitude]")
            lat, lon = float(coords[0]), float(coords[1])
        except (ValueError, TypeError, UnicodeDecodeError) as err:
            return self._json(400, {"error": str(err)})

        # Заглушка відповіді (без logic.py та store.py)
        stub_result = {
            "title": "Тестова подія (заглушка)",
            "date": "1920-01-01",
            "description": f"Клік у точці: {lat:.5f}, {lon:.5f}",
            "period": 1,
            "period_name": "Тестовий період"
        }
        self._json(200, {"result": stub_result})


def main():
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"[Заглушка] Сторінка та API: http://127.0.0.1:{port}  (Ctrl+C — зупинити)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nЗупинено.")


if __name__ == "__main__":
    main()
