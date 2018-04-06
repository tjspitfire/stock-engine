# Copyright 2018, Todd L. Jarolimek II
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

possible_commands = []
word = ""

def call_to_possible_call_strings(*argv):
	# In this case, argv[0] is possible commands

	possible_call_strings = []
	word = ""
	for i,string in enumerate(argv[0]):
		for char in string:
			word += char
			possible_call_string.append(word)

	return possible_call_string

def construct_query(query_type, **kwargs):
	from time import strftime

	# calls = ["symbol", "query", "range"]
	# calls_dict = {}

	# for call in calls:
	# 	temp = call_to_possible_call_strings(call)
	# 	calls_dict[call] = temp

	# if kwargs:
	# 	for kwarg in kwargs:
	# 		for i,char in enumerate(kwarg):
	# 			# I need to parse the kwarg.
	# 			if i == 0:
	# 				check = char
	# 				for item in calls_dict.items():
	# 					if kwarg in item:
	# 						call = item[0]
	# 						call = calls_dict[call]
	# query_type = call
	st = "/stock/"
	ch = "/chart/"
	div = "/dividends/"
	mk = "/market/"
	lst = "/list/"
	lst = st + mk + lst
	spl = "/splits/"
	queryDB = {}
	queryDB["stock"] = {
	"book": "/book",
	# Omit following until I have a working prototype.
	"chart": {
		"5y": ch + "5y",
		"2y": ch + "2y",
		"1y": ch + "1y",
		"ytd": ch + "ytd",
		"6m": ch + "6m",
		"3m": ch + "3m",
		"1m": ch + "1m",
		"1d": ch + "1d",
		"today": ch + "/date/" + strftime("%Y%m%d"),
		# "date": ch + "/date/" + kwargs["date"],
		"dynamic": ch + "dynamic"
	},
	"company": "/company",
	"delayed-quote": "/delayed-quote",
	# Omit following until I have a working prototype.
	"dividends": {
		"5y": div + "5y",
		"2y": div + "2y",
		"1y": div + "1y",
		"ytd": div + "ytd",
		"6m": div + "6m",
		"3m": div + "3m",
		"1m": div + "1m"
	},
	"earnings": "/earnings",
	"effective-spread": "/effective-spread",
	"financials": "/financials",
	"stats": "/stats",
	"logo": "/logo",
	"news": "/news", # last 10 news items
	"ohlc": "/ohlc", # OHLC: Returns the official open and close for a give symbol.
	"peers": "/peers",
	"previous": "/previous",
	"price": "/price",
	"quote": "/quote",
	"relevant": "/relevant",
	# Omit following until I have a working prototype.
	"splits": {
		"5y": spl + "5y",
		"2y": spl + "2y",
		"1y": spl + "1y",
		"ytd": spl + "ytd",
		"6m": spl + "6m",
		"3m": spl + "3m",
		"1m": spl + "1m"
	},
	"time-series": "/time-series",
	"volume-by-venue": "/volume-by-venue"
	}

	queryDB["ref"] = "/ref-data/symbols"

	# omit until I have a working prototype
	queryDB["market"] = {
	"threshold-securities": st + mk + "threshold-securities", # day's data available at 20:30 daily
	"short-interest": st + "/ziext/short-interest",
	"list": {
		"mostactive": lst + "/mostactive",
		"gainers": lst + "/gainers",
		"losers": lst + "/losers",
		"iexvolume": lst + "iexvolume",
		"iexpercent": lst + "iexpercent"
	},
	"previous": st + mk + "/previous",
	"market": "/market" # This endpoint returns near real time traded volume on the markets
	}
	# onetimer
	
	require_range = ["chart", "dividends", "splits"]
	require_listtype = ["list"]

	# base_url = "https://api.iextrading.com/1.0"
	if query_type in queryDB["stock"]:
		symbol = kwargs["symbol"]
		query = st + symbol
		if query_type in require_range:
			_range = kwargs["range"]
			query += queryDB["stock"][query_type][_range]
		else:
			try:
				query += queryDB["stock"][query_type]
			except TypeError:
				print(json.dumps(queryDB["stock"][query_type]))

	elif query_type in queryDB["market"]:
		if query_type in require_listtype:
			query = queryDB["market"]["list"][kwargs["iexlist"]]
		else:
			query = queryDB["market"][query_type]

	elif query_type in queryDB["ref"]:
		query = queryDB["ref"]

	return query

def construct_path(pathv, project_path, folder_path, ext, **kwargs):
	"""
	THINGS TO ADD: 
		1. CHECK PROJECT_PATH, FOLDER_PATH IF EXISTS
		2. CHECK IF FULL PATH ALREADY EXISTS

	"""
	from time import strftime
	filename = "\\"
	for i,arg in enumerate(pathv):
		if i == (len(pathv) - 1):
			filename += pathv[i]
		else:
			filename += pathv[i] + "_"
	if kwargs:
		if kwargs["time"]:
			if kwargs["time"] == True:
				filename += strftime("%H%M%S")
		if kwargs["date"]:
			if kwargs["date"] == True:
				date= strftime("%Y%m%d")
				os.system("mkdir %(date)s")
				folder_path = folder_path + "\\" + date
				
	if list(ext)[0] != ".":
		ext = "." + ext
	PATH = project_path + folder_path + filename + ext
	return PATH

# def query_all_symbols(folder, query_type, **kwargs):
# 	from hawkeye import *
# 	symbol_path = "C:\\piex\\file\\stock"
# 	from os import system
# 	file_folder = "C:\\piex\\file"
# 	company_folder = file_folder + "\\company"
# 	stock_ref = pd.read_csv(file_folder + "\\ref.csv")
# 	symbols = stock_ref["symbol"]
# 	from piex import IEX
# 	import pandas as pd
# 	ranges = ["5y","2y","1y","ytd","6m","3m","1m","1d","today","dynamic"]
# 	for symbol in symbols:
# 		for rng in ranges:
# 			iex = IEX
# 			# get 3m data
# 			meta, data = iex.get(symbol=symbol,query="chart",range=rng)
# 			df = pd.DataFrame(data)
# 			folder = symbol
# 			pathname = construct_path([symbol,query,range], "C:\\piex", "\\file" + company_folder, ".csv")
# 			df.to_csv(pathname)
