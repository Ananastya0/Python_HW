import requests


class YouGile:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def auth_token(self, login = '', password = ''):
        creds = {
            'login': login,
            'password': password
        }
        resp = requests.post(self.base_url, json=creds)
        return resp.json()

    def create_project(self, title):
        body = {
            'title': title
        }
        resp = requests.post(self.base_url, json=body, headers = self.headers)
        return resp.json()
    
    def update_project(self, project_id, title_new):
        body = {
            'title': title_new
        }
        resp = requests.put(f"{self.base_url}/{project_id}", json=body, headers = self.headers)
        return resp.json()
    
    def get_project(self, project_id):
        resp = requests.get(f"{self.base_url}/{project_id}", headers = self.headers)
        return resp.json()

    def create_project_without_title(self):
        body = {}
        resp = requests.post(self.base_url, json=body, headers = self.headers)
        return resp
    
    def get_project_by_invalid_id(self, project_id):
        resp = requests.get(f"{self.base_url}/{project_id}", headers = self.headers)
        return resp
    
    def change__invalid_project(self, project_id, new_title_new):
        body = {
            'title': new_title_new
        }
        resp = requests.put(f"{self.base_url}/{project_id}", json=body, headers = self.headers)
        return resp
