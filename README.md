# Kudos-box
Source code of  [kudos-box.com](https://kudos-box.com)

At work we have a cardboard box in which we can leave notes anonymously 
to praise other colleagues. It is called Kudos-box and it is and the origin.
of this project. 

I tried to look for a digital alternative to it and since I couldn't find anything, 
I decided to create it myself.

Well, I probably want to write some code and I was looking for an excuse to do it 😅.

Features:
- create anonymous messages in a box 
- only members of a box are able to see the messages

![Kudos-box](https://github.com/abel-castro/kudos-box/blob/main/screenshot.jpg)

### Development setup
This project uses docker-compose for development. 
- Create a .env file from the template env_template_dev with the desired values.

- Build the development image: ```docker-compose build ```

- Run ```docker-compose up``` and go to http://0.0.0.0:8000
to see your runserver.

- Create a superuser:
```docker-compose run --rm django /app/manage.py createsuperuser ```

### To-dos
- Notify box members via email when a new message arrives

