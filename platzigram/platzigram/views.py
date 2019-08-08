from django.http import HttpResponse

# utilities
from datetime import datetime
import json

def hello_world(request):
	now = datetime.now().strftime('%b %dth %Y - %H:%M hrs');
	return HttpResponse('oh hi! Current server time is {now}'.format(now=now))

def sort_integers(request):
	print(request)
	# import pdb; pdb.set_trace()
	# pulse key 'c' to exit debug and send response

	# numbers is a string '10,4,50,32'
	numbers = request.GET['numbers']
	numbers = numbers.split(',') # list of string split by comma
	numbers = [int(i) for i in numbers ] # list of integer
	sorted_ints = sorted(numbers) # sort list

	data = {
		'status'  : 'ok',
		'numbers' : sorted_ints,
		'message' : 'Integers sorted successfuly'
	}
	# method dumps translate dictionary to json
	return HttpResponse(
		json.dumps(data, indent=4), 
		content_type='application/json'
	)

def say_hi(request,name,age):
	if age < 12:
		message = 'Sorry {}, you are not allowed here'.format(name)
	else:
		message = 'Hello {}, welcome to Platzigram'.format(name)

	return HttpResponse(message)