# python_assignment

## Background
Done as part of a interview home assignment in Python.

## Summary
The main purpose of the tool is to experience with APIs, Async jobs & DB in Python.

## APIs
* POST /upload
<br>The POST upload receives data in the following formart: {1:[5,7,2],2:[8,3,2],3:[2,5,1]}
<br>The API than needs to store the raw data in a table in the DB that have the following columns: id, raw_data, result
<br>and call an async celery job to calculate the result, which is the multiplication of the list of the numbers and store it in the result column. 

* GET /results/{result_id}
<br>The GET API fetches the result of result_id data from the DB.
