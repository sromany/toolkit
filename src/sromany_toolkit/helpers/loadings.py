import time

from tqdm import tqdm


def loading_bar(timerange: int = 100, step_sleep: float = 0.1) -> None:
    """
    Prints a loading bar in the shell with a range of <timerage> and a default step time sleep of 0.1

    Args:
        timerange:
        step_sleep:

    Returns: Nothing

    Example:
    """
    for i in tqdm(range(timerange)):
        time.sleep(step_sleep)
