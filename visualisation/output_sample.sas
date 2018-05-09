begin_version
3
end_version
begin_metric
0
end_metric
7
begin_variable
ExtVnfCpd1_status
-1
3
Atom value (ExtVnfCpd1, Created)
Atom value (ExtVnfCpd1, Deleted)
Atom value (ExtVnfCpd1, Initial)
end_variable
begin_variable
Vdu1_status
-1
4
Atom value (Vdu1, Created)
Atom value (Vdu1, Deleted)
Atom value (Vdu1, Initial)
Atom value (Vdu1, Started)
end_variable
begin_variable
VduCpd1_status
-1
3
Atom value (VduCpd1, Created)
Atom value (VduCpd1, Deleted)
Atom value (VduCpd1, Initial)
end_variable
begin_variable
VnfVl_status
-1
3
Atom value (VnfVl, Created)
Atom value (VnfVl, Deleted)
Atom value (VnfVl, Initial)
end_variable
begin_variable
VduCpd2_status
-1
3
Atom value (VduCpd2, Created)
Atom value (VduCpd2, Deleted)
Atom value (VduCpd2, Initial)
end_variable
begin_variable
Vdu2_status
-1
4
Atom value (Vdu2, Created)
Atom value (Vdu2, Deleted)
Atom value (Vdu2, Initial)
Atom value (Vdu2, Started)
end_variable
begin_variable
ExtVnfCpd2_status
-1
3
Atom value (ExtVnfCpd2, Created)
Atom value (ExtVnfCpd2, Deleted)
Atom value (ExtVnfCpd2, Initial)
end_variable
0
begin_state
2
2
2
2
2
2
2
end_state
begin_goal
7
0 0
1 3
2 0
3 0
4 0
5 3
6 0
end_goal
16
begin_operator
create ExtVnfCpd1
1
0 2
1
0 0 -1 0
1
end_operator
begin_operator
delete ExtVnfCpd1
2
0 0
1 1
1
0 0 -1 1
1
end_operator
begin_operator
create Vdu1
3
1 2
0 0
2 0
1
0 1 -1 0
1
end_operator
begin_operator
configure Vdu1
1
1 0
1
0 1 -1 3
1
end_operator
begin_operator
delete Vdu1
1
1 0
1
0 1 -1 1
1
end_operator
begin_operator
create VduCpd1
2
2 2
3 0
1
0 2 -1 0
1
end_operator
begin_operator
delete VduCpd1
2
2 0
1 1
1
0 2 -1 1
1
end_operator
begin_operator
create VnfVl
1
3 2
1
0 3 -1 0
1
end_operator
begin_operator
delete VnfVl
3
3 0
2 1
4 1
1
0 3 -1 1
1
end_operator
begin_operator
create VduCpd2
2
4 2
3 0
1
0 4 -1 0
1
end_operator
begin_operator
delete VduCpd2
2
4 0
5 1
1
0 4 -1 1
1
end_operator
begin_operator
create Vdu2
3
5 2
6 0
4 0
1
0 5 -1 0
1
end_operator
begin_operator
configure Vdu2
1
5 0
1
0 5 -1 3
1
end_operator
begin_operator
delete Vdu2
1
5 0
1
0 5 -1 1
1
end_operator
begin_operator
create ExtVnfCpd2
1
6 2
1
0 6 -1 0
1
end_operator
begin_operator
delete ExtVnfCpd2
2
6 0
5 1
1
0 6 -1 1
1
end_operator
