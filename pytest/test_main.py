from fatapi.testclient import TestClient
from .main import app,todos

client = TestClient(app)

def setup_function():
    todos.clear()   

def test_create_todo():
    response = client.get("/")