#  >>> fac(n)
#  Traceback (most recent call last):
#  / File "<pyshell#0>", line 1, in <module>
#   /  fac(n)
# /NameError: name 'fac' is not defined

# >>> from math import factorial
# >>> fac(n)
# /Traceback (most recent call last):
#  / File "<pyshell#2>", line 1, in <module>
#   /  fac(n)
# /NameError: name 'fac' is not defined

# >>> from math import factorial as fac
# >>> fac(n)
# /Traceback (most recent call last):
#  / File "<pyshell#4>", line 1, in <module>
#   /  fac(n)
# /NameError: name 'n' is not defined

# >>> n=100
# >>> fac(n)
# 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
 
# >>> len(str(fac(n)))
# 158
# >>> 
# >>> 
# >>> from math import factorial as fac
# >>> n = 100
# >>> k = 2
# >>> fac(n) // (fac(k) * fac(n - k))
# 4950
# >>> fac(n)
# 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
# >>> len(str(fac(n)))
# 158
# >>> import zen
# Traceback (most recent call last):
#   File "<pyshell#18>", line 1, in <module>
#     import zen
# ModuleNotFoundError: No module named 'zen'
# >>> import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# >>> 0b10
# 2
# >>> # Binary int
# >>> 0o10
# 8
# >>> #octo int
# >>> 0x10
# 16
# >>> # Exadecimal int
# >>> # FLOAT
# >>> 3.125
# 3.125
# >>> 3E8
# 300000000.0
# >>> 1.616E-35
# 1.616e-35
# >>> float(7)
# 7.0
# >>> float("1.618")
# 1.618
# >>> float("nan")
# nan
# >>> float("inf")
# inf
# >>> float("-inf) # minus infinite
      
