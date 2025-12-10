from requests import post, get
from json import dumps
import logging
logging.basicConfig(level=logging.INFO, force=True)
logger = logging.getLogger("GenFilesMCP")

def check_knowledge_exists(url: str, token: str) -> dict:
    """
    Check if knowledge items exist at the specified URL with the provided token.
    
    Args:
        url (str): The base URL to check for knowledge items.
        token (str): The authorization token for the request.
    Returns:
        dict: A dictionary mapping knowledge item names to their IDs.
    """

    # Ensure the URL ends with '/api/v1/knowledge/list'
    endpoint = f'{url}/api/v1/knowledge/list'

    # Prepare headers for the request
    headers = {
        'Authorization': token,
        'Accept': 'application/json'
    }

    # Make the GET request to fetch the knowledge list
    response = get(endpoint, headers=headers)
    
    if response.status_code != 200:
        return dumps({"error":{"message": f'Error creating knowledge'}})
    elif response.status_code == 200:
        # Parse the JSON response to get the list of knowledge items
        knowledge_list = response.json()
        knowledge_dict = {f"{k['name']}_{k['user_id']}":{'knowledge_id': k['id'], 'user_id': k['user_id']} for k in knowledge_list}
        logger.info(f"Knowledge items fetched successfully:  {knowledge_dict}")
        return knowledge_dict
    
def add_file_to_knowledge(url: str, token: str, knowledge_id: str, file_id: str) -> bool:
    """
    Add a file to a specified knowledge item.
    Args:
        url (str): The base URL to add the file to the knowledge item.
        token (str): The authorization token for the request.
        knowledge_id (str): The ID of the knowledge item.
        file_id (str): The ID of the file to be added.
    Returns:
        bool: True if the file was added successfully, False otherwise.
    """

    # Add a file to a specified knowledge item.
    url = f'{url}/api/v1/knowledge/{knowledge_id}/file/add'

    # Prepare headers and data for the request
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    # Prepare payload for the request
    data = {'file_id': file_id}

    # Make the POST request to add the file to the knowledge item
    response = post(url, headers=headers, json=data)

    # Return True if the file was added successfully, else False
    if response.status_code == 200:
        logger.info("File added to knowledge base successfully.")
        return True
    else:
        logger.error(f"Error adding file to knowledge base")
        return False
    
def create_knowledge(url: str, token: str, file_id: str, user_id: str, knowledge_name: str = 'My Generated Files') -> bool:
    """
    Create a new knowledge item if it does not already exist.

    Args:
        url (str): The base URL to create the knowledge item.
        token (str): The authorization token for the request.
        file_id (str): The ID of the file to be added to the knowledge item.
        user_id (str): The ID of the user creating the knowledge item.
        knowledge_name (str): The name of the knowledge item to be created.
    
    Returns:
        bool: True if the knowledge item was created, False otherwise.
    """
    # Check if the knowledge item already exists
    knowledge_dicts = check_knowledge_exists(url, token)
    
    if not isinstance(knowledge_dicts, dict):
        logger.error("Failed to check knowledge exists")
        return False
    
    # If it exists, do nothing; otherwise, create it
    if f'{knowledge_name}_{user_id}' in knowledge_dicts.keys() and knowledge_dicts[f'{knowledge_name}_{user_id}']['user_id'] == user_id:

        # # get the knowledge id of the correct user 
        # objective_knowledge_id = '00000000-0000-0000-0000-000000000000'

        # # Find the knowledge ID for the specified user
        # for k, v in knowledge_dicts.items():
        #     if k == knowledge_name and v['user_id'] == user_id:
        #         objective_knowledge_id = v['knowledge_id']

        # Add the uploaded file to the knowledge base
        add_file_state = add_file_to_knowledge(
            url=url, 
            token=token, 
            knowledge_id=knowledge_dicts[f'{knowledge_name}_{user_id}']['knowledge_id'], 
            file_id=file_id
        )
        logger.info("Knowledge base already exists. Added file to existing knowledge base of user.")

        return add_file_state
    else:
        # Ensure the URL ends with '/api/v1/knowledge/create'
        original_url = url
        url = f'{url}/api/v1/knowledge/create'

        # Prepare payload and headers for the request
        payload = {
            "name": knowledge_name,
            "description": "Collection of files created using GenFilesMCP",
        }

        # Prepare headers for the request
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }

        # Make the POST request to create the knowledge item
        response = post(url, headers=headers, data=dumps(payload))

        # Return True if created successfully, else False
        if response.status_code == 200:
            logger.info("Knowledge base created successfully.")

            # Get the new knowledge id
            knowledge_data = response.json()
            knowledge_id = knowledge_data.get('id')
            if not knowledge_id:
                logger.error("No id in response after creating knowledge")
                return False

            # Add the uploaded file to the knowledge base
            add_file_state = add_file_to_knowledge(
                url=original_url, 
                token=token, 
                knowledge_id=knowledge_id, 
                file_id=file_id
            )

            if add_file_state:
                logger.info("File added to knowledge base successfully.")
            else:
                logger.error(f"Error adding file to knowledge base")

            return True
        else:
            logger.error(f"Error creating knowledge base")
            return False
 
