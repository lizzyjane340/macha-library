# Macha Library

### [Video Demo](https://www.youtube.com/watch?v=puB21mO4Iws) beta version

## Description

Macha Library is a web application for contributing, browsing and learning from Computer Science and Programming related
online resources. The app was created for members of the Macha Discord server, and includes a user registration & login 
feature for existing members. To view Macha Library resources, or to contribute, login is required. Users then have the ability 
to add or delete resources. 

Resources, applicable categories for that resource, and associated data are also stored in a **SQLite3** database. Uploaded 
image files are stored as **blob** data within the database and are not uploaded to the server's file directory.

Visually, the web application is responsive to smaller viewport sizes. The front end was developed using **Bootstrap 5 CDN**, 
custom **CSS** and **Javascript**, **HTML5** and the **Jinja2** template engine, and a darkmode feature is enabled via the
**darkmode.js CDN**.

The back end is implemented entirely in **Python3** using the **Flask** framework.

Application features include:

- User registration
- User sessions
- user login/logout
- SQL database
- Resource contribution form
- Image upload facility
- Resource deletion 
- Text search
- Category search
- Darkmode.js widget
- Responsive design

## Installation

Use the Python package manager to install Flask. You will also need **python3**.

```bash
pip install flask
```

Clone this repository, **cd** into the local directory and run the application on your **localhost** by doing the following:

- cd macha-library
- install flask
- run flask

You may find it beneficial to run Macha Library in a **venv** environment.

## Contributing

Pull requests are welcome from members of the Macha server. If you are a member of the Macha Discord server, to contribute 
a CS related resource to the library itself, please go to the hosted application at:

[Python Anywhere](https://www.machalibrary.pythonanywhere.com/)

## Screenshots

![5B9B4E2A-55DA-4851-A5E5-51237C4EDC34_1_105_c](https://user-images.githubusercontent.com/75592024/135724564-24b916b5-f5e2-4dd1-b195-adefbd0486f6.jpeg)

![9B1E37CA-92F9-4C5D-B13D-05A19437B3C7_1_201_a](https://user-images.githubusercontent.com/75592024/135724387-93ca9cca-ae6d-4ead-bf64-75d5d9b87f8c.jpeg)

<img width="477" alt="C6D112E1-0E0F-484F-9E6F-86AF2C96F165" src="https://user-images.githubusercontent.com/75592024/135724396-0bf02bb4-a10d-43ae-be3d-7726f8926190.png">

![459874C4-D1FD-4DDB-8768-78AABCF64256_1_105_c](https://user-images.githubusercontent.com/75592024/135724527-982c9e12-153f-4e32-a0e9-39ba19231165.jpeg)

<img width="754" alt="636E04C2-068A-438C-BB6F-64C3E6F5D3E6" src="https://user-images.githubusercontent.com/75592024/135724502-f86bbfdb-7801-4f34-b405-de4695548cc2.png">

<img width="703" alt="659F947C-EC60-492D-909E-AE573E117DE3" src="https://user-images.githubusercontent.com/75592024/135726064-47a535aa-f114-458b-8e05-36f6d5cd766f.png">

![C5C8BD8C-57E4-47AF-9F4B-4BCD9C6FBF0E_1_201_a](https://user-images.githubusercontent.com/75592024/135724434-c6c5dad8-0117-4bc3-935e-0f6fb6800205.jpeg)

<img width="406" alt="84092911-FE01-4F31-BD92-3500828DB980" src="https://user-images.githubusercontent.com/75592024/135725526-578df835-3532-45fa-bc07-d900615f8a3c.png">

## Contact

[https://github.com/lizzyjane340](https://github.com/lizzyjane340/)