# SyntaxError: EOL while scanning string literal
# >>> float("-inf")
# -inf
# >>> 3.0 + 1
# 4.0
# >>> if bool("eggs"):
# 	print("Yes please!")

	
# Yes please!
# >>> if "eggs":
# 	print("Yes please!")

	
# Yes please!
# >>> while true:
# 	response = input()
# 	if int(response) % 7 == 0:
# 		break

	
# Traceback (most recent call last):
#   File "<pyshell#47>", line 1, in <module>
#     while true:
# NameError: name 'true' is not defined
# >>> while true:
# 	response = input()
# 	if int(response) % 7 == 0:
# 		break
# 	12
# 	67
# 	34
# 	28

	
# Traceback (most recent call last):
#   File "<pyshell#53>", line 1, in <module>
#     while true:
# NameError: name 'true' is not defined
# >>> c = "oslo"
# >>> c
# 'oslo'
# >>> c.capitalize()
# 'Oslo'
# >>> c
# 'oslo'
# >>> help(str)
# Help on class str in module builtins:

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |  
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.
#  |  
#  |  Methods defined here:
#  |  
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |  
#  |  __contains__(self, key, /)
#  |      Return key in self.
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __format__(self, format_spec, /)
#  |      Return a formatted version of the string as described by format_spec.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __getitem__(self, key, /)
#  |      Return self[key].
#  |  
#  |  __getnewargs__(...)
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __hash__(self, /)
#  |      Return hash(self).
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __mod__(self, value, /)
#  |      Return self%value.
#  |  
#  |  __mul__(self, value, /)
#  |      Return self*value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |  
#  |  __rmod__(self, value, /)
#  |      Return value%self.
#  |  
#  |  __rmul__(self, value, /)
#  |      Return value*self.
#  |  
#  |  __sizeof__(self, /)
#  |      Return the size of the string in memory, in bytes.
#  |  
#  |  __str__(self, /)
#  |      Return str(self).
#  |  
#  |  capitalize(self, /)
#  |      Return a capitalized version of the string.
#  |      
#  |      More specifically, make the first character have upper case and the rest lower
#  |      case.
#  |  
#  |  casefold(self, /)
#  |      Return a version of the string suitable for caseless comparisons.
#  |  
#  |  center(self, width, fillchar=' ', /)
#  |      Return a centered string of length width.
#  |      
#  |      Padding is done using the specified fill character (default is a space).
#  |  
#  |  count(...)
#  |      S.count(sub[, start[, end]]) -> int
#  |      
#  |      Return the number of non-overlapping occurrences of substring sub in
#  |      string S[start:end].  Optional arguments start and end are
#  |      interpreted as in slice notation.
#  |  
#  |  encode(self, /, encoding='utf-8', errors='strict')
#  |      Encode the string using the codec registered for encoding.
#  |      
#  |      encoding
#  |        The encoding in which to encode the string.
#  |      errors
#  |        The error handling scheme to use for encoding errors.
#  |        The default is 'strict' meaning that encoding errors raise a
#  |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
#  |        'xmlcharrefreplace' as well as any other name registered with
#  |        codecs.register_error that can handle UnicodeEncodeErrors.
#  |  
#  |  endswith(...)
#  |      S.endswith(suffix[, start[, end]]) -> bool
#  |      
#  |      Return True if S ends with the specified suffix, False otherwise.
#  |      With optional start, test S beginning at that position.
#  |      With optional end, stop comparing S at that position.
#  |      suffix can also be a tuple of strings to try.
#  |  
#  |  expandtabs(self, /, tabsize=8)
#  |      Return a copy where all tab characters are expanded using spaces.
#  |      
#  |      If tabsize is not given, a tab size of 8 characters is assumed.
#  |  
#  |  find(...)
#  |      S.find(sub[, start[, end]]) -> int
#  |      
#  |      Return the lowest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |      
#  |      Return -1 on failure.
#  |  
#  |  format(...)
#  |      S.format(*args, **kwargs) -> str
#  |      
#  |      Return a formatted version of S, using substitutions from args and kwargs.
#  |      The substitutions are identified by braces ('{' and '}').
#  |  
#  |  format_map(...)
#  |      S.format_map(mapping) -> str
#  |      
#  |      Return a formatted version of S, using substitutions from mapping.
#  |      The substitutions are identified by braces ('{' and '}').
#  |  
#  |  index(...)
#  |      S.index(sub[, start[, end]]) -> int
#  |      
#  |      Return the lowest index in S where substring sub is found, 
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |      
#  |      Raises ValueError when the substring is not found.
#  |  
#  |  isalnum(self, /)
#  |      Return True if the string is an alpha-numeric string, False otherwise.
#  |      
#  |      A string is alpha-numeric if all characters in the string are alpha-numeric and
#  |      there is at least one character in the string.
#  |  
#  |  isalpha(self, /)
#  |      Return True if the string is an alphabetic string, False otherwise.
#  |      
#  |      A string is alphabetic if all characters in the string are alphabetic and there
#  |      is at least one character in the string.
#  |  
#  |  isascii(self, /)
#  |      Return True if all characters in the string are ASCII, False otherwise.
#  |      
#  |      ASCII characters have code points in the range U+0000-U+007F.
#  |      Empty string is ASCII too.
#  |  
#  |  isdecimal(self, /)
#  |      Return True if the string is a decimal string, False otherwise.
#  |      
#  |      A string is a decimal string if all characters in the string are decimal and
#  |      there is at least one character in the string.
#  |  
#  |  isdigit(self, /)
#  |      Return True if the string is a digit string, False otherwise.
#  |      
#  |      A string is a digit string if all characters in the string are digits and there
#  |      is at least one character in the string.
#  |  
#  |  isidentifier(self, /)
#  |      Return True if the string is a valid Python identifier, False otherwise.
#  |      
#  |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
#  |      "class".
#  |  
#  |  islower(self, /)
#  |      Return True if the string is a lowercase string, False otherwise.
#  |      
#  |      A string is lowercase if all cased characters in the string are lowercase and
#  |      there is at least one cased character in the string.
#  |  
#  |  isnumeric(self, /)
#  |      Return True if the string is a numeric string, False otherwise.
#  |      
#  |      A string is numeric if all characters in the string are numeric and there is at
#  |      least one character in the string.
#  |  
#  |  isprintable(self, /)
#  |      Return True if the string is printable, False otherwise.
#  |      
#  |      A string is printable if all of its characters are considered printable in
#  |      repr() or if it is empty.
#  |  
#  |  isspace(self, /)
#  |      Return True if the string is a whitespace string, False otherwise.
#  |      
#  |      A string is whitespace if all characters in the string are whitespace and there
#  |      is at least one character in the string.
#  |  
#  |  istitle(self, /)
#  |      Return True if the string is a title-cased string, False otherwise.
#  |      
#  |      In a title-cased string, upper- and title-case characters may only
#  |      follow uncased characters and lowercase characters only cased ones.
#  |  
#  |  isupper(self, /)
#  |      Return True if the string is an uppercase string, False otherwise.
#  |      
#  |      A string is uppercase if all cased characters in the string are uppercase and
#  |      there is at least one cased character in the string.
#  |  
#  |  join(self, iterable, /)
#  |      Concatenate any number of strings.
#  |      
#  |      The string whose method is called is inserted in between each given string.
#  |      The result is returned as a new string.
#  |      
#  |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
#  |  
#  |  ljust(self, width, fillchar=' ', /)
#  |      Return a left-justified string of length width.
#  |      
#  |      Padding is done using the specified fill character (default is a space).
#  |  
#  |  lower(self, /)
#  |      Return a copy of the string converted to lowercase.
#  |  
#  |  lstrip(self, chars=None, /)
#  |      Return a copy of the string with leading whitespace removed.
#  |      
#  |      If chars is given and not None, remove characters in chars instead.
#  |  
#  |  partition(self, sep, /)
#  |      Partition the string into three parts using the given separator.
#  |      
#  |      This will search for the separator in the string.  If the separator is found,
#  |      returns a 3-tuple containing the part before the separator, the separator
#  |      itself, and the part after it.
#  |      
#  |      If the separator is not found, returns a 3-tuple containing the original string
#  |      and two empty strings.
#  |  
#  |  replace(self, old, new, count=-1, /)
#  |      Return a copy with all occurrences of substring old replaced by new.
#  |      
#  |        count
#  |          Maximum number of occurrences to replace.
#  |          -1 (the default value) means replace all occurrences.
#  |      
#  |      If the optional argument count is given, only the first count occurrences are
#  |      replaced.
#  |  
#  |  rfind(...)
#  |      S.rfind(sub[, start[, end]]) -> int
#  |      
#  |      Return the highest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |      
#  |      Return -1 on failure.
#  |  
#  |  rindex(...)
#  |      S.rindex(sub[, start[, end]]) -> int
#  |      
#  |      Return the highest index in S where substring sub is found,
#  |      such that sub is contained within S[start:end].  Optional
#  |      arguments start and end are interpreted as in slice notation.
#  |      
#  |      Raises ValueError when the substring is not found.
#  |  
#  |  rjust(self, width, fillchar=' ', /)
#  |      Return a right-justified string of length width.
#  |      
#  |      Padding is done using the specified fill character (default is a space).
#  |  
#  |  rpartition(self, sep, /)
#  |      Partition the string into three parts using the given separator.
#  |      
#  |      This will search for the separator in the string, starting at the end. If
#  |      the separator is found, returns a 3-tuple containing the part before the
#  |      separator, the separator itself, and the part after it.
#  |      
#  |      If the separator is not found, returns a 3-tuple containing two empty strings
#  |      and the original string.
#  |  
#  |  rsplit(self, /, sep=None, maxsplit=-1)
#  |      Return a list of the words in the string, using sep as the delimiter string.
#  |      
#  |        sep
#  |          The delimiter according which to split the string.
#  |          None (the default value) means split according to any whitespace,
#  |          and discard empty strings from the result.
#  |        maxsplit
#  |          Maximum number of splits to do.
#  |          -1 (the default value) means no limit.
#  |      
#  |      Splits are done starting at the end of the string and working to the front.
#  |  
#  |  rstrip(self, chars=None, /)
#  |      Return a copy of the string with trailing whitespace removed.
#  |      
#  |      If chars is given and not None, remove characters in chars instead.
#  |  
#  |  split(self, /, sep=None, maxsplit=-1)
#  |      Return a list of the words in the string, using sep as the delimiter string.
#  |      
#  |      sep
#  |        The delimiter according which to split the string.
#  |        None (the default value) means split according to any whitespace,
#  |        and discard empty strings from the result.
#  |      maxsplit
#  |        Maximum number of splits to do.
#  |        -1 (the default value) means no limit.
#  |  
#  |  splitlines(self, /, keepends=False)
#  |      Return a list of the lines in the string, breaking at line boundaries.
#  |      
#  |      Line breaks are not included in the resulting list unless keepends is given and
#  |      true.
#  |  
#  |  startswith(...)
#  |      S.startswith(prefix[, start[, end]]) -> bool
#  |      
#  |      Return True if S starts with the specified prefix, False otherwise.
#  |      With optional start, test S beginning at that position.
#  |      With optional end, stop comparing S at that position.
#  |      prefix can also be a tuple of strings to try.
#  |  
#  |  strip(self, chars=None, /)
#  |      Return a copy of the string with leading and trailing whitespace remove.
#  |      
#  |      If chars is given and not None, remove characters in chars instead.
#  |  
#  |  swapcase(self, /)
#  |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
#  |  
#  |  title(self, /)
#  |      Return a version of the string where each word is titlecased.
#  |      
#  |      More specifically, words start with uppercased characters and all remaining
#  |      cased characters have lower case.
#  |  
#  |  translate(self, table, /)
#  |      Replace each character in the string using the given translation table.
#  |      
#  |        table
#  |          Translation table, which must be a mapping of Unicode ordinals to
#  |          Unicode ordinals, strings, or None.
#  |      
#  |      The table must implement lookup/indexing via __getitem__, for instance a
#  |      dictionary or list.  If this operation raises LookupError, the character is
#  |      left untouched.  Characters mapped to None are deleted.
#  |  
#  |  upper(self, /)
#  |      Return a copy of the string converted to uppercase.
#  |  
#  |  zfill(self, width, /)
#  |      Pad a numeric string with zeros on the left, to fill a field of the given width.
#  |      
#  |      The string is never truncated.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |  
#  |  maketrans(x, y=None, z=None, /)
#  |      Return a translation table usable for str.translate().
#  |      
#  |      If there is only one argument, it must be a dictionary mapping Unicode
#  |      ordinals (integers) or characters to Unicode ordinals, strings or None.
#  |      Character keys will be then converted to ordinals.
#  |      If there are two arguments, they must be strings of equal length, and
#  |      in the resulting dictionary, each character in x will be mapped to the
#  |      character at the same position in y. If there is a third argument, it
#  |      must be a string, whose characters will be mapped to None in the result.

