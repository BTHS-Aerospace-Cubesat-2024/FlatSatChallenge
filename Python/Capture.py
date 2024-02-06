#File For Group Photo
#AUTHOR: Samuel Ashkenas
#DATE: Feb/5/2024

#import libraries
import time
import board
from adafruit_lis3mdl import LIS3MDL
from git import Repo
from picamera2 import Picamera2

#VARIABLES
THRESHOLD = 0      #Any desired value from the accelerometer
REPO_PATH = "/home/pi/FlatSatChallenge"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "Photos"   #Your image folder path in your GitHub repo: ex. /Images

#imu and camera initialization
i2c = board.I2C()
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)


def git_push():
    """
    This function is complete. Stages, commits, and pushes new images to your GitHub repo.
    """
    try:
        repo = Repo(REPO_PATH)
        origin = repo.remote('origin')
        print('added remote')
        origin.pull()
        print('pulled changes')
        repo.git.add(REPO_PATH + "/" + FOLDER_PATH)
        repo.index.commit('New Photo')
        print('made the commit')
        #repo.git.execute("git push <insertkey>@github.com/BTHS-Aerospace-Cubesat-2024/FlatSatChallenge.git")
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')


def img_gen(name):
    """
    This function is complete. Generates a new image name.

    Parameters:
        name (str): your name ex. MasonM
    """
    t = time.strftime("_%H%M%S")
    imgname = (f'{REPO_PATH}/{FOLDER_PATH}/{name}{t}.jpg')
    return imgname


def take_photo():
    """
    This function is NOT complete. Takes a photo when the FlatSat is shaken.
    Replace psuedocode with your own code.
    """
    while True:
        Wait = input("Press Enter to take a picture... ")
        #picam2.start_preview(Preview.DRM)
        picam2.start()
        time.sleep(1)
        name = img_gen("Capture")
        picam2.capture_file(name)
        time.sleep(1)
        git_push()

        #CHECKS IF READINGS ARE ABOVE THRESHOLD
            #PAUSE
            #name = ""     #First Name, Last Initial  ex. MasonM
            #TAKE PHOTO
            #PUSH PHOTO TO GITHUB
        
        #PAUSE


def main():
    take_photo()


if __name__ == '__main__':
    main()
