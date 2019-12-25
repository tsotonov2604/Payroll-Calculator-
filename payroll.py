# The managerial staff are required to work 10 hours per day at the rate of $30 per hour.
# The technical staff are required to work 8 hours per day at the rate of $25 per hour.
# The janitorial staff are required to work 7 hours per day at the rate of $10 per hour.

# WORK DAY HOURS: 6:00AM - 00:00AM 

# When employee works less than required hours RATE: houry rate * 0.8
# OVERTIME: houry rate * 1.25 for the extra hour 

# M : MANAGERIAL , T: TECHNICAL, J: JANITORIAL 

def worker():
    employee = input("What is your category of employment? (’M’ for managerial, ’T’ for technical, and ’J’ for janitorial) ")
    employee = employee.upper()
    while employee not in ('M','T','J'):
        print(employee + " is not a propper category of employment.")
        employee = input("What is your category of employment? (’M’ for managerial, ’T’ for technical, and ’J’ for janitorial) ")
        employee = employee.upper()
    return employee

def hours(): 
	begin_time = str(input("At what time does your work day begin? (minilary format, eg: 8:45AM = 2045)"))
	end_time = str(input("At what time does your work day end? (minilary format, eg: 8:45AM = 2045)"))
	if len(begin_time) != 4 or len(end_time) != 4:
		return 
	if int(begin_time[0:2]) > 23 or int(end_time[0:2]) >23: 
		print("Please enter a valid time (military format).")
		return 
	if int(begin_time[-2:]) > 59 or int(end_time[-2:]) > 59:
		print("Please enter a valid time (military format).")
		return 
	if begin_time[0:2] == '05' and begin_time[-2:] == '59':
		print("You cannot clock in before 0600")
		return 
	if end_time =='0000':
		print("You cannot end after 0000")
		return
	worked_hours = int(end_time[0:2]) - int(begin_time[0:2])
	if begin_time[-2:] == '00' and end_time[-2:] == '00':
		worked_minutes = 0 
	else:
		worked_minutes = 59 - int(end_time[-2:])

	hours_worked = str(worked_hours)+str(worked_minutes)
	return worked_hours,worked_minutes

def pay(): 
	staff_member= worker()
	hours_worked = hours()

	#MANAGERIAL 
	if staff_member == 'M' and hours_worked[0] == 10: # required work hours: 10 
		hourly_salary = (hours_worked[0])* (30)

	if staff_member == 'M' and hours_worked[0] < 10:
		hourly_salary = (hours_worked[0])* (30 * 0.8)
		minute_salary = (hours_worked[1]/60)*(30 *0.8)
		hourly_salary = hourly_salary + minute_salary

	if staff_member == 'M' and hours_worked[0] > 10: 
		minute_salary = (hours_worked[1]/60)*30
		overtime = ((hours_worked[0] - 10) * (30*1.25)) + (300) + minute_salary
		hourly_salary = overtime

	#TECHNICAL
	if staff_member == 'T' and hours_worked[0] == 8: # required work hours: 8 
		hourly_salary = (hours_worked[0])* (25)

	if staff_member == 'T' and hours_worked[0] < 8:
		hourly_salary = (hours_worked[0])* (25 * 0.8)
		minute_salary = (hours_worked[1]/60)*(25 *0.8)
		hourly_salary = hourly_salary + minute_salary

	if staff_member == 'T' and hours_worked[0] > 8: 
		minute_salary = (hours_worked[1]/60)*25
		overtime = ((hours_worked[0] - 8) * (25*1.25)) + (200) + minute_salary
		hourly_salary = overtime

	#JANITORIAL
	if staff_member == 'J' and hours_worked[0] ==7: # required work hours: 7
		hourly_salary = (hours_worked[0])* (10)	

	if staff_member == 'J' and hours_worked[0] < 7:
		hourly_salary = (hours_worked[0])* (10 * 0.8)
		minute_salary = (hours_worked[1]/60)*(10 *0.8)
		hourly_salary = hourly_salary + minute_salary

	if staff_member == 'J' and hours_worked[0] > 7: 
		minute_salary = (hours_worked[1]/60)*10
		overtime = ((hours_worked[0] - 7) * (10*1.25)) + (70) + minute_salary
		hourly_salary = overtime

	return hourly_salary,staff_member,hours_worked

def main(): 
	comp = pay()
	emp_type = {'M':"Managerial","T":"Technical","J":"Janitorial"}
	employee = comp[1]
	print("----Daily Salary Report----")
	for key, value in emp_type.items(): 
		if key == employee: 
			print("Type of emplyment: " + value)
	print("Total time worked (hours,minutes): " + str(comp[2]))
	print("Total salary: ${0:.2f}".format(comp[0]))

main()


