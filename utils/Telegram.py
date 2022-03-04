import requests, logging
logger= logging.getLogger()

def sendTelegram(token, cid, message: str):
    send_text = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={cid}&text={message}"
    response = requests.post(send_text)
    logger.info("Telegram Message Sent: " + message)
    return response.json()