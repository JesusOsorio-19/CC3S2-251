#!/usr/bin/env bash
a=7; b=3
echo "$a + $b = $((a + b))"
echo "$a ** $b = $((a ** b))"

# Sustitución de comandos
fecha=$(date +%Y-%m-%d)
archivos=$(ls | wc -l)
echo "Hoy: $fecha, Archivos: $archivos"

VAR=""
echo "${VAR:-default}"       # default si VAR vacío
txt="archivo.tar.gz"
echo "${txt%.tar.gz}"        # quita sufijo
