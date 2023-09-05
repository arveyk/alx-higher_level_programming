In python, an Object Oriented Programming paradigm everything is Object
Data is presented as objects.
There are mutable and immutable types

 *-Mutable usually can have reference to the same object(aliasing) if one is
  assigned to the other
	*commom Mutables list, bytearry set dict, classes
 *-Immutable refence the same object if the are assigned the same value
	*common immutables 
	numbers: int, float, complexes, 
	sequeneces: str, tuple, bytes, frozen set
Language Reference Data model chapter:

Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.
