# %%
import requests
import pprint
# %%
url = 'http://localhost:8000/'
response = requests.get(url)
# %%
print(response.text)
# %%
pprint.pprint(response.json())
# %% ---------------------------------------------------------------------
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
print(response.text)
# %% ---------------------------------------------------------------------
response = requests.get(
    f'{url}items/{1}',
)
# %%
print(response.text)
# %%
