# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import random
from datetime import datetime

from module.uimap import *
from module.weather_api import OpenWeatherAPI

import requests

try :
    import Tkinter as tkinter
except ImportError:
    import tkinter

from tkinter.constants import *
import tkinter.messagebox
from PIL import Image, ImageTk

class App:

    def __init__(self, root, title, user):
        self.root = root
        self.root.title('piWeatherman')
        # Set Geometry to your Raspberry Pi Display Size
        # In case you don't want it fullscreen
        self.root.geometry('460x300') # Default is 460x300
        self.mainframe = tkinter.Frame(self.root)

        self.user = user

        if (self.user is None):
            self.registerGUI()
        else :
            self.weathermanGUI()

        self.mainframe.pack(fill=BOTH, expand=True)

    def registerGUI(self):
        form = tkinter.Frame(self.mainframe)

        # Color Scheme : Sort by elements
        BACKGROUND = SEMI_CLOUDY_DAY
        FOREGROUND = WHITE
        BUTTONS = SEMI_CLOUDY_DAY_ACCENT

        page_title = tkinter.Label(
            form, text='Registration', font=('Roboto', 20),
            background=BACKGROUND, foreground='#FFF'
            ).pack(pady=10)

        fullname_label = tkinter.Label(
            form, text='Full Name', width=20, font=('Roboto', 14),
            background=BACKGROUND, foreground=WHITE
            ).pack()
        fullname_entry = tkinter.Entry(form, bd=0, justify=CENTER)
        fullname_entry.pack()

        key_label = tkinter.Label(
            form, text='API Key', width=20, font=('Roboto', 14),
            background=BACKGROUND, foreground=WHITE
            ).pack()
        key_entry = tkinter.Entry(form, bd=0, justify=CENTER)
        key_entry.pack()

        locality_label = tkinter.Label(
            form, text='Locality', width=20, font=('Roboto', 14),
            background=BACKGROUND, foreground=WHITE
            ).pack()
        locality_entry = tkinter.Entry(form, bd=0, justify=CENTER)
        locality_entry.pack()

        def create_user():

            username = fullname_entry.get()
            api_key = key_entry.get()
            locale = locality_entry.get()

            if (confirmation.get()):
                with open('data/user.json', 'w') as user_information:
                    self.user = {
            	       "name": str(username),
            	       "api-key": str(api_key),
            	       "locale": str(locale)
                    }
                    json.dump(self.user, user_information)
                    form.destroy()
                    self.weathermanGUI()
            else :
                tkinter.messagebox.showinfo(
                    title='Check Confirmation', message='Click confirm to continue'
                    )

        confirmation = tkinter.IntVar()
        confirmation.set(0)
        confirmation_check = tkinter.Checkbutton(
            form, variable=confirmation, onvalue=1, offvalue=0, fg=BLACK,
            text="Confirm Information?", bg=BACKGROUND, bd=0, highlightthickness=0
            ).pack(pady=10)
        submitButton = tkinter.Button(
            form, text='Submit', font=('Roboto', 14), width=20,
            background=BUTTONS, foreground=WHITE, command=create_user, bd=0
            ).pack()

        form.configure(background=BACKGROUND)
        form.pack(fill=BOTH, expand=True)

    def weathermanGUI(self):

        window = tkinter.Frame(self.mainframe)
        header_frame = tkinter.Frame(window)
        middle_frame = tkinter.Frame(window)
        footer_frame = tkinter.Frame(window)

        def update_window():
            """ Updates the window and weather data every 10 Minutes """

            weather_api = OpenWeatherAPI(key=self.user['api-key'])
            current_weather = weather_api.current_weather(q=self.user['locale'])

            # Safe Checking : Incase of Bad Requests
            if (current_weather['cod'] == 200):
                weather_now = current_weather
            else :
                print('Error {code} : {message}'.format(
                    code=current_weather['cod'],
                    message=current_weather['message']
                ))
                sys.exit()

            # Color Scheme (sort by element) open module/uimap for changes
            weather_id = weather_now['weather'][0]['id']
            hour_now = time.strftime('%H')

            # This maps the weather from uimap.py and https://openweathermap.org/weather-conditions
            for id, name in weather_code_range:
                if (weather_id in id):
                    key_descriptor = name
                    break
            # Find a better method to map this

            FOREGROUND = ui_map['foreground']
            if int(hour_now) >= 6 and int(hour_now) <= 18:
                # DAY TIME
                BACKGROUND = ui_map[key_descriptor]['day']['background']
                ACCENT = ui_map[key_descriptor]['day']['accent']
                IMAGE = ui_map[key_descriptor]['day']['image']
            else :
                # NIGHT TIME
                BACKGROUND = ui_map[key_descriptor]['night']['background']
                ACCENT = ui_map[key_descriptor]['night']['accent']
                IMAGE = ui_map[key_descriptor]['night']['image']

            weather_title.configure(text='{weather} at\n{locale}'.format(
                weather=(weather_now['weather'][0]['description']).capitalize(),
                locale=(self.user['locale']).capitalize()
            ), background=BACKGROUND)

            forecast_img = ImageTk.PhotoImage(Image.open(IMAGE))
            forecast_label.configure(image=forecast_img, background=BACKGROUND)
            forecast_label.image = forecast_img

            env_detail_label.configure(background=ACCENT, foreground=FOREGROUND)

            # Change this if you want to switch (default : Celcius)
            k_to_c = int(weather_now['main']['temp'] - 273)
            k_to_f = (weather_now['main']['temp'] - 32) * (5/9)

            temp_giant_label.configure(
                text='{temp}°C'.format(temp=k_to_c), background=WHITE, foreground=ACCENT)
            wind_label.configure(
                text='Wind Speed : {wind} m/s'.format(wind=weather_now['wind']['speed']),
                background=WHITE, foreground=ACCENT)
            humid_label.configure(
                text='Humidity : {humid}%'.format(humid=weather_now['main']['humidity']),
                background=WHITE, foreground=ACCENT)
            pressure_label.configure(
                text='Pressure : {press} hPa'.format(press=weather_now['main']['pressure']),
                background=WHITE, foreground=ACCENT)

            header_frame.configure(background=BACKGROUND)
            window.configure(background=BACKGROUND)

            # Set to update every 10 Minutes (1000 ms = 1 second)
            # NOTE: Don't set the interval to close, weather doesn't change to often
            window.after(600000, update_window)

        # Header Forecast and City
        weather_title = tkinter.Label(
            header_frame, width=20, font=('Roboto', 18), foreground=WHITE, justify=LEFT
            )
        weather_title.pack(side=LEFT)

        forecast_label = tkinter.Label(header_frame)
        forecast_label.pack(side=RIGHT, padx=20)

        # Middle Frame (Temperature and Details)
        env_detail_label = tkinter.Label(
            middle_frame, text='Environment Details', width=20, font=('Roboto', 14),
            justify=CENTER
            )
        env_detail_label.pack(fill=X)

        env_detail = tkinter.Frame(middle_frame)
        env_detail.pack(fill=X, side=RIGHT, anchor=E, pady=20, padx=25)

        temp_frame = tkinter.Frame(middle_frame)
        temp_frame.pack(fill=X, side=LEFT, anchor=W, pady=20)

        temp_giant_label = tkinter.Label(
            temp_frame, width=10, font=('Roboto', 40)
            )
        temp_giant_label.pack(side=LEFT, anchor=E)

        wind_label = tkinter.Label(
            env_detail, font=('Roboto', 12)
            )
        wind_label.pack(fill=X, anchor=W)

        humid_label = tkinter.Label(
            env_detail, font=('Roboto', 12)
            )
        humid_label.pack(fill=X, anchor=W)

        pressure_label = tkinter.Label(
            env_detail, font=('Roboto', 12), justify=LEFT
            )
        pressure_label.pack(fill=X, anchor=W)

        # Footer Frame (Teleprompter)
        clock_label = tkinter.Label(
            footer_frame, width=20, font=('Roboto', 12),
            background=BLACK, foreground=WHITE, justify=LEFT
            )
        clock_label.pack(fill=BOTH)

        def update_time():
            """ Update time every second """
            current_time = time.strftime('%H:%M:%S')
            clock_label.configure(text=current_time)
            footer_frame.after(1000, update_time)

        update_time()

        header_frame.pack(fill=BOTH, anchor=N, expand=True)
        middle_frame.pack(fill=BOTH, anchor=CENTER, expand=True)
        footer_frame.pack(fill=BOTH, anchor=S, expand=True)

        middle_frame.configure(background=WHITE)
        footer_frame.configure(background=BLACK)
        window.pack(fill=BOTH, expand=True)

        update_window()


if __name__ == '__main__':
    root = tkinter.Tk()
    title = 'piWeatherman'

    if (os.path.exists('data/user.json')):
        with open('data/user.json', 'r') as user_information:
            user = json.load(user_information)
    else :
        user = None

    # By default, fullscreen is Off
    fullscreen = False
    def fullscreenToggle():
        global fullscreen
        if (fullscreen):
            fullscreen = False
        else :
            fullscreen = True
        return fullscreen

    app = App(root, title, user)
    icon = ImageTk.PhotoImage(Image.open('assets/image/icon/icon.ico'))

    # Compatible with python 2 and python 3
    try :
        root.iconphoto(True, icon)
    except AttributeError:
        root.tk.call('wm', 'iconphoto', root._w, icon)

    try :
        root.bind("<F11>", lambda event : root.attributes('-fullscreen', fullscreenToggle()))
        root.bind("<Escape>", lambda event:root.destroy())
        root.mainloop()
    except(EOFError, KeyboardInterrupt) :
        root.destroy()
        sys.exit()
