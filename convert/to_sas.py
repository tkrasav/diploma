from typing import List
import structure
from enum import Enum
import itertools


class Indicator(Enum):
	ATTRIBUTE = -1
	REFERENCE = 1


class Status:
	def __init__(self, name: str, status: str, prefix: str = ""):
		self.name = name
		self.status = status
		self.prefix = prefix

	def __repr__(self):
		return self.__str__()

	def __hash__(self):
		return hash((self.name, self.status))

	def __eq__(self, other):
		return self.name == other.name and self.status == other.status


class AtomStatus(Status):
	def __str__(self):
		name = self.name
		status = self.status
		if self.name is None:
			name = 'None'
		if self.status is None:
			status = 'None'
		return "Atom value (" + name + ", " + status + ")"


class BindStatus(Status):
	def __str__(self):
		name = self.name
		status = self.status
		if self.name is None and self.status is None and self.prefix is None:
			return "<null>"
		return self.prefix + "(" + name + ", " + status + ")"


class Variable:
	def __init__(self, name: str, indicator: Enum, values: List[Status]):
		self.name = name
		self.indicator = Indicator(indicator)
		self.len = len(values)
		self.values = values

	def __str__(self):
		return self.values.__str__()

	def __repr__(self):
		return self.values.__str__()


def generate_sas(nodes: List[structure.Node]) -> dict:
	output = {'state': []}
	for node in nodes:
		for attr in node.attributes.__dict__.keys():
			values = set()
			values.add(AtomStatus(node.uid, node.attributes.get(attr)))
			for interface in node.interfaces:
				if attr in interface.condition.__dict__.keys():
					values.add(
						AtomStatus(node.uid, interface.condition.get(attr))
					)
				if attr in interface.effect.__dict__.keys():
					values.add(
						AtomStatus(node.uid, interface.effect.get(attr))
					)
			values = list(values)
			values.sort(key=lambda i: i.status)
			output[node.uid + "_" + attr] = \
				Variable(node.uid + "_" + attr, Indicator.ATTRIBUTE, values)
			output["state"].append(values.index(AtomStatus(node.uid, node.attributes.get(attr))))
		for reference in node.references:
			values = list()
			values.append(BindStatus(node.uid, reference.target_node, "NegatedAtom DependsOn"))
			values.append(BindStatus(node.uid, reference.target_node, "Atom DependsOn"))
			values.append(BindStatus(None,     None,                  None))
			output[node.uid + "_" + reference.target_node] = \
				Variable(node.uid + "_" + reference.target_node, Indicator.REFERENCE, values)
			output["state"].append(0)
	return output


start_state = structure.parse('../res/current.json')
out = generate_sas(start_state)
target_state = structure.parse('../res/target.json')
file = open("output_sample.sas", "w+")
for key in out:
	if key == "state":
		continue
	var = out[key]
	statuses = "".join(i.__str__() + "\n" for i in var.values)
	file.write(
		"begin_variable\n" +
		var.name + "\n" +
		str(var.indicator.value) + "\n" +
		str(var.len) + "\n" +
		statuses +
		"end_variable\n"
	)

state_ids = "".join(
	str(st) + "\n" for st in out["state"]
)
file.write(
	"begin_state\n" +
	state_ids +
	"end_state\n"
)
print(out)