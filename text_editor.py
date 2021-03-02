from tkinter import *
import tkinter.filedialog
import ast
from PIL import Image, ImageTk


class TextEditor:
    font_size = 28
    font_type = "Georgia"

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):
        txt_file = tkinter.filedialog.askopenfilename(parent=root)
        if txt_file:
            self.text_area.delete(1.0, END)

            file_list = []

            with open(txt_file) as _file:
                # self.text_area.insert(1.0, _file.read())

                file_list = list(ast.literal_eval(_file.read()))
                for data in file_list:
                    if data[0] == "text":
                        self.text_area.insert(data[2], data[1])

                i = 0
                while i < len(file_list):
                    if file_list[i][0] == "tagon":
                        styling = file_list[i][1]
                        start_of_styling = file_list[i][2]
                        end_of_style = END
                        if (i + 2) < len(file_list):
                            end_of_style = file_list[i + 2][2]
                        self.text_area.tag_add(styling, start_of_styling, end_of_style)
                    i += 1

                root.update_idletasks()

    def save_file(self, event=None):
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file is not None:
            text_area_list = self.text_area.dump('1.0', END + '-1c')

            text_area_list = [i for i in text_area_list if i[1] != 'sel' and i[0] != 'mark']

            file.write(' '.join('("{}", "{}", "{}"), '.format(x[0], x[1], x[2]) for x in text_area_list))
            file.close()

    def make_bold(self):
        self.text_area.tag_add('bt', 'sel.first', 'sel.last')

    def make_italic(self):
        self.text_area.tag_add('ital', 'sel.first', 'sel.last')

    def __init__(self, root):
        self.text_to_write = ""
        root.title("Text Editor")
        root.geometry("600x550")
        frame = Frame(root, width=600, height=550)
        scrollbar = Scrollbar(frame)
        self.text_area = Text(frame, width=600, height=550, yscrollcommand=scrollbar.set, padx=10, pady=10,
                              font=(self.font_type, self.font_size))

        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side='right', fill='y')
        self.text_area.pack(side='left', fill='both', expand=True)

        file_menu = Menu(the_menu, tearoff=0)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)

        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.quit_app)

        the_menu.add_cascade(label='File', menu=file_menu)

        edit_menu = Menu(the_menu, tearoff=0)
        edit_menu.add_command(label='Bold', command=self.make_bold)
        edit_menu.add_command(label='Italic', command=self.make_italic)
        the_menu.add_cascade(label='Edit', menu=edit_menu)

        self.text_area.tag_config('bt', font=(self.font_type, self.font_size, 'bold'))
        self.text_area.tag_config('ital', font=(self.font_type, self.font_size, 'italic'))

        toolbar = Frame(root, bd=1, relief=RAISED)
        open_img = Image.open('img/open.png')
        save_img = Image.open('img/save.png')
        copy_img = Image.open('img/copy.png')
        cut_img = Image.open('img/cut.png')
        paste_img = Image.open('img/paste.png')
        bold_img = Image.open('img/bold.png')
        italic_img = Image.open('img/italic.png')

        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        copy_icon = ImageTk.PhotoImage(copy_img)
        cut_icon = ImageTk.PhotoImage(cut_img)
        paste_icon = ImageTk.PhotoImage(paste_img)
        bold_icon = ImageTk.PhotoImage(bold_img)
        italic_icon = ImageTk.PhotoImage(italic_img)

        open_button = Button(toolbar, image=open_icon, command=self.open_file)
        save_button = Button(toolbar, image=save_icon, command=self.save_file)
        copy_button = Button(toolbar, image=copy_icon, command=lambda: root.focus_get().event_generate('<<Copy>>'))
        cut_button = Button(toolbar, image=cut_icon, command=lambda: root.focus_get().event_generate('<<Cut>>'))
        paste_button = Button(toolbar, image=paste_icon, command=lambda: root.focus_get().event_generate('<<Paste>>'))
        bold_button = Button(toolbar, image=bold_icon, command=self.make_bold)
        italic_button = Button(toolbar, image=italic_icon, command=self.make_italic)

        open_button.image = open_icon
        save_button.image = save_icon
        copy_button.image = copy_icon
        cut_button.image = cut_icon
        paste_button.image = paste_icon
        bold_button.image = bold_icon
        italic_button.image = italic_icon

        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        copy_button.pack(side=LEFT, padx=2, pady=2)
        cut_button.pack(side=LEFT, padx=2, pady=2)
        paste_button.pack(side=LEFT, padx=2, pady=2)
        bold_button.pack(side=LEFT, padx=2, pady=2)
        italic_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        frame.pack()

        root.config(menu=the_menu)


root = Tk()
the_menu = Menu(root)
text_editor = TextEditor(root)
root.mainloop()
