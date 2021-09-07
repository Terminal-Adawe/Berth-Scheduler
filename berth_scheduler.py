from tkinter import *
from saveBerth import saveBerth
from saveBerth import getBerths
from saveBerth import delete_berth
from scheduler_logic import scheduler_logic
from show_schedule import show_schedule

def saveBerth_button_click():
	saveBerth(berthName.get(),berthTonnes.get(),berthCalls.get())
	berthName.delete(0,END)
	berthTonnes.delete(0,END)
	berthCalls.delete(0,END)

def get_schedule():
	final_schedule = scheduler_logic(periodInput.get(),berth_dock_time_input.get())

	show_schedule(final_schedule)


root = Tk()
root.title("Berth scheduler")

frame = LabelFrame(root, text="Berth scheduler", padx=50, pady=50)
frame.pack()

period = LabelFrame(frame, text="Period in months")
period.pack()

periodInput = Entry(period)
periodInput.pack()
periodInput.insert(0,"6")

berth_dock_time_label = LabelFrame(frame, text="Allowed berth docking time in hours")
berth_dock_time_label.pack(pady=20)

berth_dock_time_input = Entry(berth_dock_time_label)
berth_dock_time_input.pack(pady=3)
berth_dock_time_input.insert(0,"52")


availableBerths = LabelFrame(frame, text="Berths")
availableBerths.pack()

addBerth = Frame(availableBerths)
addBerth.grid(row=0, column=0)

berthPortion1 = Frame(addBerth)
berthPortion1.pack()

berthNameLabel = Label(berthPortion1, text="Add Berth")
berthNameLabel.grid(row=0, column=0)

berthName = Entry(berthPortion1)
berthName.grid(row=1, column=0, columnspan=2)

berthTonnesInputLabel = Label(berthPortion1, text="Tonnes")
berthTonnesInputLabel.grid(row=0, column=3)

berthTonnes = Entry(berthPortion1)
berthTonnes.grid(row=1, column=3)

berthCallsLabel = Label(berthPortion1, text="No of calls")
berthCallsLabel.grid(row=0, column=4)

berthCalls = Entry(berthPortion1)
berthCalls.grid(row=1, column=4)

# addBerthButton = Button(addBerth, text="Add Berth", command= lambda: saveBerth(berthName.get(),berthTonnes.get(),berthCalls.get()))
addBerthButton = Button(addBerth, text="Add Berth", command=saveBerth_button_click)
addBerthButton.pack(pady=10)


# Get berths
berths = getBerths()

# Show berths
showBerths = Frame(availableBerths)
showBerths.grid(row=0,column=1)

berthFrame = LabelFrame(showBerths, text="Available Berths")
berthFrame.pack(padx=10, pady=15)

berthViewLabels = Label(berthFrame, text="Name")
berthViewLabels.grid(row=0,column=0)

berthViewLabels = Label(berthFrame, text="Tonnes")
berthViewLabels.grid(row=0,column=1)

berthViewLabels = Label(berthFrame, text="No of calls")
berthViewLabels.grid(row=0,column=2)

print("about to print berths")
print(berths)

i=1
for berth in berths:

	berthViewName = Label(berthFrame, text=berth[0])
	berthViewName.grid(row=i,column=0)

	berthViewTonnes = Label(berthFrame, text=berth[1])
	berthViewTonnes.grid(row=i,column=1)

	berthViewCalls = Label(berthFrame, text=berth[2])
	berthViewCalls.grid(row=i,column=2)

	deleteBerthButton = Button(berthFrame, text="Delete Berth", command= lambda: delete_berth(berth[3]))
	deleteBerthButton.grid(row=i, column=3)

	i=i+1


scheduled_frame = LabelFrame(frame, text="schedules")
scheduled_frame.pack(pady=5)

addBerthButton = Button(scheduled_frame, text="Schedule Berths", command=get_schedule)
addBerthButton.pack(pady=20, padx=5)

schedules = Frame(scheduled_frame)
schedules.pack(pady=10, padx=8)



print(berths)




root.mainloop()