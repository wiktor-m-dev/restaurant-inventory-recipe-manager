# Restaurant Inventory & Recipe Manager

A simple Command Line Interface (CLI) application for managing a restaurant's inventory, recipes, and suppliers. The project uses `pydantic` for robust data validation.

## Features
- **Ingredients:** Track stock levels and link to specific suppliers.
- **Recipes:** Manage recipes including their preparation times.
- **Suppliers:** Store supplier contact details with built-in email validation.
- **Persistence:** Automatically save and load data to a `restaurant_data.json` file.

## Requirements
- Python 3.x
- `pydantic`

## How to Run

1. Install the required dependencies:
   ```bash
   pip install pydantic
   ```
2. Start the application:
   ```bash
   python main.py
   ```