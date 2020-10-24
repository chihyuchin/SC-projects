"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# Type this number to stop
GG = -100


def main():
	"""
	Enter numbers as temperature to calculate the highest, lowest and average temperature of the list
	function also counts the number of cold day(s), defined as temperature <16
	"""
	print('StanCode \"Weather Master 4.0"!')
	data = float(input('temperature'))
	count = 0
	average = 0
	cold_days = 0
	if data == GG:
		print('No temperature was entered')
	else:
		Highest_temperature = data
		Lowest_temperature = data
		if data < 16:
			cold_days += 1
		while True:
			data = float(input('Next temperature: (or -100 to quit)?'))
			if data != GG:
				average = (average * count + data)/(count + 1)
				count += 1
				if data < 16:
					cold_days += 1
			if data >= Highest_temperature and data != GG:
				Highest_temperature = data
			if data <= Lowest_temperature and data != GG:
				Lowest_temperature = data
			if data == GG:
				print('Highest temperature= '+str(Highest_temperature))
				print('Lowest temperature= '+str(Lowest_temperature))
				print('Average= '+str(average))
				print('Cold Day(s)= '+str(cold_days))
				break





###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
