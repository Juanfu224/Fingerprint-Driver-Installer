sudo apt purge fprintd libpam-fprintd "libfprint-2-*" -y
sudo apt install meson cmake libglib2.0-dev libgusb-dev libcairo2-dev libgirepository1.0-dev libnss3-dev libgudev-1.0-dev gtk-doc-tools valgrind git -y
git clone https://gitlab.freedesktop.org/libfprint/libfprint.git
cd libfprint
sudo meson builddir
sudo meson install -C builddir
sudo apt install fprintd libpam-fprintd -y
sudo pam-auth-update
fprintd-enroll -f right-index-finger
fprintd-verify
