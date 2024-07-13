> ⚠️ Due to a lack of time, I abandoned this project and no longer own the domain kudos-box.com.

# Kudos-box
Source code of  [kudos-box.com](http://kudos-box.com)

AAt work, we had a cardboard box where we could leave anonymous notes to praise other colleagues. It was called the Kudos Box, and that was the origin of the idea for this project.

I tried to find a digital alternative to it, but since I couldn’t find anything suitable, I decided to create it myself.
Well, I probably just wanted to write some code, and that was a good excuse for me to do it 😅.

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

- Create the demo box (not password restricted):
```docker-compose run --rm django /app/manage.py create_demo_box ```
  
### Useful commands
- Run the tests:
```docker-compose run --rm django /app/manage.py test ```

- Black:
```docker-compose run --rm django black . ```

- Isort:
```docker-compose run --rm django isort . ```

### To-dos
- Notify box members via email when a new message arrives

