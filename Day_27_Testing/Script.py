def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):

    array = []
    for i in range(10):
        array.append(i)
    @staticmethod
    def get_array():
        return TestDataUniqueValues.array

    @staticmethod
    def get_expected_result():
        index_sorted_array = sorted(range(len(TestDataUniqueValues.array)), key=lambda k: TestDataUniqueValues.array[k])
        return TestDataUniqueValues.array[index_sorted_array[0]]

class TestDataExactlyTwoDifferentMinimums(object):
    
    array = []
    for i in range(10):
        array.append(i)
    array.insert(5,0)
    @staticmethod
    def get_array():
        return TestDataExactlyTwoDifferentMinimums.array

    @staticmethod
    def get_expected_result():
        index_sorted_array = sorted(range(len(TestDataExactlyTwoDifferentMinimums.array)), key=lambda k: TestDataExactlyTwoDifferentMinimums.array[k])
        return TestDataExactlyTwoDifferentMinimums.array[index_sorted_array[0]]


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
