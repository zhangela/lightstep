# LightStep Take Home

## HOW TO RUN:

1. cd into lightstep directory
2. (optional) start virtual env: virtualenv -p /usr/local/bin/python3 .
3. (optional) activate the virtual env: source ./bin/activate
4. Install the required packages: pip3 install -r requirements.txt

Then:

### Correct test cases, expect correct output

~~~
$ ./parse_log.py --help
usage: parse_log.py [-h] [--file FILE] --criteria
                    {maxErrorOperation,longestTransaction}

Parse logs and answer questions.

optional arguments:
  -h, --help            show this help message and exit
  --file FILE           Log file in JSON that contains all logs, default:
                        input.json
  --criteria {maxErrorOperation,longestTransaction}
                        The search criteria, e.g. maxErrorOperation,
                        longestTransaction
~~~

~~~
$ ./parse_log.py --criteria longestTransaction
0eecc4a2-d7e6-4413-b86e-ea4c18b8e2a4
~~~

~~~
$ ./parse_log.py --criteria maxErrorOperation
GET
~~~

~~~
$ ./parse_log.py --criteria maxErrorOperation --file input.json
GET
~~~

### Incorrect test cases, expect exception

~~~
$ ./parse_log.py --criteria maxErrorOperation --file input.txtusage: parse_log.py [-h] [--file FILE] --criteria CRITERIA
parse_log.py: error: argument --file: can't open 'input.txt': [Errno 2] No such file or directory: 'input.txt'
~~~

~~~
$ ./parse_log.py --criteria wrongCriteria
usage: parse_log.py [-h] [--file FILE] --criteria
                    {maxErrorOperation,longestTransaction}
parse_log.py: error: argument --criteria: invalid choice: 'wrongCriteria' (choose from 'maxErrorOperation', 'longestTransaction')
~~~
### Unit tests:

To run unit tests:
~~~
$ nosetests test_log_searcher.py
~~~

## KEY DESIGN DECISIONS:

### API

I decided the API would expose `--criteria maxErrorOperation` to the user, and for each new supported search criteria, we would need to implement a new function like those in `SEARCH_CRITERIA_FUNCTIONS`. Given the currently limited # of search criteria, I think this is acceptable. However, in the future, we might want to make this more extensible.

One way of making this more extensible is to process transactions data into a dataframe-like object and expose a SQL-like interface, where each additional entry in `SEARCH_CRITERIA_FUNCTIONS` would just be a simple SQL query, which would reduce the amount of boilerplate code significantly.

### Processing Logs

Currently, we do a first round process of the logs by grouping them into transactions, and then each function in `SEARCH_CRITERIA_FUNCTIONS` does a second round search over the minimally processed logs within each transaction. If we know the types of search criteria we need to support ahead of time, the first round process can do more work and summarize logs within each transaction, instead of keeping the raw list of logs.

### Storing Logs

The current design is not storing any logs because we are assuming each time we run this function, we might be running over totally new input log files. If we expect to run many searches over the same log file, or if the log file is very very large, we can do more pre-processing / caching.

## EVALUATION:

I recommend reading in order of: `parse_log.py` -> `log_searcher.py` -> `test_log_searcher.py` for ease of understanding.

I spent around 3 hours on the assignment.
