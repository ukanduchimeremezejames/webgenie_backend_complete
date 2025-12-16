git clone https://github.com/ukanduchimeremezejames/webgenie_backend_complete
cd webgenie_backend
python -m venv venv
source venv/bin/activate
venv\Scripts\activate (CMD) or
venv\Scripts\Activate.ps1 (Powershell) or
source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload

Ctrl + C (CMD & Powershell)
deactivate (Linux/macOS [when done])
