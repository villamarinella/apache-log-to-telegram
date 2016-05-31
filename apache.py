import time
import sys
import subprocess

datei='/var/log/apache2/access.log'
wait_time=300
## waiting time before the enxt access
with open(datei) as f:
    line_count = len(f.readlines())
    print line_count
    anzahl=line_count

while True:
  with open(datei) as f:
    line_count = len(f.readlines())
    print line_count
    anzahl1=line_count
    if anzahl1 > anzahl:
      with open(datei) as f:
        line_list = f.read().splitlines()
        j=anzahl
        while True:
          print line_list[j]
          aax=line_list[j]
          subprocess.call(['./tg.sh' , aax])
          time.sleep(10)
	  j=j+1
	  if j >= anzahl1:
	    anzahl=anzahl1
	    break
	  
    time.sleep(wait_time)
    
    


