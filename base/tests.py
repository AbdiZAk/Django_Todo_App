from django.test import TestCase
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '../todo_app/.env')
load_dotenv(dotenv_path)\

name = f'{str(os.getenv("NAME"))}'

print(name)
