# Bài 1: Viết một file .py trong đó documentation/docstrings được trình bày theo một quy chuẩn tự chọn. Bổ sung type hint nếu có thể.

import numpy as np

def solveLE(A, b):
    """
    This method is used to solve a linear equation Ax=b.

    Parameters
    ----------
    A: numpy.ndarray
       Coefficient matrix.
    b: numpy.ndarray 
       Ordinate or "dependent variable" values.

    Returns
    -------
    result: numpy.ndarray
        Solution to the equation Ax = b.  Returned shape is identical to `b`.
    
    Raises
    ------
    LinAlgError
        If `a` is singular or not square.

    See Also
    --------
    numpy.linalg.solve : Similar function in NumPy.
    scipy.linalg.solve : Similar function in SciPy.

    Examples
    --------
    Solve the system of equations "x0 + 2 * x1 = 3" and "3 * x0 + 2 * x1 = 2":

    >>> A = np.array([[1, 2], [3, 2]])
    >>> b = np.array([3, 5])
    >>> x = solveLE(A, b)
    >>> print(x)
   [1.,  1.]

    Check that the solution is correct:

    >>> np.allclose(np.dot(A, x), b)
    True
    
    """
    x = np.dot(np.linalg.inv(A), b)
    return x

