#!/bin/bash
set -e

echo "Actualizando paquetes..."
sudo apt update && sudo apt upgrade -y

echo "Instalando dependencias base..."
sudo apt install -y git vim docker.io python3 python3-pip curl unzip

echo "Habilitando y arrancando Docker..."
sudo systemctl enable docker
sudo systemctl start docker

echo "Versiones instaladas:"
git --version
vim --version | head -n 1
docker --version
python3 --version
pip3 --version

echo "Instalación completada correctamente."
