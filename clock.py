import PySimpleGUI as psg

def launchGameLoop(window):
  while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
      break
  window.close()

def main():
  layout = [[]]
  window = psg.Window(title="Clock", layout=layout, size=(1024, 600)).Finalize()
  window.Maximize()
  launchGameLoop(window)
  print("ran successfully!")
  
if __name__ == "__main__":
  main()
