Format = {
	1:"Month Day, Year. Example: January 1, 2016", 
	2:"MM/DD/YY. Example: 01/01/16", 
	3:"MM/DD/YYYY. Example: 01/01/2016"
}

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
months_capitalized = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print Format

def longform_year(short_year):
	if short_year < 16:
		return short_year + 2000
	else:
		return short_year + 1900

def choose_format(choice):
	choice = raw_input("Select a format for your data: ")
	return choice

def date_reformat(date_string, target_format):
	if date_string[0].isalpha():
		if target_format == 1:
			return date_string
		if target_format == 2:
			date_list = date_string.split(' ')
			date_list[0] = str(months.index(date_list[0])+1).zfill(2)
			date_list[2] = date_list[2][2:]
		if target_format == 3:
			date_list = date_string.split(' ')
			date_list[0] = str(months.index(date_list[0]) + 1).zfill(2)
			date_list[1] = date_list[1][0:-1]
			if len(date_list[1]) == 1:
				date_list[1] = date_list[1].zfill(2)
		return '/'.join(date_list)

	elif '/' in date_string and 6<= len(date_string) <= 8:
		date_list = date_string.split('/')
		if target_format == 1:
			date_list[0] = int(date_list[0])
			date_list[0] = months[date_list[0] -1]
			date_list[2] = longform_year(date_list[2])
			return date_list[0] + " "  + date_list[1] + ", " + date_list[2]
		if target_format == 2 or target_format == 3:
			date_list[0] = date_list[0].zfill(2)
			date_list[1] = date_list[1].zfill(2)	
		if target_format == 3:
			date_list[2] = longform_year(date_list[2])	
		return '/'.join(date_list)	

	elif '/' in date_string and len(date_string) == 10:
		if target_format == 1:
			date_list = date_string.split('/')
			date_list[0] = int(date_list[0])
			date_list[0] = months[date_list[0] -1]
			date_list[1] = int(date_list[1])
			return date_list[0] + " "  + date_list[1] + ", " + date_list[2]
		if target_format ==2:
			date_list = date_string.split('/')
			date_list[2] = date_list[2][2:]
			return '/'.join(date_list)
		if target_format == 3:
			return date_string

format = int(raw_input("what is the target format?: "))
date = raw_input("What is today's date?: ").lower()
print date_reformat(date, format)

