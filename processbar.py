import PySimpleGUI as sg

def CustomMeter():
    # layout the form
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(10000, orientation='h',
                              size=(20, 20), key='progress')],
              [sg.Cancel()]]

    # create the form`
    window = sg.Window('Custom Progress Meter', layout)
    progress_bar = window['progress']
    # loop that would normally do something useful
    for i in range(10000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=0, timeout_key='timeout')
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.update_bar(i+1)
    # done with loop... need to destroy the window as it's still open
    window.CloseNonBlocking()

CustomMeter()