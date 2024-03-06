co = [[3,3,3,1,6,1,2,6,2,1,2],[3,3,3,1,6,2,2,4,2,2,2],[3,3,3,1,3,6,2,2,2,3,2],
      [9,1,6,4,4,4,2],[9,1,6,5,2,5,2],[3,3,3,1,3,8,2],[3,3,3,1,6,5,2,5,2],
      [3,3,3,1,6,5,2,5,2]]

def fn(b):
   if b:
      return chr(64)
   elif not b:
      return chr(32)
   else:
      return None

for li in co:
   stat = True
   i = 0
   while i < len(li):
      print(fn(stat)*li[i], end = "")
      stat = not stat
      i += 1 # There is no i++ in Python
   print()
