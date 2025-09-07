from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_text():
    res = client.post('/api/v1/query', json={'text': 'test', 'language': 'en'})
    assert res.status_code == 200
    data = res.json()
    assert 'answer_en' in data
    assert data['answer_en'].startswith('Stub')


def test_image_diagnosis():
    files = {'image': ('leaf.jpg', b'binarydata', 'image/jpeg')}
    res = client.post('/api/v1/image-diagnosis', files=files)
    assert res.status_code == 200
    data = res.json()
    assert data['label'] in ['healthy', 'disease']
