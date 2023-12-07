# letsbloom
Letsbloom API assignment

Running the application:

1) Install Flask and Flask-SQLAlchemy:
code: pip install Flask Flask-SQLAlchemy

( "virtualenv venv" and ".\venv\Scripts\activate" to run in virtual environment)

2) Run the application:
code: python app.py

The API will be accessible at http://127.0.0.1:5000/.



Seeding the Database with mockdata: 

1) Run the seed script:
code: python seed.py

This will populate the database with mockdata




API Documentation:


1) Retrieve All Books (GET /api/books):

Description: Retrieve a list of all books in the library.
Request: GET /api/books

Ex: Right now on my local host I can get all the books at : http://127.0.0.1:5000/api/books


2) Add a New Book (POST /api/books):

Description: Add a new book to the library.
Request: POST /api/books
 
Ex: On my Powershell I can post a new book by this command: Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/books" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"title": "New Book", "author": "New Author"}'

You can use POSTMAN for this or bash commands(curl) as well.


3) Update Book Details (PUT /api/books/{id}):

Description: Update the details of a specific book in the library.
Request: PUT /api/books/{id}

Ex: I'm using this command on Powershell : Invoke-RestMethod -Method PUT -Uri "http://127.0.0.1:5000/api/books/6" -Headers @{"Content-Type"="application/json"} -Body '{"title": "Updated Book Title", "author": "Updated Author"}'

Like above you can use POSTMAN or bash(CURL) to PUT as well

4) Delete Book (DELETE /api/books/{id}):

Description: Deletes the specific book in the library, This is not needed according to the requirements of the assignment. But did it just for the sake of it. 
Request: DELETE /api/books/{id}

Additional Notes:
I also wanted to write the code where I can get the ID of any book using title or author(So it becomes easier to Update an existing book or delete a specific book), since it's out of scope didn't write it.

I also tried to solve the DevOPs question, but couldn't do it in limited time. This is the docker file I could come up with:

# Stage 1: Build the Go application
FROM golang:1.21.3-alpine AS build
LABEL stage=builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o app

# Stage 2: Create a minimal image to run the application
FROM alpine:latest
WORKDIR /app
COPY --from=build /app/app .
EXPOSE 8080
CMD ["./app"]

Author:
Rajesh Narravula(2014CE10360).









