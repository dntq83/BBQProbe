import urllib.request               #talks to an ESP32 running this code: https://github.com/johnty/BBQProbe/tree/main/thermocouple_esp32
contents = urllib.request.urlopen("http://10.10.29").read().decode()  #find IP address and put it here...
f_string = contents.split("/")[2]   #first / is for </head>, second / is between the C and F readings ;)
f_vals = f_string.split();          # split again based on spaces, result should be the F value string only.
print(f_vals[0])