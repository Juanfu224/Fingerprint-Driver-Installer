import os

# Elimina los paquetes fprintd y libpam-fprintd del sistema, junto con sus archivos de configuración.
os.system("sudo apt purge fprintd libpam-fprintd")

# Instala las herramientas y dependencias necesarias para compilar y trabajar con libfprint.
os.system("sudo apt install meson cmake libglib2.0-dev libgusb-dev libcairo2-dev libgirepository1.0-dev libnss3-dev libgudev-1.0-dev gtk-doc-tools valgrind")

# Clona el repositorio oficial de libfprint.
os.system("git clone https://gitlab.freedesktop.org/libfprint/libfprint.git")

# Configura la compilación del proyecto libfprint en un directorio llamado 'builddir'.
os.system("sudo meson builddir")

# Instala el proyecto libfprint desde el directorio de compilación 'builddir'.
os.system("sudo meson install -C builddir")

# Vuelve a instalar los paquetes fprintd y libpam-fprintd, necesarios para la autenticación de huellas dactilares.
os.system("sudo apt install fprintd libpam-fprintd")

# Actualiza la configuración de autenticación del sistema para aplicar los cambios de PAM (Pluggable Authentication Modules).
os.system("sudo pam-auth-update")

# Registra una huella digital (dedo índice derecho) en el sistema para la autenticación biométrica.
os.system("fprintd-enroll -f right-index-finger")
