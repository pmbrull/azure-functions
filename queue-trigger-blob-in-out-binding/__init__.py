import logging
import azure.functions as func


def main(msg: func.QueueMessage,
         inputblob: func.InputStream,
         outputblob: func.Out[func.InputStream]) -> None:

    logging.info(
        f"""Blob name is: {inputblob.name)}"""
        )

    text = inputblob.read().decode('utf-8')
    logging.info("Clear text:%s'", text)

    # 4. Write to Blob file
    outputblob.set(inputblob)
