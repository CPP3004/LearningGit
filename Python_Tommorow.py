from datetime import date 
 
today=date.today()
days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
print("Tomorrow will be " +days[today.weekday()+1 %7])
print("Heeeeeeeeeeeeee Hawwwwwwwwwwwwwwww")