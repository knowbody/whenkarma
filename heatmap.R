library(rjson)


file_source <- 'prepared_data.json'
data <- fromJSON(file=file_source, method='C')

# single element of JSON
points_vector <- NULL
date_vector <- NULL

data_length <- length(data)

for (i in 1350:1721) {
  for (d in data[[i]]) {
    points_vector <- append(points_vector, as.numeric(d$points))
    date_vector <- append(date_vector, d$date)
  }
}

d <- structure(list(X = date_vector, Y = points_vector), .Names = c("X", "Y"), class = "data.frame")
require(MASS)
dens <- kde2d(d$X, d$Y)  #overrode default bandwidth
filled.contour(dens)