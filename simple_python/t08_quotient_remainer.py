secs = 301.765421

secs2 = int(secs)

print(secs2)

day, modday = divmod(secs2, 60*60*24)
print (modday)

hour, modhour = divmod(modday, 60*60)
print (hour)
print (modhour)

minu, modminu = divmod(modhour, 60)
print (minu)
print (modminu)


sec_final = modminu

if (secs -secs2) >= 0.5:
  sec_final = sec_final+1

print (sec_final)

print(f'day:{day} hour:{hour} minute:{minu} seconds:{sec_final}')
