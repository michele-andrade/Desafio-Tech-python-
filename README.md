# Desafio-Tech-python-
Desafio Automação e Desenvolvimento de Software
### Como executar este projeto?

Abaixo terá os comandos necessários para executar este projeto. 
**Inicialmente cria-se uma máquina virtual**

python3 -m venv venv 

**Ativa-se essa máquina**

source venv/bin/activate

**Instalando o django e tkinter**

pip install django djangorestframework 
pip install tk

**Execuntado o projeto**

python manage.py migrate --run-syncdb 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 

