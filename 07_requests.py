# %%
import requests
# %%
url = 'http://localhost:8000/'
response = requests.get(url)
# %%
response.text
# %%
response.json()
# %%
item_id = 1
response = requests.put(
    f'{url}items/{item_id}',
    json = {
        "name": "manzana",
        "price": 10,
        "is_offer": True
    }
)
# %%
response.text
# %%
response = requests.get(
    f'{url}items/{1}',
)
# %%
response.text
# %%
