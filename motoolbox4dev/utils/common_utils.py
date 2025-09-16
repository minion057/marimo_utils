import marimo as mo

from motoolbox4dev.decorators.public_decorator import *

@public
def stderr_print(msg, **kwargs):
    """
    Output messages with the standard error output redirected.

    Parameters
    ----------
    msg : str
        Message to print.

    kwargs : dict
        Additional keyword arguments passed to print().

    Notes
    -----
    This function redirects standard error output while printing.
    If desired, you can clear the output window using `mo.output.clear()`.
    """
    with mo.redirect_stderr():
        print(msg, **kwargs)
