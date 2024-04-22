Implement a backtracking search which takes a CSP and finds a valid assignment for all the
variables in the CSP, if one exists. It should leverage your AC-3 implementation to maintain
arc consistency. When Choosing a variable to assign, it should use your minimum remaining
values heuristic implementation. Along with the solution to the CSP, your search should return
the order in which it assigned the variables, and the domains of the remaining unassigned
variables after each assignment. For each variable, keep track of any failed values that it had to
backtrack for. You’ll probably also want to do some book keeping to keep track of, for each variable, how many previous variables required at least one backtrack to find the correct value.

- Inputs:
  

1. **csp (dict):**
```python
csp = {
'variables' : {
    Tile ID (str) : [vals (int)],
}
,
'constraints' : {
    (ID1 (str), ID2 (str)): [(val1 (int), val2 (int)),],
```
2. **Assignments (dict):**
   
   Tracks the assigned values

   **Update Instructions:** Add current val for current var when it only has one val left in domain
```python
assigments = 
{
  Tile ID (str) : value (int)
}
```

1. **Assignment Order (list):**
```python
order = [ID1 (Str), ...]
```
1. **Unnassigned Domains (dict):**
   
   Tracks the domains of each unassgined Tile

   **Update Instructions:** Add updated domains from CSP when a new variable is succesfully assigned 

```python
domains = 
{
  Tile ID (str) : [vals (int)],
}
```
1. **Failed Values (dict):**
   
   Keeps track of values that lead to an inconsistent domain space.

   **Update Instructions:** Add current Val for Current Tile when AC3 returns False
```python
failed =
{
  Tile ID (str) : [vals (int)],
}

