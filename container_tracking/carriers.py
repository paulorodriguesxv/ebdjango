import json
import requests
import logging

logger = logging.getLogger(__name__)


def _get_carrier(container_number):
    return container_number[:4].upper()


def is_valid_carrier(container_number):
    carries_extrators = ["CCLU", "CBHU", "CSLU", "CSNU"]
    return _get_carrier(container_number) in carries_extrators


def _parser_content(content):
    status = content['containerNumberStatus']
    location = content['location']
    date = content['timeOfIssue']
    carrier = "Cosco Shipping"
    return dict(date=date, status=status, location=location, carrier=carrier)


def _execute(url, container_id):
    _url = url.format(container_id=container_id)

    response = requests.get(_url)
    response_text = response.json()

    try:
        data = (response_text['data']['content']['containers'][0]
                ["containerCircleStatus"][0])

        data = _parser_content(data)
        return data
    except IndexError:
        logger.info(f"Container not found {container_id}")

    return None


def is_valid_carrier(container_number):
    carries_extrators = ("CCLU", "CBHU", "CSLU", "CSNU")
    return _get_carrier(container_number) in carries_extrators


def request_container_info(container_number):
    url = 'http://elines.coscoshipping.com/ebtracking/public/containers/{container_id}?timestamp=1559757057924'

    if not is_valid_carrier(container_number):
        return None

    return _execute(url, container_number)


if __name__ == "__main__":
    data = request_container_info("CCLU4522432")
    print(data)

    data = request_container_info("CSNU6719769")
    print(data)