# >>> c = ['bear',
# 	     'girafe',
# 	     'elephant',
# 	     'caterpillar',]
# >>> c
# ['bear', 'girafe', 'elephant', 'caterpillar']
# >>> cities = ['Bournemouth', 'London', 'Paris', 'Lima', 'Buenos Aires', 'Santiago de chile', 'Oakland', 'Sydney', 'Albany', 'Perth']
# >>> for city in cities:
# 	print(city)

	
# Bournemouth
# London
# Paris
# Lima
# Buenos Aires
# Santiago de chile
# Oakland
# Sydney
# Albany
# Perth
# >>> colors = {'crimson': 0xdc143c, 'coral': 0xff7f50, 'teal': 0x008080}
# >>> for color in colors:
# 	print(color, colors[color])

	
# crimson 14423100
# coral 16744272
# teal 32896
# >>> from urllib.request import urlopen
# >>> story = urlopen('http://sixty-north.com/c/t.txt')
# s
# >>> story_words = []
# >>> for line in story:
# 	line_words = line.split()
# 	for word in line_words:
# 		sotry_words.append(word)

		
# Traceback (most recent call last):
#   File "<pyshell#80>", line 4, in <module>
#     sotry_words.append(word)
# NameError: name 'sotry_words' is not defined
# >>> 
# >>> from urllib.request import urlopen
# >>> story = urlopen('http://sixty-north.com/c/t.txt')
# s
# >>> story_words = []
# >>> for line in story:
# 	line_words = line.split()
# 	for word in line_words:
# 		sotry_words.append(word)
		
