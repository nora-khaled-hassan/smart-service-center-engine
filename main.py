import json

def load_data():
    try:
        with open("service_data.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open("service_data.json", "w") as file:
        json.dump(data, file, indent=4)

def generate_id(data):
    if len(data) == 0:
        return 1

    max_id = data[0]["id"]

    for item in data:
        if item["id"] > max_id:
            max_id = item["id"]

    return max_id + 1

def validate_request(request):
    if request["customer"].strip() == "":
        return False, "Customer name cannot be empty"

    if request["priority"] < 1 or request["priority"] > 5:
        return False, "Priority must be from 1 to 5"

    if request["time"] <= 0:
        return False, "Estimated time must be positive"

    if request["status"] not in ["Pending", "Processed", "Closed", "Rejected"]:
        return False, "Invalid status"

    return True, "Valid"

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.items[0]
        new_items = []

        for i in range(1, len(self.items)):
            new_items.append(self.items[i])

        self.items = new_items
        return item

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def show(self):
        if self.is_empty():
            print("Queue is empty")
            return

        for item in self.items:
            print(item)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = []

        for i in range(size):
            self.table.append([])

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash(key)

        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return

        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)

        for item in self.table[index]:
            if item[0] == key:
                return item[1]

        return None

def sequential_search(data, target):
    comparisons = 0

    for i in range(len(data)):
        comparisons += 1

        if data[i]["id"] == target:
            search_history.push({
                "id": target,
                "method": "Sequential Search",
                "result": "Found",
                "comparisons": comparisons
            })
            return i, comparisons

    search_history.push({
        "id": target,
        "method": "Sequential Search",
        "result": "Not Found",
        "comparisons": comparisons
    })

    return -1, comparisons

def binary_search(data, target):
    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if data[mid]["id"] == target:
            search_history.push({
                "id": target,
                "method": "Binary Search",
                "result": "Found",
                "comparisons": comparisons
            })
            return mid, comparisons

        if data[mid]["id"] < target:
            left = mid + 1
        else:
            right = mid - 1

    search_history.push({
        "id": target,
        "method": "Binary Search",
        "result": "Not Found",
        "comparisons": comparisons
    })

    return left, comparisons

def bubble_sort(data, field):
    arr = data.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comparisons += 1

            if arr[j][field] > arr[j + 1][field]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps

def selection_sort(data, field):
    arr = data.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j][field] < arr[min_index][field]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, comparisons, swaps

def insertion_sort(data, field):
    arr = data.copy()
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j][field] > key[field]:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons, shifts

def show_requests(data):
    if len(data) == 0:
        print("No requests found")
        return

    for item in data:
        print(
            "ID:", item["id"],
            "| Customer:", item["customer"],
            "| Priority:", item["priority"],
            "| Time:", item["time"],
            "| Status:", item["status"]
        )

def get_number(message):
    while True:
        try:
            return int(input(message))
        except:
            print("Please enter a number")

def sort_requests(data):
    if len(data) == 0:
        print("No processed requests")
        return

    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = input("Choose algorithm: ")

    print("1. Request ID")
    print("2. Priority")
    print("3. Estimated Time")

    field_choice = input("Choose field: ")

    if field_choice == "1":
        field = "id"
    elif field_choice == "2":
        field = "priority"
    elif field_choice == "3":
        field = "time"
    else:
        print("Invalid choice")
        return

    if choice == "1":
        result, comparisons, moves = bubble_sort(data, field)
        algorithm = "Bubble Sort"
    elif choice == "2":
        result, comparisons, moves = selection_sort(data, field)
        algorithm = "Selection Sort"
    elif choice == "3":
        result, comparisons, moves = insertion_sort(data, field)
        algorithm = "Insertion Sort"
    else:
        print("Invalid choice")
        return

    show_requests(result)

    print("Algorithm:", algorithm)
    print("Comparisons:", comparisons)
    print("Swaps/Shifts:", moves)

    sorting_history.append({
        "algorithm": algorithm,
        "field": field,
        "comparisons": comparisons,
        "moves": moves
    })

def show_search_statistics():
    if search_history.is_empty():
        print("No search operations")
        return

    for item in search_history.items:
        print(
            item["method"],
            "| ID:", item["id"],
            "| Result:", item["result"],
            "| Comparisons:", item["comparisons"]
        )

def show_sort_statistics():
    if len(sorting_history) == 0:
        print("No sorting operations")
        return

    for item in sorting_history:
        print(
            item["algorithm"],
            "| Field:", item["field"],
            "| Comparisons:", item["comparisons"],
            "| Swaps/Shifts:", item["moves"]
        )

def test_sort(data, name):
    print()
    print(name)

    result, c, s = bubble_sort(data, "id")
    print("Bubble:", c, "comparisons,", s, "swaps")

    result, c, s = selection_sort(data, "id")
    print("Selection:", c, "comparisons,", s, "swaps")

    result, c, s = insertion_sort(data, "id")
    print("Insertion:", c, "comparisons,", s, "shifts")

