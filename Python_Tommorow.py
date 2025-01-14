from datetime import date 
 
today=date.today()
days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
print("Tomorrow will be " +days[today.weekday()+1 %7])
print("Version 3")
print("Local Merge Conflict")
print("New junk added on GitHub to show a merge conflict")
print("New change to show the effect of a pull to local, after push error due to a conflict. - REMOTE")
