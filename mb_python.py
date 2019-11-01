# Python code for Mandelbrot Fractal 
  
# Import necessary libraries 
from PIL import Image 
from numpy import complex, array 
import colorsys 
  

from bottle import route, run, static_file

# setting the width of the output image as 1024 

# @route('/mandel')
# def show():
#     return ('hello Junior')    
# run(host='localhost', port=8080, reloader=True)


# def mb(x, y):
# 	iterations = int(request.query.it or 1000)
	
# 	response.content-type = 'image/png'
#     return mandelbrot(x, y, iterations)

#run(host=requests.get('http://169.254.169.254/meta:data/local.ipv4', test, port=80)


# @route('/static/<filename:mandelbrot.png>')
# def send_static(filename):
#     return static_file(filename, root='/var')


# a function to return a tuple of colors 
# as integer value of rgb 
def rgb_conv(i): 
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
    return tuple(color.astype(int)) 
    
# function defining a mandelbrot 
def mandelbrot(x, y): 
    c0 = complex(x, y) 
    c = 0
    for i in range(1, 1000): 
        if abs(c) > 2: 
            return rgb_conv(i) 
        c = c * c + c0 
    return (0, 0, 0) 
   
@route('/man/<w:int>/<h:int>/<it:int>')
# creating the new image in RGB mode 

def view(it, w, h):
    WIDTH =it 
    img = Image.new('RGB', (w, h)) 
    pixels = img.load() 

    for x in range(img.size[0]): 
    
        # displaying the progress as percentage 
        print("%.2f %%" % (x / WIDTH * 100.0))  
        for y in range(img.size[1]): 
            pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4), 
                                        (y - (WIDTH / 4)) / (WIDTH / 4)) 
    
    # to display the created fractal after  
    # completing the given number of iterations 
    #img.show()
    img.save(fp='var/mandelbrot.png',format='png')
    return static_file('mandelbrot.png', root='./var')

run(host='localhost', debug=True, reloader=True, port=8080)


