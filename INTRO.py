
>>> x=10+10
>>> x
20
>>> Doe="python Student"
>>> doeg
Traceback (most recent call last):
  File "<python-input-3>", line 1, in <module>
    doeg
NameError: name 'doeg' is not defined. Did you mean: 'Doe'?
>>> doe
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    doe
NameError: name 'doe' is not defined. Did you mean: 'Doe'?
>>> Doe
'python Student'
>>> type(34.5)
<class 'float'>
>>> type("Samwel Doe")
<class 'str'>
>>> type("1345")
<class 'str'>
>>> type(1345)
<class 'int'>
>>> type(DOE)
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    type(DOE)
         ^^^
NameError: name 'DOE' is not defined. Did you mean: 'Doe'?
>>> type("DOE")
<class 'str'>
>>> type(Doe)
<class 'str'>
>>> type(x)
<class 'int'>
>>> y=900/12
>>> type(y)
<class 'float'>
>>> y=900/10
>>> type(y)
<class 'float'>
>>> z=900//10
>>> type(z)
<class 'int'>
>>> z
90
>>> print(z)
90
>>> y
90.0
>>> 900/12
75.0
>>> 900/13
69.23076923076923
>>> 900//13
69
>>>