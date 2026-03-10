from setuptools import setup, find_packages

setup(
    name='neo-assistant',
    version='1.0.0',
    description='Personal Assistant CLI App for managing contacts and notes.',
    author='Group-5',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            # Цей рядок означає: при введенні команди neo-assistant в терміналі, 
            # запусти функцію main() з файлу main.py у пакеті neo_assistant
            'neo-assistant = neo_assistant.main:main',
        ],
    },
)