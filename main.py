import math
import customtkinter


def calculate_soch_points(max_points, current_coof, targetCoof):
  soch_coof = 2 * targetCoof - current_coof 
  soch_points = math.ceil(round(soch_coof * max_points, 1))
  
  return soch_points


def calculate_current_coof(fo_points, sor1_points, sor2_points,
                           fo_max_points, sor1_max_points, sor2_max_points):
  current_coof = round(round(round(fo_points / fo_max_points, 1) / 2, 1) + \
  round(round(sor1_points / sor1_max_points, 1) / 4 + \
  round(sor2_points / sor2_max_points, 1) / 4, 1), 1)

  return current_coof


root = customtkinter.CTk()
root.title("Соч Calculator")
root.geometry("800x200")

customtkinter.set_default_color_theme("dark-blue")

fo_points_max_entry = customtkinter.CTkEntry(root, placeholder_text="Макс. балл ФО")
fo_points_max_entry.grid(column=0, row=0, padx=10, pady=5)
fo_points_entry = customtkinter.CTkEntry(root, placeholder_text="Факт. балл ФО")
fo_points_entry.grid(column=0, row=1, padx=10, pady=5)

sor1_points_max_entry = customtkinter.CTkEntry(root, placeholder_text="Макс. балл СОР1")
sor1_points_max_entry.grid(column=1, row=0, padx=10, pady=5)
sor1_points_entry = customtkinter.CTkEntry(root, placeholder_text="Факт. балл СО1")
sor1_points_entry.grid(column=1, row=1, padx=10, pady=5)

sor2_points_max_entry = customtkinter.CTkEntry(root, placeholder_text="Макс. балл СО2")
sor2_points_max_entry.grid(column=2, row=0, padx=10, pady=5)
sor2_points_entry = customtkinter.CTkEntry(root, placeholder_text="Факт. балл СО2")
sor2_points_entry.grid(column=2, row=1, padx=10, pady=5)

soch_points_max_entry = customtkinter.CTkEntry(root, placeholder_text="Макс. балл СОЧ")
soch_points_max_entry.grid(column=3, row=0, padx=10, pady=5)
soch_points_label = customtkinter.CTkLabel(root, text="Нужный балл СОЧ", 
                                           fg_color="transparent")
soch_points_label.grid(column=3, row=1, padx=10, pady=5)


def target_grade_optionmenu_callback(choice):
  if choice == "5":
    target_coof = 0.85
  elif choice == "4":
    target_coof = 0.65
  else:
    target_coof = 0

  try:
    soch_points = calculate_soch_points(int(soch_points_max_entry.get()),
    calculate_current_coof(int(fo_points_entry.get()),
                           int(sor1_points_entry.get()),
                           int(sor2_points_entry.get()),
                           int(fo_points_max_entry.get()),
                           int(sor1_points_max_entry.get()),
                           int(sor2_points_max_entry.get())
                          ),
                        target_coof)
    if (soch_points < 1):
      soch_points = 1
      
    if (soch_points > int(soch_points_max_entry.get())):
      soch_points_label.configure(text=f"Нужный балл СОЧ: {soch_points} (Невозможно)")
    else:
      soch_points_label.configure(text=f"Нужный балл СОЧ: {soch_points}")

  except ValueError:
    soch_points_label.configure(text="Введите число")


target_grade_label = customtkinter.CTkLabel(root, text="Целевая оценка")
target_grade_label.grid(column=0, row=2, padx=10, pady=5)

target_grade_optionmenu = customtkinter.CTkOptionMenu(root, values=["4", "5"],
   command=target_grade_optionmenu_callback)
target_grade_optionmenu.grid(column=0, row=3, padx=10, pady=5)


root.mainloop()
