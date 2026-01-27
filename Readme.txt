The project has been created using pipenv.
To run the project:
1) Install pipenv: pip install pipenv
2) Activate pipenv shell: pipenv shell
3) Install project dependencies: pipenv install



API paths for testing:
- /restaurant/menu/         - all menu items
- /restaurant/menu/<id>/    - single menu item
- /restaurant/booking/      - show table bookings

Use default Djoser endpoints for user and token operations:
- /auth/users/              - get all users with GET, register new users with POST
- /auth/token/login/        - user login, token assigned
- /auth/token/logout/       - token revoked