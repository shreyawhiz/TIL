**Redis** is not a plain key-value store.
It is actually a data structures server, supporting different kinds of values. 

>What this means is that, while in traditional key-value stores you associated string keys to string values, in Redis the value is not limited to a simple string, but can also hold more complex data structures. 

The following is the list of all the data structures supported by Redis :

1. Binary-safe **strings**.
2. **Lists**: collections of string elements sorted according to the order of insertion. They are basically linked lists.
3. **Sets**: collections of unique, unsorted string elements.
4. **Sorted sets**, similar to Sets but where every string element is associated to a floating number value, called score. The elements are always taken sorted by their score, so unlike Sets it is possible to retrieve a range of elements (for example you may ask: give me the top 10, or the bottom 10).
5. **Hashes**, which are maps composed of fields associated with values. Both the field and the value are strings. This is very similar to Ruby or Python hashes.
6. **Bit arrays** (or simply bitmaps): it is possible, using special commands, to handle String values like an array of bits: you can set and clear individual bits, count all the bits set to 1, find the first set or unset bit, and so forth.
7. **HyperLogLogs**: this is a probabilistic data structure which is used in order to estimate the cardinality of a set. Don't be scared, it is simpler than it seems... See later in the HyperLogLog section of this tutorial.
