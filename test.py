class FlatDict(dict):

	def __setitem__(self, key, item): 
		self.__dict__[key.lower()] = item

	def __getitem__(self, key):
		return self.__dict__[key.lower()]

	def __repr__(self): 
		return repr(self.__dict__)

	def __len__(self): 
		return len(self.__dict__)

	def __delitem__(self, key): 
		del self.__dict__[key.lower()]

	def keys(self): 
		return self.__dict__.keys()

	def values(self):
		return self.__dict__.values()

	def __cmp__(self, dict):
		return cmp(self.__dict__, dict)

	def __contains__(self, item):
		return item.lower() in self.__dict__

	def add(self, key, value):
		self.__dict__[key.lower()] = value

	def __iter__(self):
		return iter(self.__dict__)

	def __call__(self):
		return self.__dict__

	def __unicode__(self):
		return unicode(repr(self.__dict__))

	def get(self, key, default):
		return self.__dict__.get(key.lower(), default)
