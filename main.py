# класс объекта {pos: [], peaks: []}
class Peaks:
    def __init__(self, pos, peaks):
        self.pos = pos
        self.peaks = peaks

    def __str__(self):
        return f"pos: {self.pos}, peaks: {self.peaks}"


def find_peaks(arr):
    pos = []
    peaks = []
    length = len(arr)

    if length > 2:
        values = arr[1:-1]

        # перебор списка без учета первого и последнего элементов по индексу
        for index in range(length - 2):
            if values[index] > arr[index] and values[index] >= arr[index + 2]:
                pos.append(index+1)
                peaks.append(arr[index+1])

    return Peaks(pos, peaks)


print(find_peaks([5, 3, 4, 2, 3, 1, 2, 0, 6, 7]))
