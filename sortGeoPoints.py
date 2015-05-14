#!/opt/local/bin/python
#
# Author: 		isa56k
# Filename: 	sortGeopoints.py
# Date: 		14/05/2015
# Description: 	Takes two parameters, input file of JSON and output file of JSON. 
#			   	Then adds a location object as per the GeoPoint type in parse.com.
import sys
import json

# get the filename to process as first parameter
file_name = sys.argv[1]
output_filename = sys.argv[2]

# set up an array to hold our JSON
json_to_write_to_file = []
# open file and read in the json
with open(file_name) as json_file_data:
	# load the json into data
	data = json.load(json_file_data)
	# for each attribute line in the results element
	for results in data["results"]:
		# extract the lat
		lat = results["latitude"]
		# extract the long
		lon = results["longitude"]
		# setup a GeoPoint with the long and lat as floats
		geoPoint = {'__type': 'GeoPoint', 'latitude': float(lat), 'longitude': float(lon)}
		# convert the GeopPoint to json
		geoPointJSON = json.dumps(geoPoint, ensure_ascii=True)
		# add the location as a geopoint to the original json 
		results["location"] = geoPoint
		# append the json to our array
		json_to_write_to_file.append(results)

# setup a dictionary that we can add our JSON too
final_json = {}
# create the results object in our dicitonary
final_json["results"] = json_to_write_to_file
# setup a file to write to
outputfile = open(output_filename, 'w')
# truncate the file if it already exists with data in
outputfile.truncate()
# write our data to a file
outputfile.write(json.dumps(final_json))
# close the filew
outputfile.close()