def test_datasets(data):
    if len(data) < 2:
        print("Need at least 2 requests")
        return

    sorted_data, c, s = insertion_sort(data, "id")

    reverse_data = []
    i = len(sorted_data) - 1

    while i >= 0:
        reverse_data.append(sorted_data[i])
        i -= 1

    nearly_data = sorted_data.copy()
    nearly_data[0], nearly_data[1] = nearly_data[1], nearly_data[0]

    random_data = data.copy()

    for i in range(len(random_data) - 1):
        j = (i * 3 + 2) % len(random_data)
        random_data[i], random_data[j] = random_data[j], random_data[i]

    test_sort(sorted_data, "Already Sorted")
    test_sort(reverse_data, "Reverse Sorted")
    test_sort(nearly_data, "Nearly Sorted")
    test_sort(random_data, "Random Order")

def add_request():
    customer = input("Enter customer name: ")

    priority = get_number("Enter priority (1-5): ")
    if priority < 1 or priority > 5:
        print("Priority must be from 1 to 5")
        return

    time = get_number("Enter estimated time: ")
    if time <= 0:
        print("Estimated time must be positive")
        return

    request = {
        "id": generate_id(data),
        "customer": customer,
        "priority": priority,
        "time": time,
        "status": "Pending"
    }

    data.append(request)
    waiting_queue.enqueue(request)
    save_data(data)

    print("Request added successfully")
    print("Request ID:", request["id"])


def process_request():
    request = waiting_queue.dequeue()

    if request is None:
        print("Queue is empty")
        return

    request["status"] = "Processed"
    processed_requests.append(request)
    hash_table.put(request["id"], request)

    save_data(data)

    print("Request processed")
    print(request)

data = load_data()

waiting_queue = Queue()
processed_requests = []
search_history = Stack()
hash_table = HashTable()
sorting_history = []

for request in data:
    valid, message = validate_request(request)

    if not valid:
        continue

    if request["status"] == "Pending":
        waiting_queue.enqueue(request)
    else:
        processed_requests.append(request)
        hash_table.put(request["id"], request)

while True:
    print()
    print("===== Smart Service Center =====")
    print("1. Add Incoming Request")
    print("2. Process Next Request")
    print("3. Show Waiting Queue")
    print("4. Show Processed Requests")
    print("5. Sort Requests")
    print("6. Sequential Search")
    print("7. Binary Search")
    print("8. Hash Lookup")
    print("9. View Last Search")
    print("10. Remove Last Search")
    print("11. Show Algorithm Statistics")
    print("12. Test Sorting Datasets")
    print("13. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_request()

    elif choice == "2":
        process_request()

    elif choice == "3":
        waiting_queue.show()

    elif choice == "4":
        show_requests(processed_requests)

    elif choice == "5":
        sort_requests(processed_requests)

    elif choice == "6":
        target = get_number("Enter Request ID: ")

        index, comparisons = sequential_search(
            processed_requests, target
        )

        if index == -1:
            print("Not Found")
        else:
            print("Found")
            print(processed_requests[index])

        print("Comparisons:", comparisons)

    elif choice == "7":
        if len(processed_requests) == 0:
            print("No processed requests")
            continue

        target = get_number("Enter Request ID: ")

        sorted_data, c, s = insertion_sort(
            processed_requests, "id"
        )

        index, comparisons = binary_search(
            sorted_data, target
        )

        if index < len(sorted_data) and sorted_data[index]["id"] == target:
            print("Found")
            print(sorted_data[index])
        else:
            print("Not Found")
            print("Insert Position:", index)

        print("Comparisons:", comparisons)

    elif choice == "8":
        target = get_number("Enter Request ID: ")
        result = hash_table.get(target)

        if result is None:
            search_history.push({
                "id": target,
                "method": "Hash Lookup",
                "result": "Not Found",
                "comparisons": 1
            })
            print("Not Found")
        else:
            search_history.push({
                "id": target,
                "method": "Hash Lookup",
                "result": "Found",
                "comparisons": 1
            })
            print("Found")
            print(result)

    elif choice == "9":
        result = search_history.peek()

        if result is None:
            print("Search History is empty")
        else:
            print(result)

    elif choice == "10":
        result = search_history.pop()

        if result is None:
            print("Search History is empty")
        else:
            print("Removed:", result)

    elif choice == "11":
        print()
        print("Search Statistics")
        show_search_statistics()

        print()
        print("Sorting Statistics")
        show_sort_statistics()

    elif choice == "12":
        test_datasets(processed_requests)

    elif choice == "13":
        save_data(data)
        print("Goodbye")
        break

    else:
        print("Invalid choice")
