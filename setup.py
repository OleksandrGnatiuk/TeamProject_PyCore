from setuptools import setup, find_packages

setup(name='assistant_ota',
      version='0.0.1',
      description='CLI Assistant helps to manage the address book, notes, task book, organizes file in folder',
      url='https://github.com/OleksandrGnatiuk/TeamProject_PyCore',
      author='Oleksandr Gnatiuk, Anastasiia Kholodko, Oleg Veisa, Artem Danilov, Tatiana Maximenko',
      author_email='oleksandr.gnatiuk@gmail.com, anakholodko@gmail.com, oleg.veisa@gmail.com, ar.dantess@gmail.com, tetianamaximenko1994@gmail.com',
      include_package_data=True,
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'markdown',
            'prompt_toolkit',
            'pyttsx3',
            'requests',
            ],
      entry_points={'console_scripts': ['assistant = cli_assistant.help_invite:short_help']})
