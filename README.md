# Waitlist
Django application implementing a waitlist. A waiter's rank in the waitlist is a combination of their signup date and how many others sign up using them as a referral.

## Building and running
To create a docker image named waitlist:
```
make build-docker
```

To run the above image:
```
make run-docker
```

Then, navigate to `localhost:8000/waitlist` to see the webpage. Once you join the waitlist, you can navigate to `localhost:8000/waitlist/waiter/<username>` to view your rank.

> :warning: This app runs using the Django development server and SQLite and should not be used for production applications.

## Testing
To run tests for the waitlist django app:
```
pip install -r requirements.txt
make test
```
