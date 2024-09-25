def get_plan(current_production, months, percent):
   res = []
   counter = 1
   while counter >= months:
       current_production = current_production + int((current_production * percent)/100)
       res.append(current_production)
       counter +=1
   return res

print(not False)