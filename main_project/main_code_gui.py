import tkinter as tk
from tkinter import messagebox
import os

category_restaurant = {
    'Italian': [
        {"Name": 'Bistrô Porto', "Price": "3/5", "Rating": "5/5", "Address": "Rua Padre Cruz, 150"},
        {"Name": 'Amatriciana', "Price": "2/5", "Rating": "4/5", "Address": "Rua Afonso Aveiro, 2"},
        {"Name": 'Buona Cucina', "Price": "1/5", "Rating": "2/5", "Address": "Avenida Comandante Valódia, 7"},
        {"Name": 'Gillardino Gourmet', "Price": "4/5", "Rating": "5/5", "Address": "Rua do Ouro, 8"}
    ],
    'Japanese': [
        {"Name": 'Sushi House', "Price": "3/5", "Rating": "4/5", "Address": "Rua das Aves, 15"},
        {"Name": 'Sushi Bar', "Price": "1/5", "Rating": "2/5", "Address": "Rua do Sol, 5"},
        {"Name": 'Sushi Garden', "Price": "2/5", "Rating": "3/5", "Address": "Rua da Pasteleira, 10"},
        {"Name": 'Sushi Time', "Price": "4/5", "Rating": "5/5", "Address": "Rua da Prata, 56"}
    ],
    'Mexican': [
        {"Name": 'El Mariachi', "Price": "1/5", "Rating": "2/5", "Address": "Rua das Tomatinas, 15"},
        {"Name": 'El Paso', "Price": "2/5", "Rating": "3/5", "Address": "Rua do Passo Largo, 10"},
        {"Name": 'El Camino', "Price": "3/5", "Rating": "4/5", "Address": "Rua do Caminho Longo, 5"},
        {"Name": 'El Burrito', "Price": "5/5", "Rating": "5/5", "Address": "Rua do Esperto, 2"}
    ],
    'Chinese': [
        {"Name": 'China House', "Price": "2/5", "Rating": "3/5", "Address": "Rua da Anémona, 15"},
        {"Name": 'China Garden', "Price": "1/5", "Rating": "1/5", "Address": "Rua do Jardim, 10"},
        {"Name": 'China Wok', "Price": "3/5", "Rating": "4/5", "Address": "Rua do Lago, 5"},
        {"Name": 'China Town', "Price": "4/5", "Rating": "5/5", "Address": "Rua do Areeiro, 2"}
    ],
    'Portuguese': [
        {"Name": 'Casa do Bacalhau', "Price": "3/5", "Rating": "4/5", "Address": "Rua do Zé do Pipo, 40"},
        {"Name": 'Casa do Mar', "Price": "2/5", "Rating": "3/5", "Address": "Rua das Camélias, 4"},
        {"Name": 'Casa do Pão', "Price": "1/5", "Rating": "2/5", "Address": "Rua António Farinha, 1"},
        {"Name": 'Casa do Chá', "Price": "4/5", "Rating": "5/5", "Address": "Rua Rainha Isabel II, 13"}
    ]
}

def show_restaurants(category):
    restaurants = category_restaurant.get(category)
    if restaurants:
        result_text = f"{category} restaurants in this zone:\n\n"
        for restaurant in restaurants:
            result_text += f"Name: {restaurant['Name']}\nPrice: {restaurant['Price']}\nRating: {restaurant['Rating']}\nAddress: {restaurant['Address']}\n\n"
        messagebox.showinfo(f"{category} Restaurants", result_text)
    else:
        messagebox.showwarning("Error", "Invalid category selected")

def restart():
    result = messagebox.askyesno("Restart", "Do you want to check another category?")
    if result:
        root.deiconify()
    else:
        root.quit()

root = tk.Tk()
root.title("Restaurant Recommendation System")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#BB9457")
#setting the relative path to the icon because the simple way root.iconbitmap("name of the file") was not working
script_dir = os.path.dirname(__file__)
icon_path = os.path.join(script_dir, "restaurant.ico")
root.iconbitmap(icon_path)

label = tk.Label(root, text="Choose a restaurant category:", font=("Arial", 14), bg="#BB9457")
label.pack(pady=20)

categories = ["Italian", "Japanese", "Mexican", "Portuguese", "Chinese"]
for category in categories:
    button = tk.Button(root, text=category, width=15, font=("Arial", 12),
                       command=lambda c=category: [show_restaurants(c), restart()], bg="#FEC89A")
    button.pack(pady=5)

root.mainloop()
