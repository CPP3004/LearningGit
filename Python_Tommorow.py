from datetime import date 
 
today=date.today()
days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
print("Tomorrow will be " +days[today.weekday()+1 %7])
print("Version 3")
print("Local Merge Conflict")
print("New junk added on GitHub to show a merge conflict")
print("Creating conflict for a git push / git pull.")
