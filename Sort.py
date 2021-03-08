def bubble_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    nums = [45, 55, 35, 25]
    print('Bubble Sort: ' + ', '.join(str(e) for e in bubble_sort(nums)))
    print('Selection Sort: ' + ', '.join(str(e) for e in selection_sort(nums)))