# SyntaxError: multiple statements found while compiling a single statement
# >>> from urllib.request import urlopen
# >>> story = urlopen('http://sixty-north.com/c/t.txt')
# >>> story_words = []
# >>> for line in story:
# 	line_words = line.split()
# 	for word in line_words:
# 		story_words.append(word)

		
# >>> 
# >>> story.close()
# >>> story_words
# [b'It', b'was', b'the', b'best', b'of', b'times', b'it', b'was', b'the', b'worst', b'of', b'times', b'it', b'was', b'the', b'age', b'of', b'wisdom', b'it', b'was', b'the', b'age', b'of', b'foolishness', b'it', b'was', b'the', b'epoch', b'of', b'belief', b'it', b'was', b'the', b'epoch', b'of', b'incredulity', b'it', b'was', b'the', b'season', b'of', b'Light', b'it', b'was', b'the', b'season', b'of', b'Darkness', b'it', b'was', b'the', b'spring', b'of', b'hope', b'it', b'was', b'the', b'winter', b'of', b'despair', b'we', b'had', b'everything', b'before', b'us', b'we', b'had', b'nothing', b'before', b'us', b'we', b'were', b'all', b'going', b'direct', b'to', b'Heaven', b'we', b'were', b'all', b'going', b'direct', b'the', b'other', b'way', b'in', b'short', b'the', b'period', b'was', b'so', b'far', b'like', b'the', b'present', b'period', b'that', b'some', b'of', b'its', b'noisiest', b'authorities', b'insisted', b'on', b'its', b'being', b'received', b'for', b'good', b'or', b'for', b'evil', b'in', b'the', b'superlative', b'degree', b'of', b'comparison', b'only']
# >>> story = urlopen('http://sixty-north.com/c/t.txt')
# >>> story_words = []
# >>> for line in story:
# 	line_words = line.decode('utf8').split()
# 	for word in line_words:
# 		story_words.append(word)

		
# >>> story.close()
# >>> story_words
# ['It', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness', 'it', 'was', 'the', 'epoch', 'of', 'belief', 'it', 'was', 'the', 'epoch', 'of', 'incredulity', 'it', 'was', 'the', 'season', 'of', 'Light', 'it', 'was', 'the', 'season', 'of', 'Darkness', 'it', 'was', 'the', 'spring', 'of', 'hope', 'it', 'was', 'the', 'winter', 'of', 'despair', 'we', 'had', 'everything', 'before', 'us', 'we', 'had', 'nothing', 'before', 'us', 'we', 'were', 'all', 'going', 'direct', 'to', 'Heaven', 'we', 'were', 'all', 'going', 'direct', 'the', 'other', 'way', 'in', 'short', 'the', 'period', 'was', 'so', 'far', 'like', 'the', 'present', 'period', 'that', 'some', 'of', 'its', 'noisiest', 'authorities', 'insisted', 'on', 'its', 'being', 'received', 'for', 'good', 'or', 'for', 'evil', 'in', 'the', 'superlative', 'degree', 'of', 'comparison', 'only']
# >>> [b'It', b'was', b'the', b'best', b'of', b'times', b'it', b'was', b'the', b'worst', b'of', b'times', b'it', b'was', b'the', b'age', b'of', b'wisdom', b'it', b'was', b'the', b'age', b'of', b'foolishness', b'it', b'was', b'the', b'epoch', b'of', b'belief', b'it', b'was', b'the', b'epoch', b'of', b'incredulity', b'it', b'was', b'the', b'season', b'of', b'Light', b'it', b'was', b'the', b'season', b'of', b'Darkness', b'it', b'was', b'the', b'spring', b'of', b'hope', b'it', b'was', b'the', b'winter', b'of', b'despair', b'we', b'had', b'everything', b'before', b'us', b'we', b'had', b'nothing', b'before', b'us', b'we', b'were', b'all', b'going', b'direct', b'to', b'Heaven', b'we', b'were', b'all', b'going', b'direct', b'the', b'other', b'way', b'in', b'short', b'the', b'period', b'was', b'so', b'far', b'like', b'the', b'present', b'period', b'that', b'some', b'of', b'its', b'noisiest', b'authorities', b'insisted', b'on', b'its', b'being', b'received', b'for', b'good', b'or', b'for', b'evil', b'in', b'the', b'superlative', b'degree', b'of', b'comparison', b'only'] # im this example Bytes literals prefixed with lowercase 'b' HTTP data is provided as bytes, Use bytes.decode() to get strings
# [b'It', b'was', b'the', b'best', b'of', b'times', b'it', b'was', b'the', b'worst', b'of', b'times', b'it', b'was', b'the', b'age', b'of', b'wisdom', b'it', b'was', b'the', b'age', b'of', b'foolishness', b'it', b'was', b'the', b'epoch', b'of', b'belief', b'it', b'was', b'the', b'epoch', b'of', b'incredulity', b'it', b'was', b'the', b'season', b'of', b'Light', b'it', b'was', b'the', b'season', b'of', b'Darkness', b'it', b'was', b'the', b'spring', b'of', b'hope', b'it', b'was', b'the', b'winter', b'of', b'despair', b'we', b'had', b'everything', b'before', b'us', b'we', b'had', b'nothing', b'before', b'us', b'we', b'were', b'all', b'going', b'direct', b'to', b'Heaven', b'we', b'were', b'all', b'going', b'direct', b'the', b'other', b'way', b'in', b'short', b'the', b'period', b'was', b'so', b'far', b'like', b'the', b'present', b'period', b'that', b'some', b'of', b'its', b'noisiest', b'authorities', b'insisted', b'on', b'its', b'being', b'received', b'for', b'good', b'or', b'for', b'evil', b'in', b'the', b'superlative', b'degree', b'of', b'comparison', b'only']
# >>> 
