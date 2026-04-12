#!/bin/bash
set -e

LOG_DIR="/var/log"
DAYS=7

echo "Limpiando logs mayores a  días en  ..."
find "" -type f -name "*.log" -mtime + -delete

echo "Limpieza de logs completada correctamente."
