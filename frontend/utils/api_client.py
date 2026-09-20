import requests

BASE_URL = "http://127.0.0.1:8000"


class APIClient:

    def health(self):

        return requests.get(
            f"{BASE_URL}/health"
        ).json()

    def chat(self, question):

        response = requests.post(
            f"{BASE_URL}/chat",
            json={
                "question": question
            }
        )

        return response.json()

    def stream_chat(self, question):

        response = requests.post(
            f"{BASE_URL}/stream-chat",
            json={
                "question": question
            },
            stream=True
        )

        for chunk in response.iter_content(
            chunk_size=16,
            decode_unicode=True
        ):

            if chunk:
                yield chunk

    def search(self, query):

        response = requests.post(
            f"{BASE_URL}/search",
            json={
                "query": query
            }
        )

        return response.json()

    def documents(self):

        return requests.get(
            f"{BASE_URL}/documents"
        ).json()

    def index_document(self, filename):

        return requests.post(
            f"{BASE_URL}/index",
            json={
                "filename": filename
            }
        ).json()


api = APIClient()