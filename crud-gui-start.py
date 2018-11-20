import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer info',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            LookGUI(self.master)
        elif self.radio_var.get() == 2:
            AddGUI(self.master)
        elif self.radio_var.get() == 3:
            ChangeGUI(self.master)
        else:
            DeleteGUI(self.master)


class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Email: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Add customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.add_label = tkinter.Label(self.top_frame, text='Enter customer name to add: ')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)
        self.add2_label = tkinter.Label(self.middle_frame, text='Enter customer email to add: ')
        self.add2_entry = tkinter.Entry(self.middle_frame, width=15)

        # pack top frame
        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')
        self.add2_label.pack(side='left')
        self.add2_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame)
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add(self):
        name = self.add_entry.get()
        email = self.add2_entry.get()
        if name not in self.customers:
            self.customers[name] = email
            save_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, save_file)
            save_file.close()
            tkinter.messagebox.showinfo("Name added", "The selected name has been added.")
        else:
            print("Error")

    def back(self):
        self.look.destroy()


class ChangeGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Change customer info')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.change_label = tkinter.Label(self.top_frame, text='Enter customer name to change: ')
        self.change_entry = tkinter.Entry(self.top_frame, width=15)
        self.change2_label = tkinter.Label(self.middle_frame, text='Enter new email: ')
        self.change2_entry = tkinter.Entry(self.middle_frame, width=15)

        # pack top frame
        self.change_label.pack(side='left')
        self.change_entry.pack(side='left')
        self.change2_label.pack(side='left')
        self.change2_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame)
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.change_button = tkinter.Button(self.bottom_frame, text='Change', command=self.change)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.change_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def change(self):
        name = self.change_entry.get()
        email = self.change2_entry.get()
        if name in self.customers:
            self.customers[name] = email
            save_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, save_file)
            save_file.close()
            tkinter.messagebox.showinfo("Name changed", "The selected name has been changed.")

        else:
            print("Error")

    def back(self):
        self.look.destroy()


class DeleteGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Delete customer info')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.del_label = tkinter.Label(self.top_frame, text='Enter customer name to delete: ')
        self.del_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.del_label.pack(side='left')
        self.del_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame)
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.del_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.del_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete(self):
        name = self.del_entry.get()
        if name in self.customers:
            del self.customers[name]
            save_file = open("customer_file.dat", 'wb')
            pickle.dump(self.customers, save_file)
            save_file.close()
            tkinter.messagebox.showinfo("Name deleted", "The selected name has been deleted.")
        else:
            print("Error")

    def back(self):
        self.look.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    root.geometry("300x150")
    # call the GUI and send it the root menu
    CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
