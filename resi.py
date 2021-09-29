button1 = tk.Button(frame,text = 'Search',bg = 'gray')
button1.place(relx = 0.85,rely = 0.12,relheight = 0.8,relwidth = 0.29,anchor = 'n')

entry = tk.Entry(frame,bg = 'white')
entry.place(relx = 0.35,rely = 0.1,relheight = 0.8,relwidth = 0.65,anchor = 'n')

canvas = tk.Canvas(root,height = HEIGHT,width = WIDTH)
canvas.pack()

background_in.place(relwidth = 1,relheight = 1)