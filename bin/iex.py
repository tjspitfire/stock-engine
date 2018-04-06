# # #
# Copyright 2018, Todd L. Jarolimek II
#
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
# # #
# Data provided for free by IEX<https://iextrading.com/developer>.
# # #
# WORKING AS OF: 04/06/2018 08:30
# # #
class IEX:

	def __init__(self):
		self._dat = {}

	def get(self, query, **kwargs):
		from eagle1 import get_data
		from iexutils import construct_query
		import json

		_url = "https://api.iextrading.com/1.0" + construct_query(query, **kwargs)
		self._dat = get_data(_url)

		return self._dat