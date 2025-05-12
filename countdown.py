import time

# Ask the user for input in seconds
try:
    countdown_time = int(input("Enter countdown time in seconds: "))
    if countdown_time < 0:
        print("Please enter a positive number.")
    else:
        print(f"Countdown starts for {countdown_time} seconds.")
        while countdown_time > 0:
            mins, secs = divmod(countdown_time, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            print(timer_display, end="\r")  # Overwrites the line
            time.sleep(1)
            countdown_time -= 1

        print("Time's up!            ")
        # Replace 'alarm.mp3' with the path to your sound file
        # playsound('alarm.mp3')

except ValueError:
    print("Invalid input. Please enter a number.")
