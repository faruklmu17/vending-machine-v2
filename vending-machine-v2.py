import tkinter as tk

root = tk.Tk()
root.title("Vending Machine")

name_label = tk.Label(root, text="Type Your Name-",bg="Black",fg="white")
name_entry = tk.Entry(root)

display_label = tk.Label(root, text="")
continue_button = tk.Button(root, text="Continue",bg="Orange")

# save the name 


def display():
  name = name_entry.get()
  
  display_label.config(text="Hello, " +name+" !\nWelcome to X's Vending Machine!")
  vending_machine()
  

continue_button.config(command=display)

name_label.pack()  # To display the label in the window
name_entry.pack()

continue_button.pack()
display_label.pack()

def vending_machine():
    # coke label
    coke_label = tk.Label(root, text = "Product Code for Coke - 1001 ($2.50)")
    coke_label.pack()
    
    #KitKat label
    kitkat_label = tk.Label(root, text = "Product Code for Kitkat - 1002 ($1.75)")
    kitkat_label.pack()
    
    
    
    #product code label
    product_code_label = tk.Label(root, text = "Enter Product Code:")
    product_code_label.pack()
    
    #product code entry
    user_code = tk.Entry(root)
    user_code.pack()
    
    #product price label
    product_price_label = tk.Label(root, text = "Enter Inserted Money ($):")
    product_price_label.pack()
    
    #product price entry
    user_amount = tk.Entry(root)
    user_amount.pack()
    
    #Process button
    process_button = tk.Button(root, text = "Process",bg="Green")
    process_button.pack()
    
    # display label 
    display_label = tk.Label(root,text="")
    display_label.pack()
    
    def vending_machine():
      code = user_code.get()
      amount = user_amount.get()
      if code == "1001" and amount == "2.50":
        display_label.config(text="Paid! Coke is dispensing!",fg="green")
      elif code == "1002" and amount == "1.75":
        display_label.config(text="Paid! KitKat is dispensing!",fg="green")
      else: 
        display_label.config(text="Sorry, incorrect amount/code. Please try again!",fg="red")
    
    process_button.config(command=vending_machine)
  



#Mainloop
root.mainloop()
