# Reach Out: A mental health counselor tracker app

This is the API repository for Reach Out. User's can view and add mental health counselors in order to keep track of them.

### Important Links

- [Client Repo](https://github.com/miriam-ogbamichael/reach-out-client)
- [Deployed Client](https://miriam-ogbamichael.github.io/reach-out-client/#/)
- [Deployed API](https://git.heroku.com/reach-counselors-api.git)

### Planning Story

I began by brainstorming an idea to combine mental health and tech. Reach Out is an application that users can use to keep track of mental health counselors that they come accross that they would like to stock pile as their own personal database. Reach Out allows users to `CRUD` onto `counselors`. The first steps to accomplishing version one (V1) of Reach Out was to make an ERD and a wireframe. Afterwards, I connected the Django API back-end with the React Auth front-end and began coding in the `CRUD` routes and end-points for the `counselors`. By testing each `CRUD` command and using `console.log()` every step of the way, I verified the applications functionality. It has a long way to go before it is completed but this is the MVP of Reach Out's V1.

### User Stories

- As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.
- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
- As a signed in user, I would like to see all of the listed counselors.
- As a signed in user, I would like to create a counselor.
- As a signed in user, I would like to update a counselor I have created.
- As a signed in user, I would like to delete a counselor I have created.

### Technologies Used

- Python
- Django
- HTML/CSS
- Javascript

### Unsolved Problems

- Allowing signed in users to `view` counselors they have created
- Implement `Favorite` functionality
- Implement `Contacted` functionality to track `Contacted` counselors
- Adding `Img` of counselors to display when users `CRUD` on counselors


### API Routes

## Counselor Routes

| Verb   | URI Pattern              | Controller#Action    |
|:-------|:----------------         |:------------------   |
| GET    | `/counselors/`             | `counselors#index`     |
| POST   | `/counselors/`             | `counselors#create`    |
| GET    | `/counselors/:sessionId`   | `counselors#show`      |
| PATCH  | `/counselors/:sessionId`   | `counselors#update`    |
| DELETE | `/counselors/:sessionId`   | `counselors#delete`    |



## Auth Routes

| Verb   | URI Pattern        | Controller#Action          |
|:-------|:----------------   |:------------------         |
| POST   | `/sign-up`         | `users#sign-up`            |
| POST   | `/sign-in`         | `users#sign-in`            |
| DELETE | `/sign-out`        | `users#sign-out`           |
| PATCH  | `/change-pw`       | `users#change-password`    |



### ERD and Wireframs

- Reach Out ERD:
(https://docs.google.com/document/d/1hs9TZIhWu1fxZ5eOaOgoginVn3-xQQzq-DCaqP-EkFg/edit?usp=sharing)

- Reach Out Wireframs:
(https://docs.google.com/document/d/1JG2E0nUtYsjZ-Wb7NCXP2lNDMb4-5iFc4i8pJjHX3-4/edit?usp=sharing)
