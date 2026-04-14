import os
import django
import random

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wpl_project_db.settings')
django.setup()

from interview_prep.models import Topic, Question

def populate():
    data = {
        "Arrays": [
            # Easy
            {"text": "What is the index of the first element in an array?", "diff": "Easy", "opts": ["0", "1", "-1", "Depends on language"], "ans": "A"},
            {"text": "Which operation in an array has O(1) time complexity?", "diff": "Easy", "opts": ["Searching", "Accessing by index", "Deletion", "Insertion"], "ans": "B"},
            {"text": "What is the maximum number of elements a fixed-size array of size 10 can hold?", "diff": "Easy", "opts": ["9", "10", "11", "Infinite"], "ans": "B"},
            {"text": "Which of these is used to declare an array in C++?", "diff": "Easy", "opts": ["int a[];", "int a();", "int a{};", "array a;"], "ans": "A"},
            {"text": "Arrays are _____ data structures.", "diff": "Easy", "opts": ["Linear", "Non-linear", "Hierarchical", "None"], "ans": "A"},
            {"text": "Which property gives the number of elements in a Java array?", "diff": "Easy", "opts": ["size()", "count", "length", "index"], "ans": "C"},
            {"text": "How do you find the length of an array in Python?", "diff": "Easy", "opts": ["length(arr)", "arr.length", "len(arr)", "size(arr)"], "ans": "C"},
            {"text": "What is a 1D array?", "diff": "Easy", "opts": ["A matrix", "A list of elements", "A single value", "A pointer"], "ans": "B"},
            {"text": "In C, what is the default value of local array elements?", "diff": "Easy", "opts": ["0", "NULL", "Garbage value", "1"], "ans": "C"},
            {"text": "Can an array store different data types in C++?", "diff": "Easy", "opts": ["Yes", "No", "Only if it's a float", "Depends on compiler"], "ans": "B"},
            
            # Medium
            {"text": "What is the time complexity of a linear search in an array of size n?", "diff": "Medium", "opts": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "ans": "C"},
            {"text": "In a 2D array declared as A[3][4], how many total elements are there?", "diff": "Medium", "opts": ["7", "12", "10", "16"], "ans": "B"},
            {"text": "What happens if you try to access an index outside the array bounds in Java?", "diff": "Medium", "opts": ["Returns null", "Returns 0", "Throws Exception", "Crashes OS"], "ans": "C"},
            {"text": "Which sorting algorithm has a best-case complexity of O(n) for a nearly sorted array?", "diff": "Medium", "opts": ["Quick Sort", "Selection Sort", "Insertion Sort", "Merge Sort"], "ans": "C"},
            {"text": "What is a 'sparse array'?", "diff": "Medium", "opts": ["An array with many zeros", "An array with no elements", "An array with prime numbers", "A small array"], "ans": "A"},
            {"text": "What is the time complexity of binary search on a sorted array?", "diff": "Medium", "opts": ["O(n)", "O(log n)", "O(1)", "O(n log n)"], "ans": "B"},
            {"text": "What is the space complexity of an array of size N?", "diff": "Medium", "opts": ["O(1)", "O(N)", "O(log N)", "O(N^2)"], "ans": "B"},
            {"text": "Which of the following is an advantage of arrays?", "diff": "Medium", "opts": ["Dynamic size", "Ease of insertion", "Fast random access", "No wasted memory"], "ans": "C"},
            {"text": "In a row-major 2D array, how are elements stored?", "diff": "Medium", "opts": ["Column by column", "Row by row", "Diagonally", "Randomly"], "ans": "B"},
            
            # Hard
            {"text": "What is the time complexity to find the 'Missing Number' in an unsorted array of 1 to N using the sum formula?", "diff": "Hard", "opts": ["O(n log n)", "O(n)", "O(1)", "O(n^2)"], "ans": "B"},
            {"text": "Which algorithm is most efficient for finding the 'Majority Element' in an array?", "diff": "Hard", "opts": ["Binary Search", "Boyer-Moore Voting", "Sieve of Eratosthenes", "Kadane's Algorithm"], "ans": "B"},
            {"text": "Kadane's Algorithm is used for which problem?", "diff": "Hard", "opts": ["Sorting", "Max Subarray Sum", "Matrix Multiplication", "String Matching"], "ans": "B"},
            {"text": "How do you find the duplicate in an array of N+1 integers where elements are 1 to N using O(1) extra space?", "diff": "Hard", "opts": ["Hashing", "Sorting", "Floyd's Cycle Finding", "Linear Search"], "ans": "C"},
            {"text": "What is the time complexity of the Dutch National Flag algorithm?", "diff": "Hard", "opts": ["O(n)", "O(n log n)", "O(n^2)", "O(1)"], "ans": "A"},
            {"text": "Which of these can find the K-th smallest element in O(n) average time?", "diff": "Hard", "opts": ["Merge Sort", "Quick Select", "Heap Sort", "Bubble Sort"], "ans": "B"},
            {"text": "What is the amortized time complexity of appending to a dynamic array?", "diff": "Hard", "opts": ["O(n)", "O(log n)", "O(1)", "O(n^2)"], "ans": "C"},
        ],
        "SQL": [
            # Easy
            {"text": "Which command is used to fetch data from a table?", "diff": "Easy", "opts": ["GET", "FETCH", "SELECT", "READ"], "ans": "C"},
            {"text": "What does SQL stand for?", "diff": "Easy", "opts": ["Structured Query Language", "Simple Query Logic", "Schema Query List", "Sequential Query Link"], "ans": "A"},
            {"text": "Which clause is used to filter records?", "diff": "Easy", "opts": ["GROUP BY", "WHERE", "ORDER BY", "HAVING"], "ans": "B"},
            {"text": "How do you return all columns from a table named 'Users'?", "diff": "Easy", "opts": ["SELECT ALL Users", "SELECT * FROM Users", "GET * FROM Users", "EXTRACT Users"], "ans": "B"},
            {"text": "Which SQL keyword is used to sort the result-set?", "diff": "Easy", "opts": ["SORT", "ARRANGE", "ORDER BY", "SET"], "ans": "C"},
            {"text": "Which command is used to insert new data into a table?", "diff": "Easy", "opts": ["ADD RECORD", "INSERT INTO", "PUT", "UPDATE"], "ans": "B"},
            {"text": "Which statement is used to delete data from a database?", "diff": "Easy", "opts": ["COLLAPSE", "REMOVE", "DELETE", "DROP"], "ans": "C"},
            {"text": "Which keyword is used to return only different values?", "diff": "Easy", "opts": ["UNIQUE", "DISTINCT", "DIFFERENT", "SELECT"], "ans": "B"},
            {"text": "Which SQL command is used to update data in a table?", "diff": "Easy", "opts": ["SAVE", "MODIFY", "UPDATE", "CHANGE"], "ans": "C"},
            
            # Medium
            {"text": "Which join returns all records when there is a match in either left or right table?", "diff": "Medium", "opts": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"], "ans": "D"},
            {"text": "Which aggregate function returns the number of rows?", "diff": "Medium", "opts": ["SUM()", "TOTAL()", "COUNT()", "ROWS()"], "ans": "C"},
            {"text": "What is the difference between DELETE and TRUNCATE?", "diff": "Medium", "opts": ["No difference", "TRUNCATE can be rolled back", "DELETE is DDL", "TRUNCATE is faster and DDL"], "ans": "D"},
            {"text": "Which constraint uniquely identifies each record in a table?", "diff": "Medium", "opts": ["UNIQUE", "FOREIGN KEY", "PRIMARY KEY", "CHECK"], "ans": "C"},
            {"text": "The HAVING clause is used in combination with ______.", "diff": "Medium", "opts": ["ORDER BY", "GROUP BY", "WHERE", "JOIN"], "ans": "B"},
            {"text": "What is the default sort order for ORDER BY?", "diff": "Medium", "opts": ["DESC", "ASC", "Random", "Numerical"], "ans": "B"},
            {"text": "Which operator is used to search for a specified pattern in a column?", "diff": "Medium", "opts": ["GET", "MATCH", "LIKE", "FIND"], "ans": "C"},
            {"text": "What does the UNION operator do?", "diff": "Medium", "opts": ["Joins two tables", "Combines result-sets of two SELECTs", "Updates two tables", "Deletes duplicates in one table"], "ans": "B"},
            
            # Hard
            {"text": "What is the purpose of a 'Normalization' in databases?", "diff": "Hard", "opts": ["Increase redundancy", "Reduce redundancy", "Speed up SELECTs only", "Encrypt data"], "ans": "B"},
            {"text": "Which normal form deals with Transitive Dependency?", "diff": "Hard", "opts": ["1NF", "2NF", "3NF", "BCNF"], "ans": "C"},
            {"text": "What is an 'Index' in SQL used for?", "diff": "Hard", "opts": ["Backup data", "Speed up data retrieval", "Encrypt primary keys", "Group records"], "ans": "B"},
            {"text": "What is the 'ACID' property 'I' stand for?", "diff": "Hard", "opts": ["Information", "Integration", "Isolation", "Indexing"], "ans": "C"},
            {"text": "Which normal form requires that there are no partial functional dependencies?", "diff": "Hard", "opts": ["1NF", "2NF", "3NF", "4NF"], "ans": "B"},
            {"text": "What is a 'Composite Key'?", "diff": "Hard", "opts": ["A key with multiple columns", "A key that links to another table", "A hidden key", "A string-based key"], "ans": "A"},
            {"text": "What is the difference between WHERE and HAVING?", "diff": "Hard", "opts": ["No difference", "WHERE is for groups, HAVING for rows", "WHERE is for rows, HAVING for groups", "WHERE is faster"], "ans": "C"},
        ],
        "Linked Lists and Pointers": [
            # Easy
            {"text": "A linked list is a _____ data structure.", "diff": "Easy", "opts": ["Sequential", "Random Access", "Non-linear", "Constant"], "ans": "A"},
            {"text": "What does each node in a singly linked list contain?", "diff": "Easy", "opts": ["Data only", "Address only", "Data and Pointer", "Two pointers"], "ans": "C"},
            {"text": "What is a pointer?", "diff": "Easy", "opts": ["A variable that stores data", "A variable that stores address", "A function", "A loop"], "ans": "B"},
            {"text": "What is the value of the 'next' pointer in the last node of a linked list?", "diff": "Easy", "opts": ["0", "Head", "NULL", "Random"], "ans": "C"},
            {"text": "Which operator is used to access members of a struct through a pointer in C?", "diff": "Easy", "opts": [".", "->", "&", "*"], "ans": "B"},
            {"text": "In C++, how do you get the address of a variable 'x'?", "diff": "Easy", "opts": ["*x", "addr(x)", "&x", "$x"], "ans": "C"},
            {"text": "Which memory area is used for dynamic memory allocation?", "diff": "Easy", "opts": ["Stack", "Heap", "Register", "Static"], "ans": "B"},
            {"text": "What happens if a pointer is not initialized?", "diff": "Easy", "opts": ["Points to NULL", "Points to 0", "Points to random memory", "Compiler error"], "ans": "C"},
            
            # Medium
            {"text": "What is the time complexity to insert a node at the beginning of a singly linked list?", "diff": "Medium", "opts": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "ans": "A"},
            {"text": "A doubly linked list node contains how many pointers?", "diff": "Medium", "opts": ["1", "2", "3", "0"], "ans": "B"},
            {"text": "What is 'Memory Leak' in C++?", "diff": "Medium", "opts": ["Running out of RAM", "Not deleting dynamic memory", "Computer crash", "Virtual memory overflow"], "ans": "B"},
            {"text": "Which data structure uses the 'Circular' concept where the last node points to the first?", "diff": "Medium", "opts": ["Stack", "Circular Queue", "Circular Linked List", "Tree"], "ans": "C"},
            {"text": "What is a 'Dangling Pointer'?", "diff": "Medium", "opts": ["A NULL pointer", "Pointer to deleted memory", "Uninitialized pointer", "Pointer to an array"], "ans": "B"},
            {"text": "What is the time complexity to access the n-th element in a linked list?", "diff": "Medium", "opts": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "ans": "B"},
            {"text": "Which of these is NOT an advantage of Linked Lists over Arrays?", "diff": "Medium", "opts": ["Dynamic size", "Ease of insertion", "Random access", "No memory wastage"], "ans": "C"},
            
            # Hard
            {"text": "How do you detect a cycle in a linked list?", "diff": "Hard", "opts": ["Binary Search", "Hash Map", "Floyd's Tortoise and Hare", "Recursion"], "ans": "C"},
            {"text": "What is the time complexity to reverse a singly linked list?", "diff": "Hard", "opts": ["O(n^2)", "O(log n)", "O(n)", "O(1)"], "ans": "C"},
            {"text": "Which pointer points to the entire array and not just the first element?", "diff": "Hard", "opts": ["Wild pointer", "Array pointer", "Base pointer", "Null pointer"], "ans": "B"},
            {"text": "How can you find the middle element of a linked list in one pass?", "diff": "Hard", "opts": ["Calculate length then traverse", "Two pointers (fast and slow)", "Random search", "Using a stack"], "ans": "B"},
            {"text": "In a skip list, what is the average search time complexity?", "diff": "Hard", "opts": ["O(n)", "O(log n)", "O(1)", "O(n log n)"], "ans": "B"},
            {"text": "What is a XOR Linked List?", "diff": "Hard", "opts": ["A list with no data", "A list using XOR to save pointer space", "A list with multiple heads", "A tree-like list"], "ans": "B"},
        ],
        "Graphs and Trees": [
             # Easy
            {"text": "A tree with no nodes is called a ______.", "diff": "Easy", "opts": ["Empty tree", "Null tree", "Rootless tree", "Binary tree"], "ans": "B"},
            {"text": "How many children can a node in a Binary Tree have?", "diff": "Easy", "opts": ["Exactly 2", "At most 2", "At least 2", "Infinite"], "ans": "B"},
            {"text": "Which traversal visits the root first, then left, then right?", "diff": "Easy", "opts": ["Inorder", "Preorder", "Postorder", "Level-order"], "ans": "B"},
            {"text": "What is the top-most node of a tree called?", "diff": "Easy", "opts": ["Leaf", "Stem", "Root", "Parent"], "ans": "C"},
            {"text": "A graph with no cycles is called a ______.", "diff": "Easy", "opts": ["Acyclic graph", "Cyclic graph", "Complete graph", "Connected graph"], "ans": "A"},
            {"text": "Nodes with no children are called ______.", "diff": "Easy", "opts": ["Root", "Internal nodes", "Leaves", "Sibs"], "ans": "C"},
            {"text": "In a tree, what is a node with at least one child called?", "diff": "Easy", "opts": ["Leaf", "Internal Node", "Root only", "Edge"], "ans": "B"},
            
            # Medium
            {"text": "Which algorithm is used for finding the shortest path in a weighted graph?", "diff": "Medium", "opts": ["BFS", "DFS", "Dijkstra's", "Kruskal's"], "ans": "C"},
            {"text": "What is the height of a balanced binary tree with N nodes?", "diff": "Medium", "opts": ["O(N)", "O(log N)", "O(N^2)", "O(1)"], "ans": "B"},
            {"text": "A Full Binary Tree is one where every node has either _____ children.", "diff": "Medium", "opts": ["0 or 1", "1 or 2", "0 or 2", "Exactly 2"], "ans": "C"},
            {"text": "In a graph, BFS uses which data structure?", "diff": "Medium", "opts": ["Stack", "Queue", "Priority Queue", "Linked List"], "ans": "B"},
            {"text": "In a Binary Search Tree (BST), the left child is always _____ than the parent.", "diff": "Medium", "opts": ["Greater", "Smaller", "Equal", "None"], "ans": "B"},
            {"text": "Which traversal of a BST gives elements in sorted order?", "diff": "Medium", "opts": ["Preorder", "Postorder", "Inorder", "Level-order"], "ans": "C"},
            {"text": "In DFS, which data structure is used?", "diff": "Medium", "opts": ["Queue", "Stack", "Heap", "Array"], "ans": "B"},
            
            # Hard
            {"text": "Which algorithm is used to find the Minimum Spanning Tree?", "diff": "Hard", "opts": ["Bellman-Ford", "Prim's", "Floyd-Warshall", "PageRank"], "ans": "B"},
            {"text": "What is the time complexity of searching in a Red-Black Tree?", "diff": "Hard", "opts": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "ans": "B"},
            {"text": "A 'Self-Balancing' BST is which of these?", "diff": "Hard", "opts": ["AVL Tree", "Binary Heap", "B-Tree", "Trie"], "ans": "A"},
            {"text": "What is the maximum number of edges in a directed graph with N vertices?", "diff": "Hard", "opts": ["N", "N-1", "N(N-1)", "N^2"], "ans": "C"},
            {"text": "What is the time complexity of the Bellman-Ford algorithm?", "diff": "Hard", "opts": ["O(V+E)", "O(E log V)", "O(VE)", "O(V^2)"], "ans": "C"},
            {"text": "A 'B-Tree' is typically used in which application?", "diff": "Hard", "opts": ["Compilers", "Databases", "Networking", "AI"], "ans": "B"},
        ],
        "Time Complexities and Algorithms": [
            # Easy
            {"text": "What is the best case time complexity of Binary Search?", "diff": "Easy", "opts": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "ans": "A"},
            {"text": "Which algorithm uses the 'Divide and Conquer' strategy?", "diff": "Easy", "opts": ["Bubble Sort", "Merge Sort", "Linear Search", "Insertion Sort"], "ans": "B"},
            {"text": "O(1) is also known as _____ time.", "diff": "Easy", "opts": ["Linear", "Logarithmic", "Constant", "Quadratic"], "ans": "C"},
            {"text": "Which sort is generally the slowest for large datasets?", "diff": "Easy", "opts": ["Quick Sort", "Merge Sort", "Bubble Sort", "Heap Sort"], "ans": "C"},
            {"text": "What is the time complexity of adding an element to a stack?", "diff": "Easy", "opts": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "ans": "A"},
            {"text": "Recursion uses which internal data structure?", "diff": "Easy", "opts": ["Queue", "Stack", "Tree", "Graph"], "ans": "B"},
            {"text": "What is the time complexity of Bubble Sort in the worst case?", "diff": "Easy", "opts": ["O(n)", "O(n log n)", "O(n^2)", "O(1)"], "ans": "C"},
            
            # Medium
            {"text": "What is the average time complexity of Quick Sort?", "diff": "Medium", "opts": ["O(n log n)", "O(n^2)", "O(n)", "O(log n)"], "ans": "A"},
            {"text": "The 'Big O' notation describes the _____ bound of an algorithm.", "diff": "Medium", "opts": ["Lower", "Upper", "Average", "Tight"], "ans": "B"},
            {"text": "Which algorithm is used to find the GCD of two numbers?", "diff": "Medium", "opts": ["Sieve", "Euclidean Algorithm", "Binary Search", "Dijkstra"], "ans": "B"},
            {"text": "What is the time complexity of the Sieve of Eratosthenes?", "diff": "Medium", "opts": ["O(n)", "O(n log n)", "O(n log log n)", "O(n^2)"], "ans": "C"},
            {"text": "Space complexity of an algorithm refers to _____.", "diff": "Medium", "opts": ["Time taken", "Memory used", "Lines of code", "Number of variables"], "ans": "B"},
            {"text": "What is the time complexity of selection sort?", "diff": "Medium", "opts": ["O(n log n)", "O(n)", "O(n^2)", "O(1)"], "ans": "C"},
            {"text": "Merge sort uses which design paradigm?", "diff": "Medium", "opts": ["Greedy", "Dynamic Programming", "Divide and Conquer", "Backtracking"], "ans": "C"},
            
            # Hard
            {"text": "Dynamic Programming is based on which concept?", "diff": "Hard", "opts": ["Recursion", "Overlapping Subproblems", "Greedy choice", "Randomization"], "ans": "B"},
            {"text": "What is the worst case time complexity of Quick Sort?", "diff": "Hard", "opts": ["O(n log n)", "O(n^2)", "O(n^3)", "O(2^n)"], "ans": "B"},
            {"text": "Which problem cannot be solved using a Greedy approach?", "diff": "Hard", "opts": ["Huffman Coding", "Prim's Algorithm", "0/1 Knapsack", "Activity Selection"], "ans": "C"},
            {"text": "What is the time complexity of Matrix Multiplication (Naive)?", "diff": "Hard", "opts": ["O(n^2)", "O(n^3)", "O(n log n)", "O(2^n)"], "ans": "B"},
            {"text": "What is the time complexity of the KMP string matching algorithm?", "diff": "Hard", "opts": ["O(n*m)", "O(n+m)", "O(n log n)", "O(n^2)"], "ans": "B"},
            {"text": "The Floyd-Warshall algorithm is used for ______.", "diff": "Hard", "opts": ["MST", "All-pairs shortest paths", "Topological sort", "Network flow"], "ans": "B"},
        ],
        "Aptitude + Logic and Reasoning": [
            # Easy
            {"text": "If 5 workers can build a wall in 5 days, how long will it take 10 workers?", "diff": "Easy", "opts": ["10 days", "5 days", "2.5 days", "1 day"], "ans": "C"},
            {"text": "Look at this series: 2, 4, 8, 16, ... What number comes next?", "diff": "Easy", "opts": ["20", "24", "32", "64"], "ans": "C"},
            {"text": "Which word does NOT belong with the others?", "diff": "Easy", "opts": ["Leopard", "Cougar", "Tiger", "Elephant"], "ans": "D"},
            {"text": "If all roses are flowers and some flowers fade, can we say all roses fade?", "diff": "Easy", "opts": ["Yes", "No", "Maybe", "Depends on weather"], "ans": "B"},
            {"text": "A father is 30 years older than his son. In 5 years, he will be 3 times as old. Son's age?", "diff": "Easy", "opts": ["5", "10", "15", "20"], "ans": "B"},
            {"text": "What is 15% of 200?", "diff": "Easy", "opts": ["20", "30", "40", "15"], "ans": "B"},
            {"text": "A clock shows 4:30. If the minute hand points East, where does the hour hand point?", "diff": "Easy", "opts": ["North", "South", "North-East", "South-East"], "ans": "C"},
            
            # Medium
            {"text": "A train 100m long passes a pole in 10s. What is its speed in km/h?", "diff": "Medium", "opts": ["36", "40", "45", "50"], "ans": "A"},
            {"text": "In a row of 20 people, if A is 5th from left, what is his position from right?", "diff": "Medium", "opts": ["15th", "16th", "14th", "17th"], "ans": "B"},
            {"text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the man related to the woman?", "diff": "Medium", "opts": ["Brother", "Father", "Son", "Husband"], "ans": "C"},
            {"text": "What is the angle between the hour and minute hand at 3:00?", "diff": "Medium", "opts": ["45°", "90°", "60°", "120°"], "ans": "B"},
            {"text": "If NOON is coded as 14151514, what is MOON?", "diff": "Medium", "opts": ["13151514", "13141413", "14151513", "12151514"], "ans": "A"},
            {"text": "A sum of money doubles itself in 10 years at simple interest. What is the rate?", "diff": "Medium", "opts": ["5%", "10%", "15%", "20%"], "ans": "B"},
            
            # Hard
            {"text": "In how many ways can the letters of 'APPLE' be rearranged?", "diff": "Hard", "opts": ["120", "60", "24", "100"], "ans": "B"},
            {"text": "A bag has 3 red and 2 blue balls. If 2 balls are drawn, probability both are red?", "diff": "Hard", "opts": ["3/10", "1/5", "2/5", "1/2"], "ans": "A"},
            {"text": "Six people sit in a circle. In how many ways can they be seated?", "diff": "Hard", "opts": ["720", "120", "60", "240"], "ans": "B"},
            {"text": "If 3rd Jan of a year is Sunday, what will be 15th Feb (Non-leap year)?", "diff": "Hard", "opts": ["Monday", "Tuesday", "Sunday", "Saturday"], "ans": "A"},
            {"text": "The ratio of ages of A and B is 4:5. After 5 years, it will be 5:6. Sum of their current ages?", "diff": "Hard", "opts": ["45", "40", "50", "35"], "ans": "A"},
            {"text": "In a group of 100 people, 60 like tea, 40 like coffee, and 20 like both. How many like neither?", "diff": "Hard", "opts": ["20", "10", "30", "0"], "ans": "A"},
        ]
    }

    for topic_name, questions in data.items():
        topic, _ = Topic.objects.get_or_create(name=topic_name)
        
        count = 0
        for q in questions:
            # Check if question with same text already exists for this topic
            if not Question.objects.filter(topic=topic, text=q["text"]).exists():
                Question.objects.create(
                    topic=topic,
                    text=q["text"],
                    difficulty=q["diff"],
                    option_a=q["opts"][0],
                    option_b=q["opts"][1],
                    option_c=q["opts"][2],
                    option_d=q["opts"][3],
                    correct_option=q["ans"]
                )
                count += 1
        print(f"Added {count} new questions to {topic_name}")

if __name__ == "__main__":
    populate()
