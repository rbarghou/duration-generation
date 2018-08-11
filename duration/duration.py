import time


YIELD_TIME = "TIME"
YIELD_IDX = "IDX",
YIELD_ELAPSED = "ELAPSED"


def duration(seconds=1.0, yields=(YIELD_IDX,)):
    """
    Generates until `seconds` seconds have elapsed.

    example usage
    ```
    for i, t in duration(10.0, yields=(YIELD_IDX, YIELD_ELAPSED)):
        print("At iteration {} and {} seconds have elapsed".format(i, t))
        ...
    ```

    :param seconds: number of seconds to loop
    :param yields: Which values you would like your loop to yield
    Valid options are `YIELD_TIME`, `YIELD_IDX`, and `YIELD_ELAPSED`
    :return generator:
    """

    assert(len(yields) > 0)

    start_time = time.time()
    end_time = start_time + seconds
    now = time.time()
    idx = 0

    while now < end_time:
        now = time.time()
        payload = tuple(
            value
            for key, value in {
                YIELD_TIME: now,
                YIELD_ELAPSED: now - start_time,
                YIELD_IDX: idx
            }
            if key in yields
        )
        if len(payload) == 1:
            payload = payload[0]
        yield payload
        idx += 1
