from urllib import request, parse, error
from bs4 import BeautifulSoup as bs

def getData(url):
	print('Requesting resource')
	# Request url
	try:
		source = request.urlopen(url)
	# Return any errors
	except Exception as e:
		print(e)
		return False
	# Parse html if request was successful
	else:
		data = bs(source, 'html.parser')	
		print('Resource returned')
		return data

def selectData(element, returnAttribute):
	results, value = [], ''
	# Return string from element
	if returnAttribute is False:
		# Skip if there is no string
		value = ''.join([s.strip() for s in element.findAll(text=True)])

	# Return attribute from element
	else:
		value = str(element[returnAttribute]).strip()

	# Append value to results if not blank
	if value != '':
		results.append(value)
	return results

def filterData(data, parameters):
	results, returnAttribute = [], False
	# Determine if an attribute should be returned
	if parameters[-1] == '@':
		# Remove @ symbol from filter
		parameters = parameters[:-1]
		# Separate last attribute tag from other parameters
		returnAttribute = parameters.split('[')[-1][:-1]

	# Select elements from data
	data = data.select(parameters)

	# Go through each piece of data
	for element in data:
		# Select data and append results
		results = results + selectData(element, returnAttribute)

	return results

def sparse(url, parameters, data=False):
	results = []
	# Skip processing if filter values aren't set
	if parameters == '':
		print('A filter must be set')
	else:
		# Get data if not included with function call (included for CLI session)
		if data is False:
			data = getData(source)

		# If data was included or obtained
		if data is not False:
			# Filter data
			results = filterData(
				data=data,
				parameters=parameters
			)
			print('Found: ' + str(len(results)))
			# Sort results alphabetically
			results.sort()
	return results

# Main
if __name__ == '__main__':
	# Variable to track if session is active
	active = True
	# Define url and generate filename
	source = input('Target URL: ')
	fileName = parse.urlparse(source).netloc.strip('/') + '.txt'
	
	# Get data
	data = getData(source)
	# Stop interactive session if no data was returned
	if data is False:
		active = False

	# Wrap session to allow ctrl-c exit
	try:
		# If session is active
		while active is True:
			parameters = input('Filter parameters: ')
			if parameters == '':
				print('A filter must be set')
			# And parameters have been set
			else:
				# Run parse function
				results = sparse(source, parameters, data)

				# Output top 10 results (if any) to user
				if len(results) > 0:
					print('Example results:')
					for item in results[0:10]:
						print(item)
					# Check if the data should be saved
					saveData = input('Save the data? (y/n) (default=n) : ')
					if saveData == 'y' or saveData == 'yes':
						# Save data
						with open(fileName, 'w') as file:
							for line in results:
								file.write(line + '\n')
						print('Saved as: ' + fileName)
						# End session
						active = False
	# End session
	except KeyboardInterrupt:
		print('')
		active = False
