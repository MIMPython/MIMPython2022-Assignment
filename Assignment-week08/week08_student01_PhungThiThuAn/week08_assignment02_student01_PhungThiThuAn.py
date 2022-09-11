import time
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

    >>> A = np.array([[1, 3], [3, 2]])
    >>> b = np.array([4, 5])
    >>> x = solveLE(A, b)
    >>> print(x)
   [1.,  1.]

    Check that the solution is correct:

    >>> np.allclose(np.dot(A, x), b)
    True
    
    """
    try:
        x = np.dot(np.linalg.inv(A),b)
        return x
    except ValueError:
        return "can't solve"

if __name__ == '__main__':
    A = np.array([[1, 2, 0], [3, 5, 2], [3, 0, 9]])
    b = np.array([8, 5])
    # print(solveLE(A, b)) # can't solve

    A = np.array([[1, 2, 0], [3, 5, 2], [3, 0, 9]])
    b = np.array([8, 5, 12])

    myFuncStartTime = time.time()
    result1 = solveLE(A, b)
    myFuncEndTime = time.time()
    myFuncRunTime = myFuncEndTime - myFuncStartTime
    print("My function:", result1, myFuncRunTime)

    npFuncStartTime = time.time()
    result2 = x2 = np.linalg.solve(A, b)
    npFuncEndTime = time.time()
    npFuncRunTime = npFuncEndTime - npFuncStartTime
    print("Numpy's function:", result2, npFuncRunTime)
    # My function: [106. -49. -34.] 0.0020303726196289062
    # Numpy's function: [106. -49. -34.] 0.0002474784851074219