from setuptools import setup, find_packages

setup(name='assistant_team_project',
      version='0.0.1',
      description='CLI Assistant helps to manage the address book, notes, task book, organizes file in folder',
      url='https://github.com/OleksandrGnatiuk/TeamProject_PyCore',
      author='Oleksandr Gnatiuk', 
      author_email='oleksandr.gnatiuk@gmail.com',
      include_package_data=True,
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'markdown',
            'prompt_toolkit',
            'pyttsx3',
            'requests',
            ],
      entry_points={'console_scripts': ['assistant = cli_assistant.assistant:main']})
