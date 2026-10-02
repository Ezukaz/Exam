# py_array_rotation_detector

py_array_rotation_detector.py

>⚡
Moulinette Rules & Constraints<br>
Forbidden built-ins / modules: collections.deque.rotate().<br>
Use only permitted built-in functions to avoid getting 0 on exam day.

### Assignment

Determine if array2 is a rotation of array1.<br>A rotation shifts elements cyclically while maintaining relative order.

- Return True if array2 is a valid rotation of array1
- Return False otherwise or if array lengths differ
- Handle empty arrays (two empty arrays are considered valid rotations)

### Function signature

```python
def array_rotation_detector(arr1: list, arr2: list) -> bool:
```

### Examples

>Input<br>
```array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])```<br>
Output<br>
```True```<br>
Input<br>
```array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])```<br>
Output<br>
```True```<br>
Input<br>
```array_rotation_detector([1, 2, 3], [3, 2, 1])```<br>
Output<br>
```False```<br>
Input<br>
```array_rotation_detector([1, 2], [1, 2, 3])```<br>
Output<br>
```False```<br>
Input<br>
```array_rotation_detector([], [])```<br>
Output<br>
```True```<br>
