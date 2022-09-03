# Notepad text editor

# Import the necessary modules
import tkinter
from tkinter import colorchooser, filedialog, messagebox, font
import os


def new_file_menu_item():
    global file
    window.title(string="Notepad text editor : Untitled")
    if len(text_area.get(index1="1.0", index2=tkinter.END)) > 0:
        response = messagebox.askyesno(title="Notepad",
                                       message="Do you save want to save changes to 'Untitled'")
        print(response)
        if response is True:
            file_path = filedialog.asksaveasfilename(initialdir="C:/Users/ASHWINKANNAN/OneDrive/Desktop",
                                                     initialfile="Untitled.txt",
                                                     defaultextension=".txt",
                                                     filetypes=[
                                                         ("Text files", ".txt"),
                                                         ("HTML files", ".html"),
                                                         ("Python files", ".py"),
                                                         ("Java files", ".java"),
                                                         ("All files", ".*")
                                                         ])
            try:
                file = open(file=file_path, mode="wt")
                file.write(text_area.get(index1=1.0, index2=tkinter.END))

            finally:
                file.close()

        elif response is False:
            pass
    text_area.delete(index1=1.0, index2=tkinter.END)


def new_window_file_menu_item():
    notepad_text_editor_program()


def open_file_menu_item():
    file = filedialog.askopenfilename(initialdir="C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop",
                                      title="Open files",
                                      defaultextension=".txt",
                                      filetypes=[
                                        ("Text files", "*.txt"),
                                        ("HTML files", "*.html"),
                                        ("Python files", "*.py"),
                                        ("Java files", "*.java"),
                                        ("All files", "*.*")
                                      ])
    try:
        window.title(os.path.basename(file))
        text_area.delete(index1=1.0, index2=tkinter.END)
        file = open(file, "rt")
        text_area.insert("1.0", file.read())
    except FileNotFoundError:
        messagebox.showerror(title="Error message",
                             message="File is not found ☹☹")
    finally:
        file.close()


def save_as_file_menu_item():
    global file
    file_path = filedialog.asksaveasfilename(initialdir="C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop",
                                    title="Save As file",
                                    initialfile="*.txt",
                                    filetypes=[
                                        ("Text files", ".txt"),
                                        ("HTML files", ".html"),
                                        ("Python files", ".py"),
                                        ("Java files", ".java"),
                                        ("All files", ".*")
                                    ])
    try:
        file = open(file=file_path, mode="wt")
        file.write(text_area.get(index1=1.0, index2=tkinter.END))

    finally:
        file.close()


def exit_file_menu_item():
    try:
        window.destroy()
    except Exception:
        messagebox.showinfo(title="Exit error",
                            message="Unfortunately Exit function didn't work. Press 'X' button on the top right corner "
                                    "to exit")


def select_all_edit_menu_item():
    text_area.get(index1=1.0, index2=tkinter.END)


def cut_edit_menu_item():
    text_area.event_generate("<<Cut>>")


def copy_edit_menu_item():
    text_area.event_generate("<<Copy>>")


def paste_edit_menu_item():
    text_area.event_generate("<<Paste>>")


def delete_edit_menu_item():
    text_area.delete(index1=1.0, index2=tkinter.END)


def help_about_menu_item():
    messagebox.showinfo(title="Help menu",
                        message="This is the notepad text editor program version 1.0 which is written by me")


