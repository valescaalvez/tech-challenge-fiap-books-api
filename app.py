import os
from api import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Porta dinâmica do Render
    app.run(host="0.0.0.0", port=port, debug=True)
