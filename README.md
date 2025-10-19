# TECH STORE STOCK AND SALES MANAGEMENT SYSTEM
This is a command-line application for managing, suppliers, products and sales. Built with **python** and **Click** for an interactive terminal experience.

## Features
- Manage suppliers and products
- Record product sales and auto-update stock
- generate monthly sales report
- data storage
- command-line interface with click

## Requirements
1. python 3.10+
2. SQLite3
3. pip
4. WSL(ubuntu)

## Project Structure
```bash
phase-3-project-IanNjuguna/
│
├── lib/
│   ├── cli.py                 
│   ├── database.py            
│   ├── helpers.py             
│   └── models/
│       ├── supplier.py        
│       ├── product.py         
│       └── sale.py            
│
├── main.py                    
├── requirements.txt           
└── README.md                  
```
## Installation and Set-up
### Clone the repository
```bash
git clone git@github.com:Ian-N-N/phase-3-project-IanNjuguna.git
cd phase-3-project-IanNjuguna
```
### create and activate virtual environment
```bash
pip3 install --user pipenv
pipenv install
pipenv shell
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### initialize the database
```bash
python main.py
```
## Running the application
use commands below from the project root
```bash
python main.py add-supplier
python main.py add-product
python main.py record-sale
python main.py view-suppliers
python main.py view-products
python main.py monthly-report
```
Each command asks you for input interactively e.g, product name

## Author
Ian Ngoru Njuguna
Phase 3 python project | TECH STORE STOCK AND SALES MANAGEMENT SYSTEM