def appearance():
    if theme.get() == 1:
        # print("Light Theme is turned on")
        text_area.config(bg="white", fg="black", insertbackground="black")
        menu_bar.config(bg="white", fg="black")
        file_menu.config(bg="white", fg="black")
        edit_menu.config(bg="white", fg="black")
        about_menu.config(bg="white", fg="black")
        settings_menu.config(bg="white", fg="black")
        vertical_scrollbar.config(bg="white", activebackground="white")
        settings_window.config(bg="white")
        appearance_frame.config(bg="white")
        appearance_label.config(bg="white", fg="black")
        appearance_radiobutton.config(bg="white", fg="black")
        color_frame.config(bg="white")
        color_picker_label.config(bg="white", fg="black")
        background_color_button.config(bg="white", fg="black")
        font_color_button.config(bg="white", fg="black")
        font_frame.config(bg="white")
        font_label.config(bg="white", fg="black")
        font_type.config(bg="white", fg="black")
        font_size_spinbox.config(bg="white", fg="black")

    else:
        # print("Dark Theme is turned on")
        text_area.config(bg="black", fg="white", insertbackground="white")
        menu_bar.config(bg="black", fg="white")
        file_menu.config(bg="black", fg="white")
        edit_menu.config(bg="black", fg="white")
        about_menu.config(bg="black", fg="white")
        settings_menu.config(bg="black", fg="white")
        vertical_scrollbar.config(bg="black", activebackground="black")
        settings_window.config(bg="black")
        appearance_frame.config(bg="black")
        appearance_label.config(bg="black", fg="white")
        appearance_radiobutton.config(bg="black", fg="white")
        color_frame.config(bg="black")
        color_picker_label.config(bg="black", fg="white")
        background_color_button.config(bg="black", fg="white")
        font_color_button.config(bg="black", fg="white")
        font_frame.config(bg="black")
        font_label.config(bg="black", fg="white")
        font_type.config(bg="black", fg="white")
        font_size_spinbox.config(bg="black", fg="white")


def background_color_picker():
    color = colorchooser.askcolor(title="Pick a background color")[1]
    text_area.config(bg=color)


def font_color_picker():
    color = colorchooser.askcolor(title="Pick a font color")[1]
    text_area.config(fg=color, insertbackground=color)


def change_font():
    text_area.config(font=(font_name.get(), font_size_spinbox.get()))


def settings_menu_item():
    global theme, font_size_spinbox, background_color_button, font_color_button, font_type, font_name, \
        settings_window, appearance_frame, appearance_label, appearance_radiobutton, color_frame, color_picker_label, \
        font_label, font_frame, font_size_spinbox

    settings_window = tkinter.Toplevel()
    settings_window.title(string="Settings")
    settings_window.geometry(newGeometry="380x480")
    settings_window.resizable(width=0, height=0)
    settings_window.iconbitmap(r"C:\\Users\\ASHWINKANNAN\\Downloads\\favicon.ico")

    appearance_frame = tkinter.Frame(master=settings_window)
    appearance_frame.pack()

    theme = tkinter.IntVar()

    appearance_label = tkinter.Label(master=appearance_frame,
                                     text="Appearance",
                                     font=("Arial", 20),
                                     pady=20)
    appearance_label.pack()

    appearance_theme = ["Dark Theme", "Light Theme"]

    for index in range(len(appearance_theme)):
        appearance_radiobutton = tkinter.Radiobutton(master=appearance_frame,
                                                     text=appearance_theme[index],
                                                     font=("Arial", 10),
                                                     value=index,
                                                     variable=theme,
                                                     command=appearance,
                                                     indicatoron=False
                                                     )
        appearance_radiobutton.pack(side=tkinter.RIGHT)

    color_frame = tkinter.Frame(master=settings_window)
    color_frame.pack(pady=20)

    color_picker_label = tkinter.Label(master=color_frame,
                                       text="Color Picker", 
                                       font=("Arial", 20))
    color_picker_label.pack(pady=20)

    background_color_button = tkinter.Button(master=color_frame,
                                             text="Background color",
                                             font=("Arial", 10, "bold"),
                                             command=background_color_picker,
                                             )
    background_color_button.pack(side=tkinter.LEFT)

    font_color_button = tkinter.Button(master=color_frame,
                                       text="Font color",
                                       font=("Arial", 10, "bold"),
                                       command=font_color_picker,
                                       )
    font_color_button.pack(side=tkinter.RIGHT)

    font_frame = tkinter.Frame(master=settings_window)
    font_frame.pack()

    font_label = tkinter.Label(master=font_frame,
                               text="Font",
                               font=("Arial", 20))
    font_label.pack(pady=20)

    font_type = tkinter.OptionMenu(font_frame,
                                   font_name,
                                   *font.families(),
                                   change_font)
    font_type.config(direction="above", font=("Arial", 10, "bold"))
    font_type.pack(side=tkinter.RIGHT)

    font_size_spinbox = tkinter.Spinbox(master=font_frame,
                                        textvariable=font_size,
                                        from_=8, to=100, increment=2,
                                        justify=tkinter.CENTER,
                                        width=10,
                                        font=("Arial", 15),
                                        command=change_font)
    font_size_spinbox.pack(side=tkinter.LEFT)


