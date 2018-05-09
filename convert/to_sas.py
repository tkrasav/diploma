from typing import List
import structure
from enum import Enum
import itertools
import time
from collections import namedtuple

def millis():
    return int(round(time.time() * 1000))


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


class Condition:
	def __init__(self, variable_index: int, value_index: int):
		self.variable_index = variable_index
		self.value_index = value_index

	def __str__(self):
		return self.variable_index.__str__() + " " + self.value_index.__str__()

	def __repr__(self):
		return self.variable_index.__str__() + " " + self.value_index.__str__()


class Effect:
	def __init__(self, optional_effect: int, variable_index: int, smth: int, value_index: int):
		self.optional_effect = optional_effect
		self.variable_index = variable_index
		self.value_index = value_index
		self.smth = smth

	def __str__(self):
		return self.optional_effect.__str__() + " " + self.variable_index.__str__() + " " \
		       + self.smth.__str__() + " " + self.value_index.__str__()

	def __repr__(self):
		return self.optional_effect.__str__() + " " + self.variable_index.__str__() + " " \
		       + self.smth.__str__() + " " + self.value_index.__str__()


class Operator:
	def __init__(
			self, name: str,
			conditions: List[Condition],
			effects: List[Effect]
	):
		self.name = name
		self.conditions = conditions
		self.len = len(effects)
		self.effects = effects

	def __str__(self):
		return self.conditions.__str__()

	def __repr__(self):
		return self.conditions.__str__()

	def add_condition(self, condition: Condition):
		self.conditions.append(condition)

	def add_effect(self, effect: Effect):
		self.effects.append(effect)


def generate_sas(nodes: List[structure.Node]) -> dict:
	output = {'state': [], 'variables': {}, 'operators': {}, "timer": {"start": time.time(), "end": 0}}
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
			output['variables'][node.uid + "_" + attr] = \
				Variable(node.uid + "_" + attr, Indicator.ATTRIBUTE, values)
			output['state'].append(values.index(AtomStatus(node.uid, node.attributes.get(attr))))

	# Suppose that at following code order of Variables wouldn't change.
	order = list(output['variables'].keys())

	node_map = {}
	for node in nodes:
		node_map[node.uid] = node

	for node in nodes:
		for interface in node.interfaces:
			output['operators'][interface.name + " " + node.uid] = Operator(interface.name + " " + node.uid, [], [])
			for variable_name in interface.condition.__dict__.keys():
				output['operators'][interface.name + " " + node.uid].add_condition(
					Condition(
						order.index(node.uid + "_" + variable_name),
						output['variables'][node.uid + "_" + variable_name].values.index(
							AtomStatus(node.uid, interface.condition.__dict__[variable_name]))
					))
			for variable_name in interface.effect.__dict__.keys():
				output['operators'][interface.name + " " + node.uid].add_effect(
					Effect(
						0,
						order.index(node.uid + "_" + variable_name),
						-1,
						output['variables'][node.uid + "_" + variable_name].values.index(
							AtomStatus(node.uid, interface.effect.__dict__[variable_name]))
					))

	for node in nodes:
		for reference in node.references:
			for interface in node.interfaces:
				if interface.effect.get("status") == "Created":
					output['operators'][interface.name + " " + node.uid].add_condition(
						Condition(
							order.index(reference.target_node + "_status"),
							output['variables'][reference.target_node + "_status"].values.index(
								AtomStatus(reference.target_node, "Created"))
						)
					)
					target_node = node_map[reference.target_node]
					for target_interface in target_node.interfaces:
						if target_interface.effect.get("status") == "Deleted":
							output['operators'][target_interface.name + " " + reference.target_node].add_condition(
								Condition(
									order.index(node.uid + "_status"),
									output['variables'][node.uid + "_status"].values.index(
										AtomStatus(node.uid, "Deleted"))
								)
							)

	# for reference in node.references:
	# 	values = list()
	# 	values.append(BindStatus(node.uid, reference.target_node, "NegatedAtom DependsOn"))
	# 	values.append(BindStatus(node.uid, reference.target_node, "Atom DependsOn"))
	# 	values.append(BindStatus(None,     None,                  None))
	# 	output[node.uid + "_" + reference.target_node] = \
	# 		Variable(node.uid + "_" + reference.target_node, Indicator.REFERENCE, values)
	# 	output["state"].append(0)
	output["timer"]["end"] = time.time()
	return output


