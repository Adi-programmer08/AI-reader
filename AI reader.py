import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Welcome to our program SHOUTOUTS TO EVERYONE!")
print("\nThis program reads the data which in written.")

data = input("\nEnter the data here --> ")

time.sleep(1)
print("Reading the lines....")
speaker.Speak(data)