def notepad_text_editor_program():
    global window, text_area, menu_bar, file_menu, edit_menu, about_menu, settings_menu, vertical_scrollbar, font_name, font_size

    # ---------------------------- Window ----------------------
    window = tkinter.Tk()
    window.title(string="Notepad Text editor")
    window.geometry(newGeometry="500x500")
    window.iconbitmap(r"C:\\Users\\ASHWINKANNAN\\Downloads\\favicon.ico")
    # window.iconphoto(True, notepad_icon)

    font_name = tkinter.StringVar(master=window)
    font_name.set(value="Arial")

    font_size = tkinter.StringVar(master=window)
    font_size.set(value="25")

    # ---------------------------- Menubar, Menu and MenuItem ---------------------------------
    menu_bar = tkinter.Menu(master=window)
    window.config(menu=menu_bar)

    # File menu
    file_menu = tkinter.Menu(master=window,
                             font=("Times new roman", 15),
                             tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="New (Ctrl+N)", command=new_file_menu_item)
    file_menu.add_command(label="New Window (Ctrl+Shift+N)", command=new_window_file_menu_item)
    file_menu.add_command(label="Open (Ctrl+O)", command=open_file_menu_item)
    file_menu.add_command(label="Save As (Ctrl+Shift+S)", command=save_as_file_menu_item)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_file_menu_item)

    # Edit menu
    edit_menu = tkinter.Menu(master=window,
                             font=("Times new roman", 15),
                             tearoff=False)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    edit_menu.add_command(label="Select All (Ctrl+A)", command=select_all_edit_menu_item)
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut (Ctrl+X)", command=cut_edit_menu_item)
    edit_menu.add_command(label="Copy (Ctrl+C)", command=copy_edit_menu_item)
    edit_menu.add_command(label="Paste (Ctrl+V)", command=paste_edit_menu_item)
    edit_menu.add_command(label="Delete (Del)", command=delete_edit_menu_item)

    # About Menu
    about_menu = tkinter.Menu(master=window,
                              font=("Times new roman", 15),
                              tearoff=False)
    menu_bar.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="Help", command=help_about_menu_item)

    # Settings Menu
    settings_menu = tkinter.Menu(master=window,
                                 font=("Times new roman", 15),
                                 tearoff=False)
    menu_bar.add_cascade(label="Setting", menu=settings_menu)
    settings_menu.add_command(label="Setting", command=settings_menu_item)
    # -----------------------------------------------------------------------

    # --------------------- 'Scrollbar' widget -----------------------------------
    # Vertical scrollbar
    vertical_scrollbar = tkinter.Scrollbar(master=window,
                                           orient=tkinter.VERTICAL,
                                           width=25,
                                           )
    vertical_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    # ---------------------------------------------------------------------------

    # ----------------------------- 'Text' widget --------------------------------
    # text area
    text_area = tkinter.Text(master=window,
                             font=(font_name.get(), font_size.get()),
                             height=50, width=150,
                             # xscrollcommand=horizontal_scrollbar.set,
                             yscrollcommand=vertical_scrollbar.set)
    text_area.pack()
    # ---------------------------------------------------------

    vertical_scrollbar.config(command=text_area.yview)

    window.mainloop()


# Main Program
notepad_text_editor_program()
