from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_root():
    res = client.get("/")
 
    assert res.json().get('status')=="up"
    assert res.status_code==200

def test_create_user():
    res = client.post("/users/", json={"email": "abc@gmail.com", "password":"pswd"})

    print("=========",res.json())
    assert res.status_code==201