import logging
import azure.functions as func


def main(msg: func.QueueMessage,
         inputblob: func.InputStream) -> func.InputStream:

    return inputblob
