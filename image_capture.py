#!/usr/bin/python

def main():
    import time
    from datetime import datetime
    import picamera
    
    with picamera.PiCamera() as camera:
        filename = '{}.jpg'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        camera.start_preview()
        time.sleep(2)
        camera.capture(filename)
        camera.stop_preview()

if __name__ == '__main__':
    main()
