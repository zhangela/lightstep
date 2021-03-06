from log_searcher import search

logs = [
    {
        "service": "service_A",
        "level": "INFO",
        "timestamp": "2017-10-17 00:00:00.000000",
        "operation": "transaction_A1",
        "transaction_id": "transaction_1",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "ERROR",
        "timestamp": "2017-10-17 00:00:00.089420",
        "operation": "transaction_A1",
        "transaction_id": "transaction_1",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "DEBUG",
        "timestamp": "2017-10-17 00:00:00.207697",
        "operation": "operation_B1",
        "transaction_id": "transaction_1",
        "message": "",
    },
    {
        "service": "serviceC",
        "level": "ERROR",
        "timestamp": "2017-10-17 00:00:01.038673",
        "operation": "operation_C1",
        "transaction_id": "transaction_1",
        "message": "",
    },
    {
        "service": "serviceC",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:01.384007",
        "operation": "operation_C1",
        "transaction_id": "transaction_1",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "DEBUG",
        "timestamp": "2017-10-17 00:00:02.271526",
        "operation": "operation_B1",
        "transaction_id": "transaction_1",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:02.637356",
        "operation": "transaction_A1",
        "transaction_id": "transaction_1",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "DEBUG",
        "timestamp": "2017-10-17 00:00:01.384007",
        "operation": "operation_A2",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "DEBUG",
        "timestamp": "2017-10-17 00:00:01.418445",
        "operation": "operation_B2",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "DEBUG",
        "timestamp": "2017-10-17 00:00:02.363259",
        "operation": "operation_A2",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "INFO",
        "timestamp": "2017-10-17 00:00:02.636262",
        "operation": "operation_B1",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:03.089420",
        "operation": "operation_B1",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "ERROR",
        "timestamp": "2017-10-17 00:00:03.890186",
        "operation": "operation_A2",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:04.615705",
        "operation": "operation_B2",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:05.475280",
        "operation": "operation_A2",
        "transaction_id": "transaction_2",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "ERROR",
        "timestamp": "2017-10-17 00:00:03.089420",
        "operation": "transaction_A1",
        "transaction_id": "transaction_3",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:03.571104",
        "operation": "operation_B1",
        "transaction_id": "transaction_3",
        "message": "",
    },
    {
        "service": "serviceC",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:04.269296",
        "operation": "operation_C1",
        "transaction_id": "transaction_3",
        "message": "",
    },
    {
        "service": "serviceC",
        "level": "WARNING",
        "timestamp": "2017-10-17 00:00:04.842602",
        "operation": "operation_C1",
        "transaction_id": "transaction_3",
        "message": "",
    },
    {
        "service": "serviceB",
        "level": "INFO",
        "timestamp": "2017-10-17 00:00:05.314284",
        "operation": "operation_B1",
        "transaction_id": "transaction_3",
        "message": "",
    },
    {
        "service": "service_A",
        "level": "DEBUG",
        "timestamp": "2017-10-17 00:00:05.763280",
        "operation": "transaction_A1",
        "transaction_id": "transaction_3",
        "message": "",
    },
]


def test_search_max_error_operation():
    assert "transaction_A1" == search(logs, "maxErrorOperation")

def test_search_longest_transaction():
    assert "transaction_2" == search(logs, "longestTransaction")
