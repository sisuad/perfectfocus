import simplegui

b = 0
count = 100
interval = 10
stop_time = 0
screen_title = "Perfect"

def format(count):
    global a, b, second  
    a = count // 100  
    b = 7 - a
    return str(b) 
    
def start_handler():
    timer.start()
    
def stop_handler():
    timer.stop()
         
def tick():
    global count, stop_time
    count += 1
    if count <= 1000:
        stop_time = count - 600

    else:
        timer.stop()
    
def reset_handler():
    global count, stop_time
    timer.stop()
    stop_time = 0
    count = 100
    
def draw_handler(canvas):
    global count, screen_title, stop_time, a
    canvas.draw_text("@Suger ", (150, 145), 15, "white")
    if count == 100:
        canvas.draw_text("Count 6 ", (65, 45), 20, "white")
        canvas.draw_text("and ", (80, 75), 20, "white")
        canvas.draw_text("click 'Stop'  ASAP", (30, 105), 20, "white")
        
    elif timer.is_running():
        if 100 < count < 400:        
            canvas.draw_text(format(count), (80, 80), 30, "white")
        else:
            canvas.draw_text("???", (65, 80), 30, "white")
    else:
        if count == 600:
            canvas.draw_text(str(screen_title), (65, 80), 30, "white")
        elif stop_time == 400:
            canvas.draw_text("Time's Out!", (25, 80), 30, "red")
        else:
            if stop_time < 0:
                canvas.draw_text("-" + str(b - 1) + "." + str((100 - stop_time) % 100 ) + "s", (55, 80), 30, "white")
            else:
                canvas.draw_text("+" + str(count // 100 - 6 ) + "." + str((100 - stop_time) % 100 ) + "s", (65, 80), 30, "white")

frame = simplegui.create_frame("PerfectFocus", 200, 150)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, tick)

button1 = frame.add_button("Start", start_handler, 100,)
button2 = frame.add_button("Stop", stop_handler, 100)
button3 = frame.add_button("Restart", reset_handler, 100)

# start frame
frame.start()
   