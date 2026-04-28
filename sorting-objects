# We have a determined object
class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)

# We can have a default_compare function that wil work with ints for example, but not objects

def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'

# then we adapt sorting algorithms to use a custom compare function.

def insertion_sort(objs, compare):
    nums = list(objs)
    for i in range(len(objs)):
        cur = nums.pop(i)
        j = i-1
        while j >=0:
          result = compare(nums[j], cur)
          if result == 'lesser' or result == 'equal':
            break
          else:
            j -= 1
        nums.insert(j+1, cur)
    return nums

def bubble_sort(objs, compare):
    nums = list(objs)

    for _ in range(len(objs) - 1):

        for i in range(len(objs) - 1):

            result = compare(nums[i], nums[i+1])

            if result == "greater":

                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

# Here is an interesting use, in the partition function for finding the pivot in quicksort

def partition(objs, start=0, end=None, compare=default_compare):
    # print('partition', nums, start, end)
    if end is None:
        end = len(objs) - 1

    # Initialize right and left pointers
    l, r = start, end-1

    # Iterate while they're apart
    while r > l:
        result_l = compare(objs[l], objs[end])
        result_r = compare(objs[r], objs[end])
        # Increment left pointer if number is less or equal to pivot
        if result_l == "lesser" or result_l == "equal":
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif result_r == "greater":
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            objs[l], objs[r] = objs[r], objs[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if compare(objs[l], objs[end]) == "greater":
        objs[l], objs[end] = objs[end], objs[l]
        return l
    else:
        return end


def quicksort(objs, start=0, end=None, compare=default_compare):
    if end is None:
        nums = list(objs)
        end = len(objs) - 1

    if start < end:
        pivot = partition(objs, start, end, compare)
        quicksort(objs, start, pivot-1, compare)
        quicksort(objs, pivot+1, end, compare)

    return objs

# The with mergesort

def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare),
                 merge_sort(objs[mid:], compare),
                 compare)

def merge(left, right, compare=default_compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

# Then, having these objects:

nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]

# We can use any comparing function, for example:

# We define a compare function with any object property

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'

# We call in the sorting functions and sort them

print("Sorting by likes:")
print(merge_sort(notebooks, compare=compare_likes))
print(quicksort(notebooks, compare=compare_likes))
print(insertion_sort(notebooks, compare=compare_likes))
print(bubble_sort(notebooks, compare=compare_likes))

# We can change the comparing function, for example with titles

def compare_title(nb1, nb2):
    if nb1.title > nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title < nb2.title:
        return 'greater'

print("Sorting by title:")
print(merge_sort(notebooks, compare=compare_title))

# Then we can use the algorithms to compare anything, just defining the function and adjusting the comparison
