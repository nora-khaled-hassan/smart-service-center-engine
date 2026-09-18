# Smart Service Center Engine

A Python command-line application for managing service requests using Queue, Stack, Searching Algorithms, Sorting Algorithms, and a custom Hash Table.

This project was developed as part of **Samsung Innovation Campus - Chapter 4**.

## Features

* Add incoming service requests
* Automatically generate Request IDs
* Validate request data
* Manage waiting requests using Queue
* Process requests using FIFO
* Store processed requests
* Sequential Search
* Binary Search
* Custom Hash Table Lookup
* Search History using Stack
* Bubble Sort
* Selection Sort
* Insertion Sort
* Search statistics
* JSON data storage

## Request Data

Each service request contains:

* Request ID
* Customer Name
* Priority
* Estimated Time
* Status

Supported statuses:

* Pending
* Processed
* Closed
* Rejected

Priority values range from **1 to 5**.

## Data Structures

### Queue

The Queue is used to manage waiting requests using the **FIFO (First In, First Out)** principle.

Operations:

* `enqueue()`
* `dequeue()`
* `front()`
* `is_empty()`

### Stack

The Stack is used to store search history using the **LIFO (Last In, First Out)** principle.

Operations:

* `push()`
* `pop()`
* `peek()`
* `is_empty()`

### Hash Table

A custom Hash Table is used to store processed requests using the Request ID.

Operations:

* `hash()`
* `put()`
* `get()`

The Hash Table uses buckets to handle multiple keys with the same hash index.

## Searching Algorithms

### Sequential Search

Searches through processed requests one by one.

The program records:

* Found / Not Found
* Index
* Number of comparisons

### Binary Search

Binary Search is performed after sorting the processed requests by Request ID.

The program records:

* Found / Not Found
* Index when found
* Insert position when not found
* Number of comparisons

### Hash Lookup

Uses the custom Hash Table to find a processed request using its Request ID.

The search operation is also stored in the Search History Stack.

## Sorting Algorithms

The project includes three manual sorting algorithms:

* Bubble Sort
* Selection Sort
* Insertion Sort

The sorting functions support sorting by:

* Request ID
* Priority
* Estimated Time

Each sorting algorithm returns:

* Sorted data
* Number of comparisons
* Number of swaps or shifts
* Field used for sorting

## JSON Data

The initial service requests are stored in:

```text
service_data.json
```

The program loads the data when it starts.

## Project Structure

```text
Smart Service Center/
│
├── main.py
├── service_data.json
└── README.md
```

## How to Run

Make sure Python is installed on your computer.

Run the application using:

```bash
python main.py
```

The application runs through a command-line menu until the user selects **Exit**.

## Main Menu

```text
===== Smart Service Center =====
1. Add Incoming Request
2. Process Next Request
3. Show Waiting Queue
4. Show Processed Requests
5. Sort Requests
6. Sequential Search
7. Binary Search
8. Hash Lookup
9. View Last Search
10. Remove Last Search
11. Show Algorithm Statistics
12. Exit
```

## Basic Workflow

1. Add an incoming service request.
2. The request is added to the waiting Queue.
3. Process the next request using FIFO.
4. The processed request is added to the processed requests collection.
5. The processed request is also added to the Hash Table.
6. Search for requests using Sequential Search, Binary Search, or Hash Lookup.
7. Search operations are stored in the Search History Stack.
8. View or remove the last search operation.
9. View search statistics.

## Technologies

* Python
* JSON
* Queue
* Stack
* Sequential Search
* Binary Search
* Hash Table
* Bubble Sort
* Selection Sort
* Insertion Sort

## Project Type

**Individual Project**

Samsung Innovation Campus - Chapter 4
