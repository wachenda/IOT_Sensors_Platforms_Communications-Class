import time

temp = 78.9
humidity = 45.6
pressure = 1002.4

page_template = '''<!DOCTYPE html>
<html>
<head>
<title>My Page TItle</title>
	<link rel="stylesheet" href="styles.css">
</head>

<body style="background-color:powderblue;">

<h1>Assignment #2 - Wachenschwanz</h1>
<br />

<table style="width:50%">
<caption style="font-size:24px;">Current Weather Conditions - {}</caption>
  <tr>
    <th>Temp (deg F)</th>
    <th>Relative Humidity (%)</th> 
    <th>Pressure (hPa)</th>
  </tr>
  <tr>
    <td>{}</td>
    <td>{}</td> 
    <td>{}</td>
  </tr>
</table>

<br />

</body>

</html>'''

out_str = page_template.format(time.strftime("%I:%M %p, %a %b %d, %Y"),temp,humidity,pressure)

f = open('assignment2-DW.html', 'w')
f.write(out_str)
f.close()

