import json

def load_data():
    with open("service_data.json", "r") as file:
        data = json.load(file)
    return data

def generate_id(data):
    if len(data) == 0:
        return 1

    max_id = data[0]["id"]

    for item in data:
        if item["id"] > max_id:
            max_id = item["id"]

    return max_id + 1

def validate_request(request):
    if "customer" not in request or request["customer"].strip() == "":
        return False, "Customer name cannot be empty"

    if "priority" not in request:
        return False, "Priority is missing"

    if request["priority"] < 1 or request["priority"] > 5:
        return False, "Priority must be from 1 to 5"

    if "time" not in request:
        return False, "Estimated time is missing"

    if request["time"] <= 0:
        return False, "Estimated time must be positive"

    if "status" not in request:
        return False, "Status is missing"

    status = request["status"].strip().lower()

    if status not in ["pending", "processed", "closed", "rejected"]:
        return False, "Invalid status"

    request["status"] = status.capitalize()
    request["customer"] = request["customer"].strip()

    return True, "Valid request"

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.items[0]
        self.items = self.items[1:]
        return item

    def front(self):
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

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

def sequential_search(data, target_id):
    comparisons = 0

    for i in range(len(data)):
        comparisons += 1

        if data[i]["id"] == target_id:
            history = {
                "target_id": target_id,
                "method": "Sequential Search",
                "result": "Found",
                "comparisons": comparisons
            }

            search_history.push(history)
            return i, comparisons

    history = {
        "target_id": target_id,
        "method": "Sequential Search",
        "result": "Not Found",
        "comparisons": comparisons
    }

    search_history.push(history)
    return -1, comparisons

def bubble_sort(data, field):
    arr = data.copy()
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            comparisons += 1

            if arr[j][field] > arr[j + 1][field]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps, field

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

    return arr, comparisons, swaps, field

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

    return arr, comparisons, shifts, field

def binary_search(data, target_id):
    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if data[mid]["id"] == target_id:
            history = {
                "target_id": target_id,
                "method": "Binary Search",
                "result": "Found",
                "comparisons": comparisons
            }

            search_history.push(history)
            return mid, comparisons

        if data[mid]["id"] < target_id:
            left = mid + 1
        else:
            right = mid - 1

    history = {
        "target_id": target_id,
        "method": "Binary Search",
        "result": "Not Found",
        "comparisons": comparisons
    }

    search_history.push(history)
    return left, comparisons

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for i in range(size)]

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

def hash_lookup(hash_table, target_id):
    result = hash_table.get(target_id)

    if result is not None:
        history = {
            "target_id": target_id,
            "method": "Hash Lookup",
            "result": "Found",
            "comparisons": 1
        }

        search_history.push(history)
        return result

    history = {
        "target_id": target_id,
        "method": "Hash Lookup",
        "result": "Not Found",
        "comparisons": 1
    }

    search_history.push(history)
    return None

def show_search_statistics():
    print()
    print("Search Statistics")

    for item in search_history.items:
        print(
            item["method"],
            "| ID:", item["target_id"],
            "| Result:", item["result"],
            "| Comparisons:", item["comparisons"]
        )

# Load data
data = load_data()

# Create system objects
waiting_queue = Queue()
processed_requests = []
search_history = Stack()
hash_table = HashTable()

# Separate waiting and processed requests
for request in data:
    if request["status"] == "Pending":
        waiting_queue.enqueue(request)
    else:
        processed_requests.append(request)
        hash_table.put(request["id"], request)

# Main menu
# Main menu
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
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        customer = input("Enter customer name: ")
        priority = int(input("Enter priority (1-5): "))
        time = int(input("Enter estimated time: "))

        new_request = {
            "id": generate_id(data),
            "customer": customer,
            "priority": priority,
            "time": time,
            "status": "Pending"
        }

        valid, message = validate_request(new_request)

        if valid:
            data.append(new_request)
            waiting_queue.enqueue(new_request)
            print("Request added successfully")
            print(new_request)
        else:
            print(message)
    elif choice == "2":
        request = waiting_queue.dequeue()

        if request is None:
            print("Queue is empty")
        else:
            request["status"] = "Processed"
            processed_requests.append(request)
            hash_table.put(request["id"], request)
            print("Request processed:", request)

    elif choice == "3":
        if waiting_queue.is_empty():
            print("Queue is empty")
        else:
            for request in waiting_queue.items:
                print(request)

    elif choice == "4":
        for request in processed_requests:
            print(request)

    elif choice == "5":
        sorted_data, comparisons, swaps, field = bubble_sort(
            processed_requests, "id"
        )

        for request in sorted_data:
            print(request)

        print("Comparisons:", comparisons)
        print("Swaps:", swaps)

    elif choice == "6":
        target_id = int(input("Enter Request ID: "))

        index, comparisons = sequential_search(
            processed_requests, target_id
        )

        if index == -1:
            print("Not Found")
        else:
            print("Found")
            print("Index:", index)

        print("Comparisons:", comparisons)

    elif choice == "7":
        target_id = int(input("Enter Request ID: "))

        sorted_data, comparisons, swaps, field = bubble_sort(
            processed_requests, "id"
        )

        index, comparisons = binary_search(
            sorted_data, target_id
        )

        if index < len(sorted_data) and sorted_data[index]["id"] == target_id:
            print("Found")
            print("Index:", index)
        else:
            print("Not Found")
            print("Insert Position:", index)

        print("Comparisons:", comparisons)

    elif choice == "8":
        target_id = int(input("Enter Request ID: "))

        result = hash_lookup(hash_table, target_id)

        if result is None:
            print("Not Found")
        else:
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
        show_search_statistics()

    elif choice == "12":
        print("Goodbye")
        break

    else:
        print("Invalid choice")