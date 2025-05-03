# Fingerprint-Driver-Installer
Automates the installation and configuration of fingerprint reader drivers on Linux. Tested on Linux Mint 22 (Wilma).

# Installation
```
sudo apt purge fprintd libpam-fprintd "libfprint-2-*" -y
sudo apt install meson cmake libglib2.0-dev libgusb-dev libcairo2-dev libgirepository1.0-dev libnss3-dev libgudev-1.0-dev gtk-doc-tools libssl-dev valgrind git -y
git clone https://gitlab.freedesktop.org/libfprint/libfprint.git
cd libfprint
sudo meson builddir
sudo meson install -C builddir
sudo apt install fprintd libpam-fprintd -y
sudo pam-auth-update
fprintd-enroll -f right-index-finger
fprintd-verify
```
# Credits
- Script Author: Juanfu224 --> https://github.com/Juanfu224
- Drivers Author: Tamer Hassan --> https://gitlab.freedesktop.org/thameruddin
- Inspired by: AmulyaX --> https://gist.github.com/AmulyaX ❤️
