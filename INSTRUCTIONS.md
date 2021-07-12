>.
>## Starting the Next.js Server
>### Install Dependencies:
>```
>yarn install
>```
> Before you can start the server you'll need to set the following environment variables in the 
> next.config.js file in the root directory:
> ```
>module.exports  = {
>reactStrictMode: true,
>env: {
>GOV_DATA_BASE_URL: 'https://api.data.gov/ed/collegescorecard/v1/schools',
>API_KEY:'yourAppdata.govApiKey'
>SCHOOL_DATA_BASE_URL:'http://localhost:5000'
> }
>}
> ```
> ### Start the server:
> ```
> yarn start
> ```

>.
>## Pipenv Environment Manager For the Flask API
>[Pipenv Documentation](https://pipenv.pypa.io/en/latest/install/)
>You can use pip to install Pipenv
>[Install Instructions](https://pypi.org/project/pipenv/)
>```
>$ pip install --user pipenv
>```
>After install run:
>```
>$ pipenv shell
>```
>When shell is running, from the same terminal run:
>```
>$ pipenv install
>```
> This will install all the dependencies in the Pipfile
> You can now use all the normal python commands from inside the pipenv shell.
>## Starting Flask The Server
> Before you can start the server you'll need to set the following environment variables in a .env file
> ```
> BASE_URL='https://api.data.gov/ed/collegescorecard/v1/schools/'
> API_KEY='yourAppdata.govApiKey'
> ```
>While still in the pipenv shell run:
>```
>$ python main.py
>```
>The server should now be running on localhost:8000
>Open browser and navigate to localhost:8000
>
>## Using the API
> localhost:8000
>|endpoints| request | description  |
>|--|--|--|
>| /schools | GET  | Query Schools just as you would at https://api.data.gov/ed/collegescorecard/v1/schools/? |
>| /earnings-chart-data/:schoolId | GET  | returns student earnings data in the shape needed for the earnings bar chart on the frontend