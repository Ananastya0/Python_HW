import requests
import pytest
from YouGile import YouGile


base_url = 'https://ru.yougile.com/api-v2/projects'
headers = {'Authorization': 'Bearer PUZlZz-1q+H77CTcAr3P158c1q1G1FwS3r99VDR5FriX4PszxxXLgj5E+8uhGgVr'}

# создать проект
def test_create_project():
    api_client = YouGile (base_url, headers)
    global project_id
    resp = api_client.create_project('Test_Project')
    assert 'id' in resp, 'Проект не создался, id отсутствует'
    project_id = resp['id']

# изменить название
def test_update_project():
    api_client = YouGile (base_url, headers)
    resp_new = api_client.update_project(project_id, 'Project_New')
    assert 'id' in resp_new, 'Проект не создался, id отсутствует'

# получить id компании
def test_get_project():
    api_client = YouGile(base_url, headers)
    resp = api_client.get_project(project_id)
    assert 'id' in resp and resp['id'] == project_id, 'Ошибка: ID проекта не совпадает'
    assert 'title' in resp, 'Ошибка: в ответе нет названия проекта'

#негативные:

# создать проект без названия
def test_create_project_without_title():
    api_client = YouGile(base_url, headers)
    resp = api_client.create_project_without_title()
    assert resp.status_code == 400


# получить проект по неверному ID
def test_get_project_by_invalid_id():
    api_client = YouGile(base_url, headers)
    resp = api_client.get_project_by_invalid_id(project_id + '08')
    assert resp.status_code == 404


# изменить проект с неверными данными
def test_change__invalid_project():
    api_client = YouGile(base_url, headers)
    resp = api_client.change__invalid_project(project_id + '08', 'Проект с изменениями')
    assert resp.status_code == 404
