#!/usr/bin/python3

"""
David Wachenschwanz
UCSC IoT 30402
Fall 2017
Assignment #6 - Controlling Devices Using CGI
"""

import cgi, cgitb
import pigpio

# Raspberry Pi GPIO pins to connect to
R = 4   # GPIO04
G = 17  # GPIO17
B = 22  # GPIO22

# Initialize DMA PWM using pigpio
p = pigpio.pi()
p.set_PWM_frequency(R,8000)

cgitb.enable()

def main():
    form=cgi.FieldStorage()
    
    page_template="""<html>
    <head>
        <title>Assignment 6 :: CGI Color</title>
        <style>
            #left{
              
                
            }
            #red{
                
            }
            #green{
               
            }
            #blue{
                
            }

            .color {
              display: inline-block;
              zoom:1; *display: inline;
              width: 100px;
              height: 100px;
              border: 1px solid rgba(0, 0, 0, 0.5);
              -webkit-box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.3);
              -moz-box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.3);
              box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.3);
              margin: 0 20px;
              vertical-align: middle;
            }
            input[type=range] {
              -webkit-appearance: none;
              margin: 18px 0;
              width: 30%;
            }
            input[type=range]:focus {
              outline: none;
            }
            input[type=range]::-webkit-slider-runnable-track {
              width: 100%;
              height: 8.4px;
              cursor: pointer;
              animate: 0.2s;
              box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
              background: #d3d3d3;
              border-radius: 1.3px;
              border: 0.2px solid #010101;
            }
            input[type=range]::-webkit-slider-thumb {
              box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
              border: 1px solid #000000;
              height: 36px;
              width: 16px;
              border-radius: 3px;
              background: #ffffff;
              cursor: pointer;
              -webkit-appearance: none;
              margin-top: -14px;
            }
            input[type=range]:focus::-webkit-slider-runnable-track {
              background: #367ebd;
            }
            input[type=range]::-moz-range-track {
              width: 100%;
              height: 8.4px;
              cursor: pointer;
              animate: 0.2s;
              box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
              background: #d3d3d3;
              border-radius: 1.3px;
              border: 0.2px solid #010101;
            }
            input[type=range]::-moz-range-thumb {
              box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
              border: 1px solid #000000;
              height: 36px;
              width: 16px;
              border-radius: 3px;
              background: #ffffff;
              cursor: pointer;
            }
            input[type=range]::-ms-track {
              width: 100%;
              height: 8.4px;
              cursor: pointer;
              animate: 0.2s;
              background: transparent;
              border-color: transparent;
              border-width: 16px 0;
              color: transparent;
            }
            input[type=range]::-ms-fill-lower {
              background: #2a6495;
              border: 0.2px solid #010101;
              border-radius: 2.6px;
              box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
            }
            input[type=range]::-ms-fill-upper {
              background: #3071a9;
              border: 0.2px solid #010101;
              border-radius: 2.6px;
              box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
            }
            input[type=range]::-ms-thumb {
              box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
              border: 1px solid #000000;
              height: 36px;
              width: 16px;
              border-radius: 3px;
              background: #ffffff;
              cursor: pointer;
            }
            input[type=range]:focus::-ms-fill-lower {
              background: #d3d3d3;
            }
            input[type=range]:focus::-ms-fill-upper {
              background: #367ebd;
            }

            

        </style>
    </head>

    <body>
    <h1>Assignment 6 - CGI Colors Using RGB LED</h1>
    <hr>
    <p>Use sliders to select RGB LED color:
        <form method="post" action="/cgi-bin/assignment6_rgb_led.py"> 
            <div id="left"> 
            <div id="red"><br>
            R <input type="range" id="redslide" min="0" max="255" name="Red"/> 
            <span id="redvalue"></span>
            <br></div>
            <div id="green"><br>
            G <input type="range" id="greenslide" min="0" max="255" name="Green" value="GreenValue"/>
            <span id="greenvalue"></span>
            <br></div>
            <div id="blue"><br>
            B <input type="range" id="blueslide" min="0" max="255" name="Blue" value="BlueValue"/>
            <span id="bluevalue"></span>
            <br></div>
            </div>
            <div class="color" id="swatch" style="background: RED;"></div>
            <span id="hexcolor"></span>

            <br><br>
            <div id="txtinput"> 
            <input type="submit" value="Update RGB LED Color" /> </div>
        </form>
    </p>    

    <script>

        var colorswatch = document.getElementById("swatch");

        var hexvalue = document.getElementById("hexcolor");

        var redslider = document.getElementById("redslide");
        var redoutput = document.getElementById("redvalue");
        var r = redoutput.innerHTML = redslider.value;

        var greenslider = document.getElementById("greenslide");
        var greenoutput = document.getElementById("greenvalue");
        var g = greenoutput.innerHTML = greenslider.value;

        var blueslider = document.getElementById("blueslide");
        var blueoutput = document.getElementById("bluevalue");
        var b = blueoutput.innerHTML = blueslider.value;

        redslider.oninput = function() {
          r = redoutput.innerHTML = this.value;
          colorswatch.style.backgroundColor="#"+RGBToHex(r,g,b); 
          hexvalue.innerHTML = "#"+RGBToHex(r,g,b);
        }

        greenslider.oninput = function() {
          g = greenoutput.innerHTML = this.value;
          colorswatch.style.backgroundColor="#"+RGBToHex(r,g,b); 
          hexvalue.innerHTML = "#"+RGBToHex(r,g,b);
        }

        blueslider.oninput = function() {
          b = blueoutput.innerHTML = this.value;
          colorswatch.style.backgroundColor="#"+RGBToHex(r,g,b); 
          hexvalue.innerHTML = "#"+RGBToHex(r,g,b);
        }

        var rgbth = function (rgb) { 
          var hex = Number(rgb).toString(16);
          if (hex.length < 2) {
               hex = "0" + hex;
          }
          return hex;
        };
        var RGBToHex = function(r,g,b) {   
          var red = rgbth(r);
          var green = rgbth(g);
          var blue = rgbth(b);
          return red+green+blue;
        };


       


        
    </script>
    """

    r = 0
    g = 0
    b = 0


    print("Content-type: text/html\n\n")   
    
    if "Red" in form and "Green" in form and "Blue" in form:
      r = int(form.getvalue('Red'))
      g = int(form.getvalue('Green'))
      b = int(form.getvalue('Blue'))

      

      p.set_PWM_dutycycle(R,r)
      p.set_PWM_dutycycle(G,g)
      p.set_PWM_dutycycle(B,b)


    print(page_template)

    print("""<script>document.getElementById("redslide").value="{0}";
                      document.getElementById("redvalue").innerHTML="{0}";</script>""".format(r))
    print("""<script>document.getElementById("greenslide").value="{0}";
                      document.getElementById("greenvalue").innerHTML="{0}";</script>""".format(g))
    print("""<script>document.getElementById("blueslide").value="{0}";
                      document.getElementById("bluevalue").innerHTML="{0}";</script>""".format(b))
    print("""<script>colorswatch.style.backgroundColor="#"+RGBToHex({0},{1},{2}); 
          hexvalue.innerHTML = "#"+RGBToHex({0},{1},{2});</script>""".format(r,g,b))
    print("""<script>r = {0}; g = {1}; b = {2};</script>""".format(r,g,b))
    print()
    
    print("""</body></html>""")


main()