# Код был сформирован с использованием Swagger CodeGen

Данный модуль автоматически обновляется с получением измнений 
с официального сайта [wildberries](https://openapi.wildberries.ru/general/description/ru/) 

*Весь код был сформирован с использованием траслита на кривую латиницу*

Установка:

```python
pip install wildberries-api-client
```

Инструкция:

```python
from wildberries_api_client import content  # выберете свой раздел


conf = content.Configuration()
conf.host = 'https://advert-api.wb.ru'  # Ссылку можно найти в официальной документаци
conf.api_key['Authorization'] = ''  # Api token 
api_client = content.ApiClient(conf)

api_inst = content.ProsmotrApi(api_client)    # Наименования соответствуют подразделам
print(api_inst.content_v2_get_cards_list_post(body={"settings": 
                                                        {"cursor": 
                                                             {"limit": 1000},
                                                         "filter": {"withPhoto": -1}}
                                                    },
                                              locale='ru'))

```

Apache-2.0
Swagger