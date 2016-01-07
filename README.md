# EvalDocMaker
Application for creating physical therapy evaluation documents

Dependencies for this project include the following:
 - Python: openpyxl, datetime, json, webbrowser, wkhtmltopdf, and pdfkit
 - JavaScript: AngularJS

I want to take patient data from an .xlsx file, populate an HTML template of the evaluation document with that data, and output a pdf of the document.

My current plan is to create three modules.
The first will be a web service that retrieves patient data from an .xlsx file and exposes it.
The second will display an HTML template of the final document in the user's browser, populate it with patient data, and allow a user to edit parts of it.
The third will take the finalized HTML document as an input and output a pdf of the document.

I am making this a desktop app instead of a web app because I wanted to avoid having to deal with HIPAA regulations. For this repository, I am not using anyone's personal information. I have included sample .xlsx, html, header, and footer files to be used instead.
