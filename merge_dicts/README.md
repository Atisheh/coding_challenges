# task
Please write a function that merges two dictionaries. More specifically,
it should have the following signature:
```python
def merge(dict1, dict2, decision_func=None)
```
The two positional arguments are dictionaries, such as the following:
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
```
The result of calling the function ```merge(dict1, dict2)``` should be a new
dictionary that has all the keys of dict1 and dict2. In cases of collision, by
default, the value in the first argument should be used. Therefore, the result
of ```merge(dict1, dict2)``` would be the following:
```python
{"a": 1, "b": 2, "c": 4}
```
The third, optional argument ```decision_func``` is a function with two positional
arguments. When supplied, it should be used to create the values
for colliding keys. For example:
```python
def sum(x, y):
return x + y
merge(dict1, dict2, sum) == {"a": 1, "b": 5, "c": 4}
```
It would be great if you could add unit tests to the solution, so that the
code can be easily checked for correctness.

Bonus feature: If the values in the two dictionaries for the same key are
also dictionaries, they should also be merged.

# the solution
I especially wrote the decision_func_sum for the decision_func. When using the python builtin sum function it takes the two parameters as a list. I looked at some more builtin function and not every function takes a list for the parameters. Which is why I try to avoid these here. If people think they can just freely use them my code might break constantly.

Other than that I split up the code (and their tests) for the regular task and the bonus task.


#
(2017)
