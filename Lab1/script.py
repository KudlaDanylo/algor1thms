
def numbers_stats(*args, **kwarg):
   round_to = kwarg.get("round_to")
   ignore_none = kwarg.get("ignore_none")

   numbers = []
   for i in args:
      if ignore_none and i == None:
         continue
         break
      numbers.append(i)

   count = len(numbers)
   s = 0
   for i in args:
      if i:
         s = s + i
   suma = s
   mean = suma/count

   if round_to != None:
      mean = round(mean, round_to)

   array = {"count": count, "sum": suma, "mean": mean}
   print(array)
   print(kwarg)
numbers_stats(None, 5, ignore_none=True)




