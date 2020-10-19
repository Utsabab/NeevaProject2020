#Text Editor

## Problem Overview

Engineers at QwickType Software discovered they spent a lot of time copying and 
pasting the code. Hence, they decided to build their own text editor to speedup
the process. However, the text editor was even slower than the process before.
This project focuses on reimplementing the text editor for better performance
provided with the text processing logic written by the developers at QwickType.

## Background

The logic for the operations built initially for the text editor used string and slicing to generate the 
texts. While string is easy to manipulate, it is immutable. Every change that occurs 
in a string will generate a new string. Hence, every time we do cut and paste operations, 
the code ended up creating new strings which will result in memory wastage and bad runtime.

## Approach/Design

The approach I adapted is to use LinkedList data structure. LinkedList is a dynamic data structure
which grows and shrinks at runtime by allocating and deallocating memory. LinkedList is well known
for it's advantage of having better runtime for insertion and deletion. The pointers in the Linked List
is manipulated during copy and paste operations which will result in less memory wastage.
and also better runtime. 

However, Linked List uses more memory than string as it stores each character as an object.

### Alternatives considered

1) Gap Buffer: A Gap Buffer is dynamic array that allows efficient insertion and deletion
operations clustered near the same location. In our editor, operations occur at any random positions
which beats the purpose.  

2) Rope: Rope is an approach based on Binary tree structure. This works by storing 
strings split into sections and stored as leaves. This approach is more efficient than 
String implementation but in practice, it is complicated to implement, and maintain the code.
 
## Performance Benchmark

*  Evaluating case: "Hello friend"

    Default
    ```
    100 cut paste operations took 0.00011300000000000199 s
    100 copy paste operations took 8.909999999999474e-05 s
    100 text retrieval operations took 2.4599999999999622e-05 s
    100 mispelling operations took 0.00014830000000000398 s
    ```
   
   Improved
   ```
   100 cut paste operations took 0.0025369000000000086 s
   100 copy paste operations took 0.007171299999999992 s
   100 text retrieval operations took 0.0008149000000000073 s
   100 mispelling operations took 0.0006376999999999633 s  
   ```
   
*  Evaluating case: "Lorem ipsum dolor sit amet, consetetur..."

    Default
    ```
    100 cut paste operations took 0.0004693000000000058 s
    100 copy paste operations took 0.0001926999999999901 s
    100 text retrieval operations took 8.259999999998824e-05 s
    100 mispelling operations took 0.06891049999999999 s
   ```
    Improved 
    ```
    100 cut paste operations took 0.41778150000000003 s
    100 copy paste operations took 0.40242770000000005 s
    100 text retrieval operations took 0.42313259999999997 s
    100 mispelling operations took 0.37227830000000006 s
   ```

## How to run

Run Text Editor Benchmark
```
 python editor.py
```

Run Text Editor test
```
python editortest.py
```
## Possible Extensions

*  Fuzz testing the editor implementation to test all the edge cases.
*  Make benchmark code more dynamic.
*  Implement additional functionality like undo/redo, find/replace, etc.

## Authors

Utsab Khakurel


