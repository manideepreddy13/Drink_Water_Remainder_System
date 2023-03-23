import time

from plyer import notification


if __name__ == "__main__":
    notification.notify(
        title="REMINDER!!!",
        message="It's Time to Drink Water.",
        app_icon=r"C:\Users\manid\OneDrive\Desktop\Python\Drink Water Reminder Notification\drinkwater.ico",
        timeout=20
    )

    time.sleep(7200)
