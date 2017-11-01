from collections import defaultdict
import operator
from datetime import datetime, timezone


def search(logs, criteria):
    """Search logs for a certain criteria.

    Args:
        logs: a json list of logs
        criteria: str, must be a key in the SEARCH_CRITERIA_FUNCTIONS dict
    """

    # NB: if we expect to perform many searches over the same list of
    # transactions, we can consider caching this.
    transactions = {}
    for log in logs:
        transaction_id = log['transaction_id']

        if transaction_id not in transactions:
            transactions[transaction_id] = Transaction(transaction_id)

        transactions[transaction_id].add_log(log)

    f = SEARCH_CRITERIA_FUNCTIONS[criteria]
    return f(transactions)


def get_max_error_operation(transactions):
    """Search plugin for getting operation with max errors.

    NB: if there are multiple operations with the same # of errors, we only
    return the first one.

    """
    operation_error_count = defaultdict(int)

    for transaction in transactions.values():
        operations_with_errors = set()
        for log in transaction.logs:
            if log.level == 'ERROR':
                operations_with_errors.add(log.operation)

        for operation in operations_with_errors:
            operation_error_count[operation] += 1

    # return the key of operation_error_count with the highest value
    return max(operation_error_count.items(), key=operator.itemgetter(1))[0]


def get_longest_transaction(transactions):
    """Search plugin for getting transaction with the longest duration.

    NB: if there are multiple transactions with the same duration, we only
    return the first one.

    """
    longest_transaction_id = None
    max_transaction_duration = None

    for transaction_id, transaction in transactions.items():
        start = None
        end = None

        for log in transaction.logs:
            if start is None or log.timestamp < start:
                start = log.timestamp

            if end is None or log.timestamp > end:
                end = log.timestamp

        # if for some reason, the start/end time is not valid, we just skip
        # this transaction instead of throwing an error
        if start is None or end is None:
            continue

        duration = end - start
        if (max_transaction_duration is None or
            duration > max_transaction_duration
        ):
            max_transaction_duration = duration
            longest_transaction_id = transaction_id

    return longest_transaction_id


# dict defining the allowed search criterias
SEARCH_CRITERIA_FUNCTIONS = {
    'maxErrorOperation': get_max_error_operation,
    'longestTransaction': get_longest_transaction,
}


class Transaction(object):
    """Object encapsulating a transaction."""
    def __init__(self, transaction_id):
        self.id = transaction_id
        self.logs = []

    def add_log(self, log_json):
        log = Log(log_json)
        self.logs.append(log)


class Log(object):
    """Object encapsulating a log entry."""
    def __init__(self, log_json):
        self.service = log_json['service']
        self.level = log_json['level']
        self.operation = log_json['operation']
        self.message = log_json['message']
        self.transaction_id = log_json['transaction_id']

        # convert the time into the more standard epoch milliseconds
        self.timestamp = self._convert_to_epoch(log_json['timestamp'])

    def _convert_to_epoch(self, time_str):
        """Convert string like "2017-10-17 00:00:01.038673" to epoch in ms."""
        pattern = '%Y-%m-%d %H:%M:%S.%f'
        # get local datetime obj
        local_dt = datetime.strptime(time_str, pattern)
        # convert local datetime obj to utc datetime obj
        utc_dt = local_dt.replace(tzinfo=timezone.utc)
        # get epoch time in milliseconds
        return utc_dt.timestamp() * 1000
