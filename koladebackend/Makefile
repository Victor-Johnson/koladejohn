# Fastapi Makefile 

dev:
	ENV=development uvicorn main:app --reload

prod:
	ENV=production uvicorn main:app --host=0.0.0.0 --port=8000

test:
	ENV=testing uvicorn main:app --reload 

	