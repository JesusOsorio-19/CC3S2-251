#!/usr/bin/env bash
echo "Introduce un número"
read num

if (( num % 2 == 0 )); then
  echo "$num es par"
else
  echo "$num es impar"
fi
