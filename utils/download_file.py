from requests import get
from io import BytesIO

def download_file(url: str, token: str, file_id: str) -> BytesIO:
    """
    Download a file from the specified URL with the provided token and file ID.
    Args:
        url (str): The base URL from which the file will be downloaded.
        token (str): The authorization token for the request.
        file_id (str): The ID of the file to be downloaded.
    """
    # Ensure the URL ends with '/api/v1/files/'
    url = f'{url}/api/v1/files/{file_id}/content'

    # Prepare headers and files for the request
    headers = {
        'Authorization': token,
        'Accept': 'application/json'
    }
    # Send the GET request
    response = get(url, headers=headers)

    if response.status_code != 200:
       return {"error":{"message": f'Error downloading the file: {response.status_code}'}}
    else:
        return BytesIO(response._content)