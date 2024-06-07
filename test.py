from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

# test for create book C
def test_create_book():
	response = client.post("/books", json={"title": "School Of Money", "author": "Dr. Olumide Emmanuel", "published_year": 2007})
	assert response.status_code == 200
	assert response.json()["title"] == "School Of Money"

# test for getting all books
def test_get_books():
	response = client.get("/books")
	assert response.status_code == 200
	assert isinstance(response.json(), list)

# test for getting just a single book
def test_get_book():
	response = client.post("/books", json={"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "published_year": 2007})
	book_id = response.json()['id']
	response = client.get(f"/books/{book_id}")
	assert response.status_code == 200
	assert response.json()["author"] == "Robert Kiyosaki"


# test for updating books U
def test_update_book():
	response = client.post("/books", json={"title": "Battle Cry", "author": "TD jakes", "published_year": 2007})
	book_id = response.json()['id']
	response = client.put(f"/books/{book_id}", json={"title": "Battle Cry", "author": "Dr. D.K Olukoya", "published_year": 2007})
	assert response.status_code == 200
	assert response.json()["author"] == "Dr. D.K Olukoya"


def test_delete_book():
	response = client.post("/books", json={"title": "Why we want you to be rich", "author": "Donal and Robert", "published_year": 2010})
	book_id = response.json()['id']
	response = client.delete(f"/books/{book_id}")
	assert response.status_code == 204 # because there is no content it will return 204 instead of 200
	response = client.get(f"/books/{book_id}")
	assert response.status_code == 404

