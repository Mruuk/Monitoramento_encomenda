import hashlib
import schedule
import time
from twilio_client import send_sms
from scrapping import get_scrapping_correios
from telegram_client import send_msg

# Lista de códigos de correio
codigos_correio = ['CODE_CORREIOS', 'CODE_CORREIOS']
executou_entry_code = False 
def entry_code(code):
    with open(f"hash_{code}.txt","w") as file:
        file.write('')

if not executou_entry_code:
    for code in codigos_correio:
        entry_code(code)
    executou_entry_code = True

def job():
    for codigo_correio in codigos_correio:
        with open(f"hash_{codigo_correio}.txt", "r") as arquivo:
            hash_data_at = arquivo.read()

        result, verifica, data = get_scrapping_correios(codigo_correio, hash_data_at)

        if verifica == True:
            result = "Sem atualizações"
            # Telegram:
            send_msg(result)
            # SMS Twilio:
           # send_sms("YOUR_NUMBER", result)

        else:
            # Telegram:
            send_msg(result)
            # SMS Twilio:
           # send_sms("YOUR_NUMBER", result)

        with open(f"hash_{codigo_correio}.txt", "w") as arquivo:
            arquivo.write(data)

# Schedule the job to run every day at 10:00 AM.
schedule.every().day.at("10:40").do(job)

# Keep the program running indefinitely.
while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
    # Start the job.
    job()