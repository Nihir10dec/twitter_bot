# twitter_bot
A bot which automatically likes the posts when given a keyword

For the code to work you need to have a twitter developer account which can be applied [Here](https://developer.twitter.com/en/apply-for-access).

From that you need to collect __API_TOKEN, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_TOKEN__ and put them as of these variables in a __.env__ file in the same directory of bot.py file

You .env file will look something like this
```
API_KEY = "put_your_value_here"

API_SECRET_KEY = "put_your_value_here"

ACCESS_TOKEN = "put_your_value_here"

ACCESS_SECRET_TOKEN = "put_your_value_here"
```

The arguments which will be provided to the main function will be ssearched on twitter and the resulting posts will be liked automatically for you and the console will show the output of it which will be like
```
Tweet with id - 1286204664673787906 has been liked
Tweet with id - 1286204669442703360 has been liked
Tweet with id - 1286204669748969473 has been liked
[{'code': 139, 'message': 'You have already favorited this status.'}]
Tweet with id - 1286204685335048192 has been liked
Tweet with id - 1286204686199074817 has been liked
```
You can change the error message according to your usecase, I have printed the original error message itself.

It will continue to go on and we have to manually stop the working of bot by pressing *Ctrl+C*
