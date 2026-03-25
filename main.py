from manager import RestaurantManager
from models import Ingredient, Recipe, Supplier
from pydantic import ValidationError

def manage_category(manager, category_name, model_class):
    while True:
        print(f"\n--- Zarządzaj {category_name.capitalize()} ---")
        print("1. Dodaj nowe")
        print("2. Wyświetl wszystko")
        print("3. Usuń element")
        print("4. Powrót do menu głównego")
        
        choice = input("Wybierz: ")
        
        if choice == '1':
            try:
                uid = int(input("Wprowadź ID: "))
                name = input("Wprowadź nazwę: ")
                
                if category_name == "ingredients":
                    stock = int(input("Poziom zapasów: "))
                    sup_id = int(input("ID dostawcy: "))
                    item = model_class(id=uid, name=name, stock_level=stock, supplier_id=sup_id)
                elif category_name == "recipes":
                    time = int(input("Czas przygotowania (min): "))
                    item = model_class(id=uid, name=name, prep_time_mins=time)
                elif category_name == "suppliers":
                    email = input("Email: ")
                    item = model_class(id=uid, name=name, email=email)
                
                manager.add_item(category_name, item)
                print(f"Pomyślnie dodano {name}!")
            except ValidationError as e:
                print(f"Błąd walidacji: {e}")
            except ValueError:
                print("Błąd: Proszę wprowadzić liczby dla ID i ilości.")

        elif choice == '2':
            items = manager.get_all(category_name)
            if not items:
                print(f"Nie znaleziono {category_name}.")
            for i in items:
                # Basic display logic
                details = f"ID: {i.id} | Nazwa: {i.name}"
                if hasattr(i, 'stock_level'): details += f" | Zapasy: {i.stock_level}"
                print(details)
        
        elif choice == '3':
            try:
                target_id = int(input(f"Wprowadź ID {category_name[:-1]} do usunięcia: "))
                manager.remove_item(category_name, target_id)
                print(f"Element {target_id} usunięty (jeśli istniał).")
            except ValueError:
                print("Błąd: Proszę wprowadzić poprawne numeryczne ID.")
        
        elif choice == '4':
            break

def main():
    manager = RestaurantManager()
    
    while True:
        print("\n🍴 SYSTEM INWENTARYZACJI RESTAURACJI 🍴")
        print("1. Składniki")
        print("2. Przepisy")
        print("3. Dostawcy")
        print("4. Zapisz i Wyjdź")
        
        choice = input("Wybierz kategorię: ")
        
        if choice == '1':
            manage_category(manager, "ingredients", Ingredient)
        elif choice == '2':
            manage_category(manager, "recipes", Recipe)
        elif choice == '3':
            manage_category(manager, "suppliers", Supplier)
        elif choice == '4':
            manager.save_data()
            print("Zmiany zapisane. Do widzenia!")
            break

if __name__ == "__main__":
    main()