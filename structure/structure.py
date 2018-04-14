import json
import os
import sys
import traceback
from typing import List

sys.path.append(os.getcwd()[0])


class Attributes:
	def __init__(self, arg: dict):
		if type(arg) is not dict:
			raise IOError
		try:
			self.__dict__ = arg
			self.status = arg['status']
			if type(self.status) is not str:
				raise ValueError
		except Exception:
			raise ValueError().with_traceback(sys.exc_info()[2])

	def get(self, attr_name: str):
		return self.__dict__[attr_name]


class Interface:
	def __init__(self, arg: dict):
		self.name = arg['name']
		if type(self.name) is not str:
			raise ValueError
		self.condition = Attributes(arg['condition'])
		self.effect = Attributes(arg['effect'])


class Reference:
	def __init__(self, arg):
		self.target_node = arg['target_node']
		if type(self.target_node) is not str:
			raise ValueError
		self.relationship_types = arg['relationship_types']
		if type(self.relationship_types) is not list:
			raise ValueError("Relationship types is not a list.").with_traceback(sys.exc_info()[2])


class Node:
	def __init__(self, arg: dict):
		try:
			self.uid = arg['uid']
			if type(self.uid) is not str:
				raise ValueError

			self.types = arg['types']
			if type(self.types) is not list:
				raise ValueError

			self.attributes = Attributes(arg['attributes'])
			if type(self.attributes) is not Attributes:
				raise ValueError

			self.references = list()
			if type(arg['references']) is not list:
				raise ValueError
			else:
				for ref in arg['references']:
					self.references.append(Reference(ref))

			self.interfaces = list()
			if type(arg['interfaces']) is not list:
				raise ValueError
			else:
				for ref in arg['interfaces']:
					self.interfaces.append(Interface(ref))
		except Exception as err:
			traceback.print_exception(type(err).__name__,
			                          ValueError("Problematic Uid: " + self.uid + "\n"),
			                          sys.exc_info()[2], chain=True)

	def __str__(self):
		return self.uid

	def __repr__(self):
		return self.uid


def parse(input_file: str) -> List[Node]:
	file = open(input_file, 'r+')
	arr = json.load(file)
	ret = list()
	for obj in arr:
		ret.append(Node(obj))
	return ret
