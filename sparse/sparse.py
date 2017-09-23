from urllib import request, parse, error
from bs4 import BeautifulSoup as bs

def getData(url):
	print('Requesting resource')
	# Request url
	source = request.urlopen(url)
	# Parse html
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
	# Define list for results
	results, returnAttribute = [], False
	# Determine if an attribute should be returned
	if parameters[-1] == '@':
		# Remove @ symbol from filter
		parameters = parameters[:-1]
		# Extract last attribute tag
		returnAttribute = parameters.split('[')[-1][:-1]

	# Select elements from data
	data = data.select(parameters)

	# Go through each piece of data
	for element in data:
		# Select data and append results
		results = results + selectData(element, returnAttribute)

	# Return output data
	return results

def sparse(url, parameters):
	results = []
	# Skip processing if filter values aren't set
	if parameters == '':
		print('A filter must be set')
	else:
		# Retrieve URL data
		try:
			data = getData(source)
		except ValueError:
			print('Invalid URL')
		except error.URLError as e:
			print(e)
		else:
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
	# Define parameters
	source = input('Target URL: ')
	parameters = input('Filter parameters: ')
	# Derive filename from url
	fileName = parse.urlparse(source).netloc.strip('/') + '.txt'

	# Run parse function
	results = sparse(source, parameters)

	# Output results information to user
	if len(results) > 0:
		print('Example results:')
		for item in results[0:10]:
			print(item)
		# Save data
		saveData = input('Save the data? (y/n): ')
		if saveData == 'y' or saveData == 'yes':
			with open(fileName, 'w') as file:
				for line in results:
					file.write(line + '\n')
			print('Saved as: ' + fileName)
