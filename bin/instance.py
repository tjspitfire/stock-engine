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


class Instance:
	def __init__(self, obj):
		from eagle1 import date, time
		self.obj = obj
		self.timestamp = (date(), time())
		self.type = type(obj)
		if self.type == type("") or self.type == type({}):
			self.items = self.obj.items()
		self.key = ("Instance", self.timestamp)

		# self.index = self.data[0]
		# self.values = self.data[1]

		# def marshal(self):
		# 	import marshal
		# 	import tempfile
		# 	tempfile = tempfile.mkstemp()
		# 	with open(tempfile, "wb") as file:
		# 		marshal.dump(self, file)

	def print(self):
		def obj(self):
			if self.type == type({}):
				import json
				return print(json.dumps(self.obj, sort_keys=True, indent=2))
			else:
				return print(self.item))	def post(self):
		from google.cloud import datastore
		import google.cloud.exceptions
		# keys = self.datastore.keys()
		datastore_client = datastore.Client()
		ds = datastore.Entity(key=self.key)
		ds.insert(self)