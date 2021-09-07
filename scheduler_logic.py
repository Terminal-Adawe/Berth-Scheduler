from saveBerth import getBerths


def scheduler_logic(period,allowed_time):
	monthly_period = int(period)
	daily_period = monthly_period * 30
	hourly_period = daily_period * 24

	allowed_time = int(allowed_time)

	# print("Hourly period id ")
	# print(hourly_period)

	berths = getBerths()

	transformed_berths = []

	for berth in berths:
		list_berth = list(berth)
		berth_interval = hourly_period/berth[2]

		# print("Division between "+str(hourly_period)+" and "+str(berth[2])+" is "+str(berth_interval))
		# Interval on 4th array
		list_berth.append(berth_interval)

		# Interval plus allowed docking time in hours, 5th array
		list_berth.append(berth_interval)

		# Check to show if already appeared, 6th array
		list_berth.append(0)

		# new_berth = tuple(list_berth)
		new_berth = list_berth

		transformed_berths.append(new_berth)

		print(new_berth)

	# print("berths are now...")
	# print(transformed_berths)

	final_schedule = []

	updated = 0

	

	for x in range(allowed_time, hourly_period, allowed_time):
		bar = [0,"none",hourly_period]

		print("Available Berths are ")
		print(transformed_berths)

		for berth in transformed_berths:
			differential = abs(berth[5]-x)
			# print("Differential between "+str(berth[5])+" and "+str(x)+" is ")
			# print(differential)

			# if differential < int(bar[2]) and int(berth[5]) < updated+1:
			if differential < int(bar[2]):
				# print("differential is small so setting bar")
				bar = [berth[3],berth[0],differential,x]

				

			

			# print("berths now...")
			# print(transformed_berths)
			# print("with bar...")
			# print(bar)
			

			# print("So the new berth is ")
			# print(berth)

		print("Smallest Berth is ")
		print(bar)

		for index,berth in enumerate(transformed_berths):
			# if berth[3]==bar[0] and berth[6] < updated+1:
			if berth[3]==bar[0]:
				# print("checker 22...")
				final_schedule.append(bar)
				berth[6] = updated+1

				print("Equal berth to smallest is ")
				print(berth)
				# Very important logic. Shows which next interval it should appear
				berth[5] = berth[4] + x



		checker = 0
		for index,berth in enumerate(transformed_berths):
			# print("Index "+str(index)+" checking berth "+str(berth[6])+" compared with previous berth "+str(transformed_berths[index-1][6]))
			if index>0 and berth[6]!=transformed_berths[index-1][6]:
				checker = 1


		if checker==0:
			updated = updated + 1
		# print("That berth is now ")
		# print(transformed_berths)


		

	print("final schedule is ")
	print(final_schedule)

	return final_schedule


