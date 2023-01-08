# класс объекта {pos: [], peaks: []}
class Peaks:
    def __init__(self, pos, peaks):
        self.pos = pos
        self.peaks = peaks

    def __str__(self):
        return f"pos: {self.pos}, peaks: {self.peaks}"


def go_up_backward(arr, index):
    while (arr[index] <= arr[index - 1]) and (index > 0):
        index -= 1
    return index


def go_up_forward(arr, index):
    while index <= len(arr) - 2 and arr[index] < arr[index + 1]:
        index += 1
    return index


def go_down_backward(arr, index):
    while (arr[index] >= arr[index - 1]) and (index > 0):
        index -= 1
    return index


def go_down_forward(arr, index):
    while (arr[index] >= arr[index + 1]) and (index < len(arr) - 2):
        index += 1
    return index


def go_to_end_plateau(arr, index):
    while arr[index] == arr[index + 1] and index < len(arr) - 2:
        index += 1
    return index


def find_peaks(arr):
    pos = []
    peaks = []
    length = len(arr)

    if length > 2:
        index = 0
        while index < length - 2:
            if arr[index] > arr[index + 1]:
                pos.append(go_up_backward(arr, index))
                index = go_down_forward(arr, index)

            elif arr[index] < arr[index + 1]:
                index = go_up_forward(arr, index)

            else:
                index = go_to_end_plateau(arr, index)

        for index in pos:
            peaks.append(arr[index])
    return Peaks(pos, peaks)


print(find_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))
