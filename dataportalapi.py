import requests
import json
import math

#This is the url of your Socrata domain
sURL = 'https://data.sfgov.org'
payload = {'limit' : 620}
r = requests.get(sURL + '/api/search/views.json', params=payload)

responses = r.json()
out = []

def check_categories(d,category):
  for i in range(len(d)):
    if d[i]['name'] == category: return i
  return -1

for response in responses['results']:
	view = response['view']
	if len(view['columns']) != 0:
		name = view['name']
		vid = view['id']
		views = view['viewCount']
		size = view['columns'][0]['cachedContents']['non_null']
		if size == 0:
			size = 1
		logsize = math.log(size)
		if 'category' in view:
			category = view['category']
		else:
			category = "None"
		if 'tags' in view:
			for tag in view['tags']:
				#tags aren't used in the json file yet, these could probably be used to do alternate visualizations or in a companion list, this is just a placeholder for now
				foo = tag
		index = check_categories(out,category)
		url = "http://data.sfgov.org"
		if index == -1:
			out.append({"name": category, "children": [ {"name": name, "value": size, "url": url, "log": logsize } ] })
		else:
			out[index]["children"].append({"name": name, "value": size, "url": url, "log": logsize })

final = {"name" :" San Francisco Data Portal", "children" : out}
print json.dumps(final)