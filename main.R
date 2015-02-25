library(rjson)

file_source <- 'prepared_data.json'
data <- fromJSON(file=file_source, method='C')

# single element of JSON
points_vector <- NULL
date_vector <- NULL

data_length <- length(data)

for (i in 1300:1721) {
  for (d in data[[i]]) {
    date_vector <- append(date_vector, as.numeric(d$date))
  }
}

print(max(table(date_vector)))


days <- expression(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)

barplot(table(date_vector), names.arg=days, cex.names=0.6, ylim=c(0, 1.5 * max(table(date_vector))))