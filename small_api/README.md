## Rest API task

#### API
Please design and implement a REST API which would be able to perform the following operations:
 - Insert a new job offer (e.g. `POST /offers`)
 - Update an existing job offer (e.g. `PUT /offers/<id>`)
 - List all job offers, with pagination (e.g `GET /offers?skip=<a>&limit=<b>`)
 - Retrieve locations and categories with most of jobs, ordered by # of job offers. Expected format:
 ```javascript
 {
   "location1": ["category1", "category2"],
   "location2": ["category3"]
 }
 ```

#### Structure
Job offer structure should include:
- Title
- Description
- Company
- Location
- Job Category


## Infos
- I decided to use Tastypie since I already know it, in the beginning I tried to set it up with Flask but that wasn't one of my best ideas.
- URLs you can/should use:
  - /api/v1/offer/?format=json
  - /api/v1/offer/1/?format=json
  - /api/v1/offer?limit=25&offset=50&format=json
  - /api/v1/offer/overview/?format=json
- doing it in Postman was the best and easiest way for me
- example how to send data:
  - {"title": "Python Backend Developer","description": "more info","company": "Startup","location": "Berlin","category": "IT"}
- setup:
  - install requirements
  - run migrations
