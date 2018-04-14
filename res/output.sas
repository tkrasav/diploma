begin_version
3
end_version
begin_metric
0
end_metric
13
begin_variable
ExtVnfCpd1_status
-1
3
Atom status (ExtVnfCpd1, Initial)
Atom status (ExtVnfCpd1, Started)
Atom status (ExtVnfCpd1, Deleted)
end_variable
begin_variable
Vdu1
-1
4
Atom status (Vdu1, Initial)
Atom status (Vdu1, Created)
Atom status (Vdu1, Started)
Atom status (Vdu1, Deleted)
end_variable
begin_variable
VduCpd1
-1
3
Atom status (VduCpd1, Initial)
Atom status (VduCpd1, Started)
Atom status (VduCpd1, Deleted)
end_variable
begin_variable
VnfVl
-1
3
Atom status (VnfVl, Initial)
Atom status (VnfVl, Started)
Atom status (VnfVl, Deleted)
end_variable
begin_variable
VduCpd2
-1
3
Atom status (VduCpd2, Initial)
Atom status (VduCpd2, Started)
Atom status (VduCpd2, Deleted)
end_variable
begin_variable
Vdu2
-1
4
Atom status (Vdu2, Initial)
Atom status (Vdu2, Created)
Atom status (Vdu2, Started)
Atom status (Vdu2, Deleted)
end_variable
begin_variable
ExtVnfCpd2
-1
3
Atom status (ExtVnfCpd2, Initial)
Atom status (ExtVnfCpd2, Started)
Atom status (ExtVnfCpd2, Deleted)
end_variable
begin_variable
Vdu1ExtVnfCpd1
1
3
NegatedAtom VirtualBindsTo(Vdu1, ExtVnfCpd1)
Atom VirtualBindsTo(Vdu1, ExtVnfCpd1)
<null>
end_variable
begin_variable
Vdu1VduCpd1
1
3
NegatedAtom VirtualBindsTo(Vdu1, VduCpd1)
Atom VirtualBindsTo(Vdu1, VduCpd1)
<null>
end_variable
begin_variable
VduCpd1VnfVl
1
3
NegatedAtom VirtualLinksTo(VduCpd1, VnfVl)
Atom VirtualLinksTo(VduCpd1, VnfVl)
<null>
end_variable
begin_variable
VduCpd2VnfVl
1
3
NegatedAtom VirtualLinksTo(VduCpd2, VnfVl)
Atom VirtualLinksTo(VduCpd2, VnfVl)
<null>
end_variable
begin_variable
Vdu2VduCpd2
1
3
NegatedAtom VirtualBindsTo(Vdu2, VduCpd2)
Atom VirtualBindsTo(Vdu2, VduCpd2)
<null>
end_variable
begin_variable
Vdu2ExtVnfCpd2
1
3
NegatedAtom VirtualBindsTo(Vdu2, ExtVnfCpd2)
Atom VirtualBindsTo(Vdu2, ExtVnfCpd2)
<null>
end_variable
0
begin_state
0
0
0
0
0
0
0
0
0
0
0
0
0
end_state
begin_goal
13
0 1
1 2
2 1
3 1
4 1
5 2
6 1
7 1
8 1
9 1
10 1
11 1
12 1
end_goal
16
begin_operator
create_vm Vdu1
3
1 0
7 1
8 1
1
0 1 0 1
1
end_operator
begin_operator
configure_vm Vdu1
3
1 1
7 1
8 1
1
0 1 1 2
1
end_operator
begin_operator
delete_vm Vdu1
3
1 2
7 1
8 1
1
0 1 2 3 
1
end_operator
begin_operator
create_cp ExtVnfCpd11
1
0 0
1
0 0 0 1
1
end_operator
begin_operator
delete_cp ExtVnfCpd11
1
0 1
1
0 0 1 2
1
end_operator
begin_operator
create_cp VduCpd1
2
2 0
9 1
1
0 2 0 1
1
end_operator
begin_operator
delete_cp VduCpd1
2
2 1
9 1
1
0 2 1 2
1
end_operator
begin_operator
create_vl VnfVl
1
3 0
1
0 3 0 1
1
end_operator
begin_operator
delete_vl VnfVl
1
3 1
1
0 3 1 2
1
end_operator
begin_operator
create_cp VduCpd2
2
4 0
10 1
1
0 4 0 1
1
end_operator
begin_operator
delete_cp VduCpd2
2
4 1
10 1
1
0 4 1 2
1
end_operator
begin_operator
create_cp ExtVnfCpd12
1
6 0
1
0 6 0 1
1
end_operator
begin_operator
delete_cp ExtVnfCpd12
1
6 1
1
0 6 1 2
1
end_operator
begin_operator
create_vm Vdu2
3
5 0
11 1
12 1
1
0 5 0 1
1
end_operator
begin_operator
configure_vm Vdu2
3
5 1
11 1
12 1
1
0 5 1 2
1
end_operator
begin_operator
delete_vm Vdu2
3
5 2
11 1
12 1
1
0 5 2 3 
1
end_operator
12
begin_rule
1
0 1
7 0 1
end_rule
begin_rule
1
2 1
8 0 1
end_rule
begin_rule
1
3 1
9 0 1
end_rule
begin_rule
1
3 1
10 0 1
end_rule
begin_rule
1
4 1
11 0 1
end_rule
begin_rule
1
6 1
12 0 1
end_rule
begin_rule
1
0 2
7 1 2
end_rule
begin_rule
1
2 2
8 1 2
end_rule
begin_rule
1
3 2
9 1 2
end_rule
begin_rule
1
3 2
10 1 2
end_rule
begin_rule
1
4 2
11 1 2
end_rule
begin_rule
1
6 2
12 1 2
end_rule