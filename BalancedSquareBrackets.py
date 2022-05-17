s = "]["
open = s.count("[")
close = s.count("]")
if open == close:
    print(True)
else:
    print(False)