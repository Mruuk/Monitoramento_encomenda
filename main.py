import hashlib
import schedule
import time
from twilio_client import send_sms
from scrapping import get_scrapping_correios

def job():
    with open("hash.txt", "r") as arquivo:
	    hash_data_at = arquivo.read()
         
    # Get the latest data from the Correios website.
    result, verifica, data = get_scrapping_correios('NB789880903BR',hash_data_at)

    # Compare the new hash with the old hash.
    if verifica == True:
        # The data has not changed.
        result = "Sem atualizações"
        send_sms('+5545999805505', result)
    else:
        # The data has changed.
        send_sms('+5545999805505', result)

    # Update the old hash with the new hash.
    with open("hash.txt", "w") as arquivo:
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