library(rjson)

file_source <- 'prepared_data.json'
data <- fromJSON(file=file_source, method='C')

# single element of JSON
points_vector <- NULL
date_vector <- NULL

data_length <- length(data)

for (i in 1:365) {
  for (d in data[[i]]) {
    points_vector <- append(points_vector, as.numeric(d$points))
    date_vector <- append(date_vector, d$date)
  }
}

points <- points_vector
names(points) <- date_vector

plot(date_vector, points_vector)

# barplot(points)