from datetime import datetime

import pytest
from some_web_client import SomeResourceClient
import responses


@responses.activate
def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 1677842892,
        "timeDiff": 2165
    }
    responses.add(method=responses.GET, url="https://www.avito.ru/web/2/user/get-status/173e8385d5459f5eb8531bb3543081695e0d83e5a7f1e73b9a5b9c91511b5867",
                  json=valid_json_answer, status=200)
    some_resource_client = SomeResourceClient("https://www.avito.ru")
    res = some_resource_client.get_user_last_action_time("173e8385d5459f5eb8531bb3543081695e0d83e5a7f1e73b9a5b9c91511b5867")
    assert res == datetime.fromtimestamp(valid_json_answer["lastActionTime"] - valid_json_answer["timeDiff"])


@responses.activate
def test_some_web_client():
    valid_json_data_with_error = {
        "errors": [
            "Not found"
        ]
    }
    responses.add(method=responses.GET, url="https://www.avito.ru/web/2/user/get-status/173e8385d5459f5eb8531bb3543081695e0d83e5a7f1e73b9a5b9c91511b5867-",
                  json=valid_json_data_with_error, status=404)
    with pytest.raises(KeyError):
        some_resource_client = SomeResourceClient("https://www.avito.ru")
        some_resource_client.get_user_last_action_time("173e8385d5459f5eb8531bb3543081695e0d83e5a7f1e73b9a5b9c91511b5867-")


if __name__ == "__main__":
    some_resource_client = SomeResourceClient("https://www.avito.ru")
    res = some_resource_client.get_user_last_action_time("173e8385d5459f5eb8531bb3543081695e0d83e5a7f1e73b9a5b9c91511b5867")
    print(res)