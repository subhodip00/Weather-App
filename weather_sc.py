import tkinter as tk
import requests

def test_func(entry):
    print('This is : ',entry)

def get_weather(city):
    weather_key = '66da54aeb2f9ec59563464a70dfc476f'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,'q' : city,'units':'metric'}
    response = requests.get(url,params= params)
    weather = response.json()

    label['text'] = disp_weather(weather)


def disp_weather(weather):
    try:
        name = weather['name']
        temperature = weather['main']['temp']
        description = weather['weather'][0]['description']
        final_response = 'City : %s\nTemperature(C) : %s\nConditions : %s' % (name,temperature,description.capitalize())
    except:
        final_response = 'Data not Found'
    
    return final_response


root = tk.Tk()

background = tk.PhotoImage(file = 'photo2.png')
background_in = tk.Label(root,image = background)
background_in.pack()

frame  = tk.Frame(root,bg = '#80c1ff',bd = 5)
frame.place(relx = 0.5,rely = 0.1,relheight = 0.1,relwidth = 0.8,anchor = 'n')

frame2 = tk.Frame(root,bg = '#80c1ff',bd = 10)
frame2.place(relx = 0.5,rely = 0.3,relheight = 0.6,relwidth = 0.8,anchor = 'n')

button1 = tk.Button(frame,text = 'Search',bg = 'gray',font = 30,command = lambda:get_weather(entry.get()))
button1.place(relx = 0.7,relheight = 1,relwidth = 0.3)

entry = tk.Entry(frame,bg = 'white',font = 30)
entry.place(relx = 0.35,relheight = 1,relwidth = 0.7,anchor = 'n')

label = tk.Label(frame2,bg = 'white',font = 50, anchor = 'nw',justify = 'left')
label.place(relheight = 1,relwidth = 1)


tk.mainloop()