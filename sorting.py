from time import sleep
import numpy as np


test = False

class Array:

    full_array = None

    def stack_it(self):
        to_stack  = np.array(self.values)
        if not np.array_equal(to_stack, self.pile[-1]):
            self.pile = np.vstack((self.pile, np.array(self.values)))
        
    def set_all(self, values):
        for i in range(len(self.values)):
            self.values[i] = values[i]
            self.stack_it()
        for i in range(len(self.values)):
            Array.full_array[self.lower_index + i] = values[i]
            self.stack_it()
            

    def __init__(self, values, lower_index=0):
        self.lower_index = lower_index
        self.values = list(values)
        
        self.pile = np.array(self.values)
        if Array.full_array == None:
            Array.full_array = list(values)

    def swap(self, index1, index2):
        self.values[index2], self.values[index1] = self.values[index1], self.values[index2]
        Array.full_array[self.lower_index + index2], Array.full_array[self.lower_index +
                                                                      index1] = Array.full_array[self.lower_index + index1], Array.full_array[self.lower_index + index2]
        self.stack_it()

    def set(self, index, num):
        self.values[index] = num
        Array.full_array[self.lower_index + index] = num
        self.stack_it()

    def get_len(self):
        return len(self.values)


def bubble_sort(nums):  
    swapped = True
    while swapped:
        swapped = False
        for i in range(nums.get_len() - 1):
            if nums.values[i] > nums.values[i + 1]:
                nums.swap(i, i + 1)
                swapped = True


def selection_sort(nums):  # n^2
    for i in range(nums.get_len()):
        lowest_value_index = i
        for j in range(i + 1, nums.get_len()):
            if nums.values[j] < nums.values[lowest_value_index]:
                lowest_value_index = j
        
        nums.swap(i, lowest_value_index)


def insertion_sort(nums):  # n^2
    for i in range(1, nums.get_len()):
        item_to_insert = nums.values[i]
        j = i - 1
        while j >= 0 and nums.values[j] > item_to_insert:
            nums.set(j + 1, nums.values[j])
            j -= 1
        nums.set(j + 1, item_to_insert)


def heap_sort(nums):  # n * logn

    def heapify(nums, heap_size, root_index):
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        if left_child < heap_size and nums.values[left_child] > nums.values[largest]:
            largest = left_child

        if right_child < heap_size and nums.values[right_child] > nums.values[largest]:
            largest = right_child

        if largest != root_index:
            nums.swap(root_index, largest)
            heapify(nums, heap_size, largest)

    n = nums.get_len()

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums.swap(i, 0)
        heapify(nums, i, 0)


def merge_sort(nums, lower_index=0):  # n * logn
    def merge(left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    if nums.get_len() <= 1:
        return nums.values

    mid = nums.get_len() // 2

    left_list = merge_sort(Array(nums.values[:mid], lower_index))
    right_list = merge_sort(Array(nums.values[mid:], mid), mid)

    nums.set_all(left_list + right_list)

    sorted_list = merge(left_list, right_list)

    nums.set_all(sorted_list)
    return sorted_list


def quick_sort(nums):  # n^2
    def partition(nums, low, high):
        pivot = nums.values[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums.values[i] < pivot:
                i += 1

            j -= 1
            while nums.values[j] > pivot:
                j -= 1

            if i >= j:
                return j

            nums.swap(j, i)

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, nums.get_len() - 1)
