## Command project by OTA Team

## Personal assistant
This project represents the implementation of a personal assistant with a command line interface (CLI). 
The project is installed as a Python package and can be called anywhere in the system by the appropriate command after installation; <p>
This simple python app will help you to manage: 
_your address book_ , _your notes_ , _your list of task_ (with the responsible persons and deadlines), _sort files on your computer_ , _have rate of currency_ (used API website of NBU).

This project was written in the **OOP paradigm**, the following libraries were used: **re, datetime, pathlib, collections, shutil, prompt_toolkit, requests, pickle, pyttsx3**.
The address book, notes, task book save to **pickle** file.


### Installation

Download package, unpack it and use next command to install it from unpacked folder:

```bush
pip install -e .
```

### Calling

Launch command line and use command `assistant`

___

### Description

**Auto-completion of commands** in the command line will help you manage this application.

CLI Assistant can:

- [x] To __get short tips on__ how to use you can call `help` command at any time during your work with assistant

<p>

- [x] to __add new contact__ and one or more phones (for example 2 phones) use command: `add contact <name> <phone> <phone>`
- [x] to __remove contact__ use command: `remove contact <name>`

<p>

- [x] to __add phone to contact__ use command: `add phone <name> <one phone>`
- [x] to __change phone of contact__ use command: `change phone <name> <old phone> <new phone>`
- [x] to __remove phone of contact__ use command: `remove phone <name> <old phone>`

<p>

- [x] to __add e-mail to contact__ use command: `add email <name> <e-mail>`
- [x] to __change e-mail of contact__ use command: `change email <name> <new e-mail>`
- [x] to __remove e-mail of contact__ use command: `remove email <name>`

<p>

- [x] to __add address to contact__ use command: ` add address <name> <address> `
- [x] to __change address of contact__ use command: ` change address <name> <new address> `
- [x] to __remove address of contact__ use command: ` remove address <name> `

<p>

- [x] to __add birthday of contact__ use command: ` add birthday <name> <dd/mm/yyyy> `
- [x] to __remove birthday__, write command: ` remove birthday <name> `
- [x] to __change birthday__, write command: ` change birthday <name> <dd/mm/yyyy>`
- [x] to __see how many days to contact's birthday__ use command: `days to birthday <name>`
- [x] to __see list of birthdays in period__ (sorted by days of birthday) use command: `birthdays <number of days>`

<p>

- [x] to __search contacts__ with < text to search > use command: `search contacts <text to search>`
- [x] to __see full record of contact__ use command: ` phone <name> `
- [x] to __see all contacts__ use command: `show addressbook`
- [x] to __say goodbye__ use one of these commands: `good bye` or `close` or `exit` or ` . `
- [x] to __say hello__ use command: `hello`

___

### Personal notes script

<p> This script can manage personal notes.</p>

- [x] to __add note__ use command:  `add note <text>`
- [x] to __edit note__ use command:  `change note <id> <edited text>`
- [x] to __add tags__ use command:  `add tags <id> <tag1 tag2 tag3...>`
- [x] to __see all notes__ use command: `show notes`
- [x] to __see and listen any note__ use command: `note <id>`
- [x] to __delete note__ use command: `remove note <id>`
- [x] to __search notes__ use command: `search notes <text_to_search>`
- [x] to __search tags__ use command: `search tags <tag_to_search>`

___

### List of task

<p> This script can manage list of task with deadlines and responsible persons.</p>

- [x] to __add task__ use command:  `add task <name of responsible persons> <deadline in format dd/mm/yyyy> <text of task>`
- [x] to __remove task__ use command:  `remove task <ID of task>`
- [x] to __see all tasks__ use command: `show tasks`
- [x] to __change deadline of task__ use command: `change deadline <ID of task> <new deadline in format dd/mm/yyyy`
- [x] to __search tasks__ use command: `search tasks <text_to_search>`
- [x] to __search tasks of responsible person__ use command: `responsible person <name>`

___
<p>

- [x] to __see rate of currency__ today use command: `currency <name of currency>` 


___

### Clean-folder script

<p> This script can sort all files in the folder. The script sorts all files according to file's extensions.</p>

- [x] to __sort files in folder__ use command: `clean-folder <path to folder>`

...

- [ ] if this folder is not exists, you'll see a message in console.
- [ ] The script sorts files according to file's extensions and replaces files to the destination folders.
- [ ] Default destination folders are `documents`, `images`, `video`, `music`, `archives` and `unknown`.
- [ ] if you want to set your own rules of sorting files you have to change **extensions** dict:

  ```python
  extensions = {
    "images": ['.jpeg', '.png', '.jpg', '.svg'],
    "video": ['.avi', '.mp4', '.mov', '.mkv'],
    "documents": ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    "music": ['.mp3', '.ogg', '.wav', '.amr'],
    "archives": ['.zip', '.gz', '.tar'],
    "unknown": [""]
    }
  ```

- [ ] All files with relevant extensions will be moved to these folders;
- [ ] if these folders were not exist it will be created;
- [ ] The script recursively checks all subfolders and replaces all files to destination folders;
- [ ] Empty folders will be deleted;
- [ ] Files with Cyrillic name will be **renamed to Latin name**;
- [ ] if subfolders involve the files with the same name, these files will be renamed - **date-time will be added to file's name**;
- [ ] All archives will be unpacked to subfolder with the name as archive's name in folder `archive`;
- [ ] if archive is broken, script will continue its work without unpacking this archive. In console you'll see message about this broken archive;
- [ ] When script finishes cleaning the folder, you'll see the report.

___


### Our TEAM:
<p> 
Oleksandr Gnatiuk (Team Lead) <p>
Anastasiia Kholodko (Scrum Master) <p>
Oleg Veisa <p>
Artem Danilov<p>
Tatiana Maximenko

