import FreeSimpleGUI as sg
import zip_creator as zip

label1 = sg.Text('Select files to compress:')
input1 = sg.Input()
choose_btn1 = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text('Select destination folder:')
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse('Choose', key='folder')

compress_btn = sg.Button('Compress')

layout = [[label1, input1, choose_btn1], [label2, input2, choose_btn2], [compress_btn] ]

window = sg.Window('File Compressor', layout = layout)

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values["folder"]
    print(filepaths)
    print(folder)
    zip.make_archive(filepaths, folder)

    
window.close()