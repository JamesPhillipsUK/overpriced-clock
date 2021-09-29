import PySimpleGUI as psg
import datetime

def launchGameLoop(window):

  while True:
    event, values = window.read(timeout = 1000)
    if event == psg.WIN_CLOSED:
      break
    window['time'].update(datetime.datetime.now().strftime('%H:%M:%S'))
    if datetime.datetime.now().time() < datetime.time(12) and datetime.datetime.now().time() >= datetime.time(6):
      window['greeting'].update("Good morning")
    elif datetime.datetime.now().time() >= datetime.time(12) and datetime.datetime.now().time() < datetime.time(18):
      window['greeting'].update("Good afternoon")
    elif datetime.datetime.now().time() >= datetime.time(18) and datetime.datetime.now().time() < datetime.time(22):
      window['greeting'].update("Good evening")
    else:
      window['greeting'].update("Good night")
  window.close()

def main():
  layout = [
    [psg.Text("The time is:", font = ('Ubuntu', 100), justification = 'center')],
    [psg.Text("00:00:00", size = (8, 1), font = ('Ubuntu', 100), justification = 'center', key = 'time')],
    [psg.Text("Good morning", size = (15, 1), font = ('Ubuntu', 100), justification = 'center', key = 'greeting')]
  ]
  window = psg.Window(title="Clock", layout=layout, size=(1024, 600), element_justification='c', finalize = True)
  window.Maximize()
  launchGameLoop(window)
  print("ran successfully!")
  
if __name__ == "__main__":
  main()
