total = int(input())


hours = total//3600
#print(hours)

mins = (total-hours*60*60)//60
#print(mins)

secs = total - (hours*60*60 + mins*60)
#print(secs)

print(f"Hours: {hours}, Minutes: {mins}, Seconds: {secs}")