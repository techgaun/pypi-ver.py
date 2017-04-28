# pypi-ver.py

## Installation and Usage

I had been using something like this for a while. Thought I would index it on github so that I can get it quickly when I change my system.

```shell
pip install -r requirements.txt
python pypi-ver.py requests
```

### Examples

```shell
python pypi-ver.py requests | head -n1 # the latest version

# add above to alias
alias pylatest="python pypi-ver.py requests | head -n1"
```

### System-wide install

```shell
sudo wget 'https://raw.githubusercontent.com/techgaun/pypi-ver.py/master/pypi-ver.py' -O /usr/bin/pypi-ver && sudo chmod +x /usr/bin/pypi-ver
```

## Other Methods
There are several ways to accomplish this but I wanted to be able to run something quick.
You can use [yolk](https://pypi.python.org/pypi/yolk) or use invalid version number in your pip install (eg. `pip install requests==234234`).
