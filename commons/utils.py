
def extract_msg_blob_name(msg: dict) -> str:
    """Normalize and Event Hub subject as a BLOB name"""

    return msg['subject'].replace('/blobServices/default/containers/', '').replace('blobs/', '')
