@echo off
start cmd /k lt --port 3000 --subdomain front-end --allow-invalid-cert
start cmd /k lt --subdomain back-end --port 8000 --allow-invalid-certm