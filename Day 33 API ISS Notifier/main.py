import time
from iss import Iss

iss = Iss()


def send_email():
    print("Sending email.")


while True:
    iss.update_info()
    if iss.is_visible():
        send_email()
        time.sleep(420)
        # ISS is only visible for 1-6 minutes.
        # Waits 7 minutes after ISS was visible to check again
    else:
        time.sleep(60)
        # If ISS is not visible, wait 1 minute and check again
