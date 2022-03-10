# pylcars
Create easily Star Trek influenced LCARS user interfaces

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes..

### Prerequisites

You need some software to create your own LCARS display.
  * Python 3.x
  * PyQT5
  * xxhash
  * pyaudio

### Installing 

#### Debian based 
```
sudo apt-get update 
sudo apt-get -y upgrade
apt-get install python3 python3-pip portaudio19-dev python-qt5 python3-dev
pip install xxhash pyaudio
cd your_project_folder
git clone https://github.com/StowasserH/pylcars.git
cd pylcars
pip install -e .
```

## Development

Feel free to use and modify it, but please help me to improve it.

### Coding style

If you commit code pls try to format it in [PEP8](https://www.python.org/dev/peps/pep-0008/)


## Authors

* **Harald Stowasser** - *Initial work* - [StowasserH](https://github.com/StowasserH)

See also the list of [contributors](https://github.com/StowasserH/pylcars/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
