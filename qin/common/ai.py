import httpx
import hashlib

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """Calculate the hash of a file using the specified hash algorithm.
    
    Args:
        file_path (str): The path to the file.
        hash_algorithm (str): The hash algorithm to use (e.g., 'md5', 'sha1', 'sha256').
        
    Returns:
        str: The computed hash value as a hexadecimal string.
    """
    hash_func = hashlib.new(hash_algorithm)
    
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def get_civitai_model_info_by_hash(hash: str):
    url = f'https://civitai.com/api/v1/model-versions/by-hash/{hash}'
    response = httpx.get(url)
    if(response.status_code == 200):
        return response.json()
    else:
        return None