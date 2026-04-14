import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wpl_project_db.settings')
django.setup()

from interview_prep.models import Topic, Question

def add_questions(topic_name, questions):
    topic, _ = Topic.objects.get_or_create(name=topic_name)
    count = 0
    for q in questions:
        if not Question.objects.filter(topic=topic, text=q[0]).exists():
            Question.objects.create(
                topic=topic, text=q[0], difficulty=q[1],
                option_a=q[2][0], option_b=q[2][1], option_c=q[2][2], option_d=q[2][3],
                correct_option=q[3]
            )
            count += 1
    print(f"Added {count} new questions to {topic_name}")

def populate():
    # Format: [Text, Difficulty, [OptA, OptB, OptC, OptD], CorrectAns]
    data = {
        "Arrays": [
            # Easy (15 total)
            ["What is the index of the first element?", "Easy", ["0", "1", "-1", "n"], "A"],
            ["Which operation is O(1)?", "Easy", ["Search", "Access", "Delete", "Insert"], "B"],
            ["Max elements in array of size 10?", "Easy", ["9", "10", "11", "0"], "B"],
            ["Declare array in C++?", "Easy", ["int a[];", "int a();", "int a{};", "a[]"], "A"],
            ["Arrays are _____ structures.", "Easy", ["Linear", "Non-linear", "Tree", "Graph"], "A"],
            ["Java array length property?", "Easy", ["size()", "count", "length", "len"], "C"],
            ["Python array length?", "Easy", ["len()", "size()", "count()", "length"], "A"],
            ["What is a 1D array?", "Easy", ["Matrix", "List", "Point", "Scalar"], "B"],
            ["C local array default value?", "Easy", ["0", "NULL", "Garbage", "1"], "C"],
            ["Can C++ arrays store mixed types?", "Easy", ["Yes", "No", "Maybe", "Depends"], "B"],
            ["Minimum array elements?", "Easy", ["0", "1", "-1", "Any"], "A"],
            ["Arrays in C use _____ memory.", "Easy", ["Contiguous", "Random", "Virtual", "Heap"], "A"],
            ["Array indexing usually starts at?", "Easy", ["0", "1", "-1", "Random"], "A"],
            ["Is an array a primitive type in Java?", "Easy", ["Yes", "No", "Sometimes", "Only int"], "B"],
            ["What is the last index of array size N?", "Easy", ["N", "N+1", "N-1", "0"], "C"],
            
            # Medium (15 total)
            ["Linear search complexity?", "Medium", ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "C"],
            ["Elements in A[3][4]?", "Medium", ["7", "12", "10", "16"], "B"],
            ["Java out of bounds result?", "Medium", ["Null", "0", "Exception", "Crash"], "C"],
            ["Sort with O(n) best case?", "Medium", ["Quick", "Selection", "Insertion", "Merge"], "C"],
            ["What is a sparse array?", "Medium", ["Many zeros", "Empty", "Prime only", "Small"], "A"],
            ["Binary search complexity?", "Medium", ["O(n)", "O(log n)", "O(1)", "O(n!)"], "B"],
            ["Space complexity of size N array?", "Medium", ["O(1)", "O(N)", "O(N^2)", "O(log N)"], "B"],
            ["Array advantage?", "Medium", ["Dynamic size", "Easy insert", "Fast access", "No waste"], "C"],
            ["Row-major storage?", "Medium", ["Col by Col", "Row by Row", "Diagonal", "None"], "B"],
            ["Dynamic array append (average)?", "Medium", ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "A"],
            ["C resize function?", "Medium", ["malloc", "calloc", "realloc", "free"], "C"],
            ["Array to represent Heap?", "Medium", ["Yes", "No", "Only Max Heap", "Only Min Heap"], "A"],
            ["Base address is address of?", "Medium", ["Last element", "Middle", "First element", "Size"], "C"],
            ["Searching in unsorted array?", "Medium", ["Binary", "Linear", "Interpolation", "None"], "B"],
            ["2D array is also called?", "Medium", ["Vector", "Matrix", "List", "Queue"], "B"],

            # Hard (10 total)
            ["Find missing number in 1..N?", "Hard", ["O(n log n)", "O(n)", "O(1)", "O(n^2)"], "B"],
            ["Majority element algorithm?", "Hard", ["Binary", "Boyer-Moore", "Sieve", "Kadane"], "B"],
            ["Kadane's used for?", "Hard", ["Sort", "Max Subarray", "Matrix", "Match"], "B"],
            ["Duplicate in 1..N with O(1) space?", "Hard", ["Hash", "Sort", "Floyd's Cycle", "Linear"], "C"],
            ["Dutch National Flag complexity?", "Hard", ["O(n)", "O(n log n)", "O(n^2)", "O(1)"], "A"],
            ["K-th smallest in O(n) avg?", "Hard", ["Merge", "Quick Select", "Heap", "Bubble"], "B"],
            ["Dynamic array amortized append?", "Hard", ["O(n)", "O(log n)", "O(1)", "O(n^2)"], "C"],
            ["Sliding window max complexity?", "Hard", ["O(NK)", "O(N log N)", "O(N)", "O(N log K)"], "C"],
            ["Range Sum Query with updates?", "Hard", ["Hash", "Fenwick Tree", "Stack", "Queue"], "B"],
            ["Rain water trapping complexity?", "Hard", ["O(N^2)", "O(N log N)", "O(N)", "O(1)"], "C"]
        ],
        "SQL": [
            # Easy (15 total)
            ["Command to fetch data?", "Easy", ["GET", "FETCH", "SELECT", "READ"], "C"],
            ["SQL stands for?", "Easy", ["Structured", "Simple", "Schema", "Sequential"], "A"],
            ["Clause to filter records?", "Easy", ["GROUP", "WHERE", "ORDER", "HAVING"], "B"],
            ["Select all columns?", "Easy", ["ALL", "*", "EVERY", "COLUMNS"], "B"],
            ["Keyword to sort?", "Easy", ["SORT", "ARRANGE", "ORDER BY", "SET"], "C"],
            ["Insert data command?", "Easy", ["ADD", "INSERT INTO", "PUT", "UPDATE"], "B"],
            ["Delete data statement?", "Easy", ["COLLAPSE", "REMOVE", "DELETE", "DROP"], "C"],
            ["Unique values keyword?", "Easy", ["UNIQUE", "DISTINCT", "DIFF", "SELECT"], "B"],
            ["Update data command?", "Easy", ["SAVE", "MODIFY", "UPDATE", "CHANGE"], "C"],
            ["Create database command?", "Easy", ["MAKE", "NEW", "CREATE DATABASE", "ADD"], "C"],
            ["Delete table structure?", "Easy", ["DELETE", "REMOVE", "DROP", "TRUNCATE"], "C"],
            ["Check for NULL?", "Easy", ["= NULL", "IS NULL", "== NULL", "NOT NULL"], "B"],
            ["Wildcard for multiple chars?", "Easy", ["?", "*", "%", "$"], "C"],
            ["Primary Key must be?", "Easy", ["Unique", "NULL", "Duplicate", "String"], "A"],
            ["Join two tables keyword?", "Easy", ["LINK", "JOIN", "CONNECT", "UNION"], "B"],
            
            # Medium (15 total)
            ["Match in either table?", "Medium", ["INNER", "LEFT", "RIGHT", "FULL OUTER"], "D"],
            ["Function for row count?", "Medium", ["SUM", "TOTAL", "COUNT", "ROWS"], "C"],
            ["DELETE vs TRUNCATE?", "Medium", ["None", "TRUNCATE rollback", "DELETE DDL", "TRUNCATE DDL"], "D"],
            ["Unique record ID?", "Medium", ["UNIQUE", "FOREIGN", "PRIMARY", "CHECK"], "C"],
            ["HAVING used with?", "Medium", ["ORDER", "GROUP BY", "WHERE", "JOIN"], "B"],
            ["Default ORDER BY?", "Medium", ["DESC", "ASC", "Random", "None"], "B"],
            ["Pattern search operator?", "Medium", ["GET", "MATCH", "LIKE", "FIND"], "C"],
            ["UNION purpose?", "Medium", ["Join", "Combine SELECTs", "Update", "Delete"], "B"],
            ["Change table structure?", "Medium", ["CHANGE", "MODIFY", "ALTER", "UPDATE"], "C"],
            ["Foreign Key purpose?", "Medium", ["Unique", "Relationship", "Backup", "Index"], "B"],
            ["String concatenation in SQL?", "Medium", ["+", "CONCAT()", "&&", "||"], "B"],
            ["Index purpose?", "Medium", ["Security", "Speed", "Space", "Backup"], "B"],
            ["BETWEEN is inclusive?", "Medium", ["Yes", "No", "Depends on DB", "Only for dates"], "A"],
            ["IN operator checks for?", "Medium", ["Range", "List of values", "Pattern", "Null"], "B"],
            ["AS keyword is for?", "Medium", ["Sort", "Alias", "Filter", "Join"], "B"],

            # Hard (10 total)
            ["Normalization purpose?", "Hard", ["Increase redundancy", "Reduce redundancy", "Speed", "Encrypt"], "B"],
            ["Transitive Dependency form?", "Hard", ["1NF", "2NF", "3NF", "BCNF"], "C"],
            ["ACID 'I' stands for?", "Hard", ["Info", "Integrate", "Isolation", "Index"], "C"],
            ["Partial dependency form?", "Hard", ["1NF", "2NF", "3NF", "4NF"], "B"],
            ["Composite Key definition?", "Hard", ["Multi-column", "Foreign", "Hidden", "String"], "A"],
            ["WHERE vs HAVING?", "Hard", ["None", "Row vs Group", "Group vs Row", "Speed"], "B"],
            ["Stored Procedure?", "Hard", ["Table", "Precompiled SQL", "Backup", "Log"], "B"],
            ["Revoke privileges?", "Hard", ["DENY", "REMOVE", "REVOKE", "UNGRANT"], "C"],
            ["What is a View?", "Hard", ["Backup", "Virtual Table", "Physical Copy", "GUI"], "B"],
            ["ACID 'D' stands for?", "Hard", ["Data", "Durability", "Delete", "Design"], "B"]
        ],
        "Object Oriented Programming (OOP)": [
            # Easy (15 total)
            ["OOP Full Form?", "Easy", ["Object Oriented Programming", "Open", "Office", "Object Open"], "A"],
            ["Fundamental Pillar?", "Easy", ["Recursion", "Inheritance", "Sort", "Loop"], "B"],
            ["Class is a _____?", "Easy", ["Method", "Blueprint", "Variable", "Package"], "B"],
            ["Java object creation keyword?", "Easy", ["class", "create", "new", "this"], "C"],
            ["Wrapping data/methods?", "Easy", ["Inherit", "Poly", "Encapsulation", "Abstract"], "C"],
            ["Non-OOP language?", "Easy", ["C", "C++", "Python", "Java"], "A"],
            ["Instance of a class?", "Easy", ["Object", "Method", "Member", "Constructor"], "A"],
            ["Inheritance keyword in Java?", "Easy", ["implements", "extends", "inherits", "using"], "B"],
            ["Access modifier for all?", "Easy", ["private", "public", "protected", "internal"], "B"],
            ["Python OOP self refers to?", "Easy", ["Class", "Object", "Global", "None"], "B"],
            ["Destructor in C++ starts with?", "Easy", ["*", "&", "~", "!"], "C"],
            ["Does Python support private?", "Easy", ["Yes", "No", "Only for ints", "By convention"], "D"],
            ["Smallest unit of OOP?", "Easy", ["Class", "Method", "Object", "Variable"], "C"],
            ["Can a class have multiple objects?", "Easy", ["No", "Yes", "Only two", "Depends on RAM"], "B"],
            ["OOP focuses on?", "Easy", ["Logic", "Data/Objects", "Procedures", "Flow"], "B"],
            
            # Medium (15 total)
            ["Polymorphism definition?", "Medium", ["Hiding", "Many forms", "Multi-objects", "Reuse"], "B"],
            ["Constructor purpose?", "Medium", ["Destroy", "Initialize", "Sort", "Link"], "B"],
            ["Java missing inheritance?", "Medium", ["Single", "Multiple", "Multilevel", "Hierar"], "B"],
            ["'this' keyword refers to?", "Medium", ["Static", "Current Object", "Class", "Parent"], "B"],
            ["Hiding details, showing function?", "Medium", ["Abstract", "Encapsulation", "Inherit", "Poly"], "A"],
            ["Modifier for same package?", "Medium", ["private", "public", "protected", "default"], "D"],
            ["Static method can access?", "Medium", ["Instance vars", "Static vars", "Both", "Neither"], "B"],
            ["Overloading is ______?", "Medium", ["Compile-time", "Runtime", "Both", "None"], "A"],
            ["Super keyword refers to?", "Medium", ["Child", "Parent", "Global", "Current"], "B"],
            ["Final class cannot be ______?", "Medium", ["Instantiated", "Inherited", "Modified", "Deleted"], "B"],
            ["Method signature includes?", "Medium", ["Return type", "Name/Params", "Body", "Access"], "B"],
            ["Abstract class can have body?", "Medium", ["Yes", "No", "Only in Java", "Only in C++"], "A"],
            ["Interface members are by default?", "Medium", ["Private", "Public/Abstract", "Static", "Final"], "B"],
            ["Multiple inheritance in C++?", "Medium", ["Yes", "No", "Only for structs", "Virtual only"], "A"],
            ["Friend function can access?", "Medium", ["Public", "Private", "Global", "Nothing"], "B"],

            # Hard (10 total)
            ["Abstract Class instantiation?", "Hard", ["Can", "Cannot", "Only if static", "Only if final"], "B"],
            ["Overloading vs Overriding?", "Hard", ["None", "Compile vs Runtime", "Runtime vs Compile", "Sort"], "B"],
            ["What is an Interface?", "Hard", ["Screen", "Contract", "Type", "Private"], "B"],
            ["Diamond Problem is in ______?", "Hard", ["Bug", "Multiple Inheritance", "Memory", "Sort"], "B"],
            ["Overriding demonstrates ______?", "Hard", ["Encapsulate", "Abstract", "Runtime Poly", "Static Poly"], "C"],
            ["Pure Virtual Function makes class?", "Hard", ["Static", "Private", "Abstract", "Final"], "C"],
            ["Virtual Destructor purpose?", "Hard", ["Speed", "Proper cleanup", "Security", "Space"], "B"],
            ["Composition vs Inheritance?", "Hard", ["Same", "Has-a vs Is-a", "Is-a vs Has-a", "None"], "B"],
            ["Shallow vs Deep Copy?", "Hard", ["Same", "Ref vs Value", "Value vs Ref", "Memory"], "B"],
            ["Coupling in OOP should be?", "Hard", ["High", "Low", "Medium", "Zero"], "B"]
        ]
    }

    for topic_name, questions in data.items():
        add_questions(topic_name, questions)

if __name__ == "__main__":
    populate()
