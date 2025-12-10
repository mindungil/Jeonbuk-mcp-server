from requests import post
from json import dumps
from io import BytesIO

def upload_file(url: str, token: str, file_data: BytesIO, filename:str, file_type:str) -> dict:
    """ 
    Upload a file to the specified URL with the provided token.
    Args:
        url (str): The URL to which the file will be uploaded.
        token (str): The authorization token for the request.
        file_data (BytesIO):  with .name attribute set to the full filename.
        filename (str): The desired filename for the uploaded file (without extension).
        file_type (str): The file extension/type (e.g., 'pptx', 'xlsx', 'docx', 'md').
    Returns:
        dict: Contains 'file_path_download' with a markdown hyperlink for downloading the uploaded file.
              Format: "[Download {filename}.{file_type}](/api/v1/files/{id}/content)"
              On error: {"error": {"message": "error description"}}
    """
    # MIME type mapping
    mime_types = {
        'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'md': 'text/markdown'
    }
    
    mime_type = mime_types.get(file_type, 'application/octet-stream')
    
    # Ensure the URL ends with '/api/v1/files/'
    url = f'{url}/api/v1/files/'

    # Prepare headers and files for the request
    headers = {
        'Authorization': token,
        'Accept': 'application/json'
    }
 
    # Handle file_like: assume it's a file-like object (e.g., BytesIO) with .name attribute set
    files = {'file': (f"{filename}.{file_type}", file_data, mime_type)}

    response = post(url, headers=headers, files=files)


    if response.status_code != 200:
       return {"error": {"message": f'Error uploading file: {response.status_code}, {response.text}'}}, response
    elif response.status_code == 200:
        return {
            "file_path_download": f"[Download {filename}.{file_type}](/api/v1/files/{response.json()['id']}/content)"
        }, response.json()