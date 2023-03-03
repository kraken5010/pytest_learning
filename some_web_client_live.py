import json
from datetime import datetime

import requests


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f"{self.url}/web/2/user/get-status/{user_id}")
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        json_data = self.__user_get_status(user_id)
        last_action_time = json_data["lastActionTime"]
        time_diff = json_data["timeDiff"]
        return datetime.fromtimestamp(last_action_time - time_diff)


some_resource_client = SomeResourceClient("https://www.avito.ru")
res = some_resource_client.get_user_last_action_time("173e8385d5459f5eb8531bb3543081695e0d83e5a7f1e73b9a5b9c91511b5867")
print(res)

# res = requests.get("https://www.avito.ru/web/2/user/get-status/173e8385d5459f5eb8531bb3543081695e0d83e5a7f1e73b9a5b9c91511b5867")
# print(res.text)