def probe():
	start_time = time.time()
	start_state = structure.parse('../res/current.json')
	out = generate_sas(start_state)
	target_state = structure.parse('../res/target.json')
	goal = generate_sas(target_state)
	file = open("output_sample.sas", "w+")
	file.write(
		"begin_version\n" +
		str(3) + "\n" +
		"end_version\n" +
		"begin_metric\n" +
		str(0) + "\n" +
		"end_metric\n" +
		str(len(out['variables'])) + "\n"
	)
	for key in out['variables']:
		var = out['variables'][key]
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
		"0\n" +
		"begin_state\n" +
		state_ids +
		"end_state\n"
	)

	order = list(out['variables'].keys())
	order_target = list(goal['variables'].keys())
	goal_ids = ""
	for key in out['variables']:
		if key == "state":
			continue
		current_var = out['variables'][key]
		target_var = goal['variables'][key]
		goal_ids += str(order.index(key)) + " " + str(goal["state"][order_target.index(key)]) + "\n"
	file.write(
		"begin_goal\n" +
		str(len(out['variables'])) + "\n" +
		goal_ids +
		"end_goal\n"
	)
	file.write(
		str(len(out['operators'])) + "\n"
	)
	for key in out['operators']:
		operator = out['operators'][key]
		conditions = "".join(
			str(cond) + "\n" for cond in operator.conditions
		)
		effects = "".join(
			str(eff) + "\n" for eff in operator.effects
		)
		file.write(
			"begin_operator\n" +
			operator.name + "\n" +
			str(len(operator.conditions)) + "\n" +
			conditions +
			str(len(operator.effects)) + "\n" +
			effects +
			"1\n" +
			"end_operator\n"
		)
	done_time = time.time()
	timer = namedtuple("timer", ["start", "end"])
	return timer(start_time, done_time)


def write_sas(filename: str, current_out: dict, target_out: dict):
	file = open(filename, "w+")
	file.write(
		"begin_version\n" +
		str(3) + "\n" +
		"end_version\n" +
		"begin_metric\n" +
		str(0) + "\n" +
		"end_metric\n" +
		str(len(current_out['variables'])) + "\n"
	)
	for key in current_out['variables']:
		var = current_out['variables'][key]
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
		str(st) + "\n" for st in current_out["state"]
	)
	file.write(
		"0\n" +
		"begin_state\n" +
		state_ids +
		"end_state\n"
	)

	order = list(current_out['variables'].keys())
	order_target = list(target_out['variables'].keys())
	goal_ids = ""
	for key in current_out['variables']:
		if key == "state":
			continue
		goal_ids += str(order.index(key)) + " " + str(target_out["state"][order_target.index(key)]) + "\n"
	file.write(
		"begin_goal\n" +
		str(len(current_out['variables'])) + "\n" +
		goal_ids +
		"end_goal\n"
	)
	file.write(
		str(len(current_out['operators'])) + "\n"
	)
	for key in current_out['operators']:
		operator = current_out['operators'][key]
		conditions = "".join(
			str(cond) + "\n" for cond in operator.conditions
		)
		effects = "".join(
			str(eff) + "\n" for eff in operator.effects
		)
		file.write(
			"begin_operator\n" +
			operator.name + "\n" +
			str(len(operator.conditions)) + "\n" +
			conditions +
			str(len(operator.effects)) + "\n" +
			effects +
			"1\n" +
			"end_operator\n"
		)


import random
import copy

start_state = structure.parse('../res/current.json')
how_many_nodes_need = 10
base_name = start_state[0].uid
for i in range(how_many_nodes_need):
	base_node = copy.deepcopy(start_state[0])

	base_node.uid = base_node.uid + str(i)
	where_choose = list(range(how_many_nodes_need))
	where_choose.remove(i)
	how_many_refs = random.choice([1, 2, 3])
	rand = random.sample(where_choose, how_many_refs)
	base_node.references = []
	for reference in list(rand):
		base_node.references.append(
			structure.Reference.get_instance(base_name + str(reference), ["tosca.relationships.DependsOn"])
		)

	start_state.append(base_node)
out = generate_sas(start_state)
print(start_state)
print(out)
