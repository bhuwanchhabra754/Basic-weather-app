import requests
import json
import tkinter as tk
def get_weather():
    location=city_entry.get()
    degree = degree_entry.get().upper()
    api_url=f"http://api.weatherapi.com/v1/current.json?key=9e0066fce7b74e7798a95200241608&q={location}&aqi=no"
    response=requests.get(api_url)
    result=json.loads(response.text)
    print_text=(
    f"Temperature at {location} is: ", result["current"]["temp_c"],f"°{degree}"
    (f"Humidity level at {location} is: ",result["current"]["humidity"])
    (f"Cloudiness at {location} is: ",result["current"]["cloud"],"%")
    )
import requests
import json
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def get_weather():
    location = city_entry.get()
    degree = degree_entry.get().upper()

    api_url = f"http://api.weatherapi.com/v1/current.json?key=9e0066fce7b74e7798a95200241608&q={location}&aqi=no"
    response = requests.get(api_url)
    result = json.loads(response.text)
    temp = result["current"]["temp_c"] if degree == "C" else result["current"]["temp_f"]
    humidity = result["current"]["humidity"]
    cloudiness = result["current"]["cloud"]
        
    result_text = (
        f"Temperature at {location} is: {temp}°{degree}\n"
        f"Humidity level at {location} is: {humidity}%\n"
        f"Cloudiness at {location} is: {cloudiness}%"
    )
    result_label.config(text=result_text)

root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")
root.resizable(False, False)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')

city_label = tk.Label(frame, text="City:", font=('Math Sans', 14))
city_label.place(relwidth=0.2, relheight=1)
city_entry = tk.Entry(frame, font=('Math Sans', 12))
city_entry.place(relx=0.2, relwidth=0.5, relheight=1)

degree_label = tk.Label(frame, text="Unit (C/F):", font=('Math Sans', 14))
degree_label.place(relx=0.7, relwidth=0.2, relheight=1)
degree_entry = tk.Entry(frame, font=('Math Sans', 12))
degree_entry.place(relx=0.9, relwidth=0.1, relheight=1)

fetch_button = tk.Button(root, text="Get Weather", font=('Math Sans', 14), command=get_weather)
fetch_button.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.45, anchor='n')

result_label = tk.Label(lower_frame, font=('Math Sans', 14), anchor='nw', justify='left', bd=4)
result_label.place(relwidth=1, relheight=1)

root.mainloop()


root = tk.Tk()
root.title("Weather App")
root.geometry("500x600")
root.resizable(False, False)

# Load and set background image (uncomment if you have a background image)
# background_image = Image.open("background.jpg")  # Replace with your image path
# background_photo = ImageTk.PhotoImage(background_image)
# background_label = tk.Label(root, image=background_photo)
# background_label.place(relwidth=1, relheight=1)

# Create a frame for the main content
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')

# City Entry
city_label = tk.Label(frame, text="City:", font=('Courier', 14))
city_label.place(relwidth=0.2, relheight=1)
city_entry = tk.Entry(frame, font=('Courier', 14))
city_entry.place(relx=0.2, relwidth=0.5, relheight=1)

# Degree Entry
degree_label = tk.Label(frame, text="Unit (C/F):", font=('Courier', 14))
degree_label.place(relx=0.7, relwidth=0.2, relheight=1)
degree_entry = tk.Entry(frame, font=('Courier', 14))
degree_entry.place(relx=0.9, relwidth=0.1, relheight=1)

# Fetch Button
fetch_button = tk.Button(root, text="Get Weather", font=('Courier', 14), command=get_weather)
fetch_button.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1, anchor='n')

# Create a lower frame for the results
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.45, anchor='n')

# Result Display
result_label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
result_label.place(relwidth=1, relheight=1)

# Run the application
root.mainloop()
