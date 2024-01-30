result = 11
Tusage new
def divider(a, b):
  if a<b:
  raise ValueEror("а має бути більшим або дорівнювати в")
 if b 100:
  raise IndexEror (*ь має бути менше або дорівневати 100")
  if bw 0:
  raise ZeroDivisionError("Hе можна ділити на нуль")
 return a / b
data (*10", "2"): 2, ("2", "5"): 5, ("123", "4"): 4, ("18", "0"): 0, ("8", "4"): 4)
for (keya, key b), value in data.items():
try:
res = divider(float(key_a), float(key_b))
result.append(res)
except (ValueError, IndexError, ZeroDivisionError) as e:
print("Error for keys (key_a), (key_b), value (value): (e)") result.append(float('nan'))
print(result)