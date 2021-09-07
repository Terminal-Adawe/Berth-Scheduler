from tkinter import *

def show_schedule(scheduled_berths):
	root = Tk()
	root.title("Berth scheduler")

	frame = LabelFrame(root, text="Show Schedules", padx=50, pady=50)
	frame.pack()

	schedule_hour_label = Label(frame, text="Hour")
	schedule_hour_label.grid(row=0,column=0)

	the_berth_label = Label(frame, text="Berth")
	the_berth_label.grid(row=0,column=1)

	print("about to go through all this")
	print(scheduled_berths)

	i=1
	for schedule in scheduled_berths:
		schedule_hour = Label(frame, text=schedule[3])
		schedule_hour.grid(row=i,column=0)

		the_berth = Label(frame, text=schedule[1])
		the_berth.grid(row=i,column=1)

		i=i+1

	root.mainloop()