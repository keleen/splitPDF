import PySimpleGUI as sg
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def pdf_splitter(file_path, start, end):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    dir_name = os.path.dirname(file_path)
    pdf = PdfFileReader(file_path)
    pdf_writer = PdfFileWriter()
    out_put_filename = '{}/{}_{}_{}.pdf'.format(dir_name, file_name, start, end)
    new_start = start - 1
    for page in range(new_start, end):
        pdf_writer.addPage(pdf.getPage(page))
        print(page)

    with open(out_put_filename, 'wb') as out:
        pdf_writer.write(out)
        sg.popup_notify('分割成功', out_put_filename)

def start():
    layout = [
        [sg.Text('开始页数:'), sg.Input()],
        [sg.Text('结束页数:'), sg.Input()],
        [sg.Text('选择文件:'), sg.Input(readonly=True), sg.FileBrowse('浏览', file_types = (('ALL Files', '*.pdf'),),)],
        [sg.Button('Cancle'), sg.Button('OK')]
    ]

    window = sg.Window('分割PDF', layout=layout, location=(100, 100))

    while True:
        event, values = window.read()
        if event == 'OK':
            start = int(values.get(0))
            end = int(values.get(1))
            file_path = values.get(2)

            if file_path is None or file_path == '':
                sg.popup_notify('错误',  '请选择PDF', icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                continue
            pdf = PdfFileReader(file_path)
            numPages = pdf.numPages
            if start > end:
                sg.popup_notify('错误', '开始页数不能大于结束页数', icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                continue
            if start - 1 < 0:
                sg.popup_notify('错误', '开始页数不能小于1', icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                continue
            if start > numPages :
                sg.popup_notify('错误', '开始页数不能大于PDF总页数', icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                continue
            if end > numPages:
                sg.popup_notify('错误', '结束页数不能大于PDF总页数', icon=sg.SYSTEM_TRAY_MESSAGE_ICON_WARNING)
                continue

            pdf_splitter(file_path, start, end)

        elif event == 'Cancle':
            exit(0)
        elif event in (sg.WIN_CLOSED, 'Exit'):
            exit(0)

    window.close()


if __name__ == '__main__':
    start()
