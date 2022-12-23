"""
@Author: Bhupinder Singh
@Date: 2022-12-15
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-15
@Title : Python Program for measuring the time that elapses between the start and end clicks

"""
import time

def time_convert(sec):


  """
  Description:
      Function to convert the time into a standard format.
  Parameters:
      sec: Time in secs
  Return:
      none
  """


  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


if __name__ == '__main__':

    input("Press Enter to start")
    start_time = time.time()

    input("Press Enter to stop")
    end_time = time.time()

    time_lapsed = end_time - start_time
    time_convert(time_lapsed)