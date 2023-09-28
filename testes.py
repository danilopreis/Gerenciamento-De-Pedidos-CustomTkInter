import sqlite3
my_conn = sqlite3.connect('sistema_gp_fusiontec.db')
###### end of connection ####

query="SELECT distinct(Projeto) as class FROM Pedidos"
r_set=my_conn.execute(query);
my_list = [r for r, in r_set] # create a  list

import tkinter as tk
my_w = tk.Tk()
my_w.geometry("250x200")  # Size of the window
my_w.title("www.plus2net.com")  # Adding a title

options = tk.StringVar(my_w)
options.set(my_list[0]) # default value

om1 =tk.OptionMenu(my_w, options, *my_list)
om1.grid(row=2,column=5)

my_w.mainloop()




'''import sqlite3

conn = sqlite3.connect("sistema_gp_fusiontec.db")
cur = conn.cursor()
cur.execute("SELECT Projeto from Pedidos")

rows = cur.fetchall()
print(rows)

result_list = [list(row) for row in rows]

print(result_list)

cur.close()
conn.close()'''
