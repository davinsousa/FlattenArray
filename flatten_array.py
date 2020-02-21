def flatten(iterable):


	if iterable[0] is None:
		if len(iterable)==1: #if it is the last element of the list and is NULL, return nothing
			return []
		else:
			return flatten(iterable[1:]) #if it is NULL but not the last element, than ignore this element and call the function for rest of elements
	else:
		if type(iterable[0]) is list:
			if len(iterable)==1: #if it is a list and the last element, than call the function for this element (list)
				return flatten(iterable[0])
			else:
				return flatten(iterable[0])+flatten(iterable[1:]) #if not the last element, than call the function for this element and the rest
		else:
			if len(iterable)==1:
				return [iterable[0]] #if not a list but it is the last element, just return the element
			else:
				return [iterable[0]]+flatten(iterable[1:]) #if not a list and also not the last element, return the element + the function for the rest 






