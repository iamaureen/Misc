## makeCacheMatrix - his function creates a special "matrix" object that can cache its inverse.
## cacheSolve - his function computes the inverse of the special "matrix" returned by makeCacheMatrix above. 
## If the inverse has already been calculated (and the matrix has not changed), then the cachesolve should retrieve the 
## inverse from the cache.


makeCacheMatrix <- function(x = matrix()) {
  m <- null #initially inverse of function is null
  set <- function(y){
    x <<- y
    m <<- null
  }
  get <- function() x
  setInverse <- function(inverse){
    m <<- inverse
    return (m)
  }
  getInverse <- function() m
  list(set=set, get=get, setInverse=setInverse, getInverse=getInverse)

}



cacheSolve <- function(x, ...) {
       m <- x$getInverse # get the inverse matrix and check. if it is not calcluated, then calculate it
       if(!is.null(m)){
         message("found cached data")
         return (m)
       }
       #cached inverse not found, so inverse and return it
       data <- x$get()
       inverse <- solve(data)
       x$setInverse(inverse)
       inverse
}
