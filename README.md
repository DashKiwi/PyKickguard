# PyKickGuard

PyKickGuard is a simple piece of software to allow you to not get kicked for inactivty. Just make sure to use it for programs that allow you use this type of software. I am not liable for any negative effects you may cause when using this software.

## Installation

You can either run the setup.bat file found in the top folder (will ask for administrator) of the repository or manually download the required library's below.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed library's.

for Windows:
```bash
pip install keyboard
```

for Linux:
```bash
sudo pip install keyboard
```
Note: sudo is required for the keyboard library because it is accessing the lower levels of the computers input system which Linux doesnt allow. 

## Usage
To automatically start it you can run the Start.bat file which will start the program (reccomend a shortcut) or run the code below in the terminal to start it manually

```bash
cd yourdrive:\pathtofolder
python Main.py
```
alternatively you could run the python file in your own IDE. Whatever you do it is up too you!
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
