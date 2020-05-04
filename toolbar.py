import time, sys

def update_progress(progress):
    barLength = 42
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    block = int(round(barLength*progress))
    text = "\r {1}% {0} {2}".format( "#"*block + " " *(barLength-block), int(progress*100), status)
    sys.stdout.write(text)
    sys.stdout.flush()

def default():
    for i in range(101):
        update_progress(i/100.0)
        time.sleep(0.1)

print("")
