"""
clock.py
A simple Python-powered clock for my Raspberry Pi.  Using PySimpleGUI to make it look nice.

Authors
-------
  Jesse Phillips <james@jamesphillipsuk.com>
"""

import PySimpleGUI as psg # PySimpleGUI UI Library
import datetime # It's a clock.

def launchEventLoop(window):
  """
  This method contains the event loop for the application.  It takes the applications window as a parameter.

  Parameters
  ----------
  window: window
    The application window.
  """
  # BEGIN THE EVENT LOOP
  while True:
    event, values = window.read(timeout = 1000) # Only need to update once per second.
    if event == psg.WIN_CLOSED:
      break # End the event runtime if the user requests to close the window.

    window['time'].update(datetime.datetime.now().strftime('%H:%M:%S')) # Update the clock.

    # Display a nice message to the user.
    now = datetime.datetime.now().time()
    if now < datetime.time(12) and now >= datetime.time(6):
      window['greeting'].update("Good morning")
    elif now >= datetime.time(12) and now < datetime.time(18):
      window['greeting'].update("Good afternoon")
    elif now >= datetime.time(18) and now < datetime.time(22):
      window['greeting'].update("Good evening")
    else:
      window['greeting'].update("Good night")
  # KILL THE WINDOW ONCE THE EVENT RUNTIME IS OVER.
  window.close()

def main():
  """
  Main method for the application.
  """
  psg.theme('DarkAmber') # Set a cool-looking theme, easy on the eyes.
  layout = [ # The Window layout.  Filled with default values.
    [psg.Text("The time is:", font = 'Ubuntu 100', justification = 'center')],
    [psg.Text("00:00:00", size = (8, 1), font = 'Ubuntu 165 bold', justification = 'center', key = 'time')],
    [psg.Text("Good morning", size = (15, 1), font = 'Ubuntu 96', justification = 'center', key = 'greeting')]
  ]
  window = psg.Window(title="Clock", layout=layout, size=(1024, 600), element_justification='c', finalize = True) # Build the application window.
  window.Maximize()
  launchEventLoop(window) # Run the event loop for the application on the window.

if __name__ == "__main__":
  main()