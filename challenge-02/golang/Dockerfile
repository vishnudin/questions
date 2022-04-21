FROM golang:1.12.0-alpine3.9
ARG ENV=dev
COPY . .
COPY file-${ENV}.txt file.txt
RUN go build server.go
CMD ["./server"]
