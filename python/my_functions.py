#Colin Duncan
def list_length(list):
    return len(list)
"Given a list, returns an integer representing the length of the list"
def words_start_with_e(words):
    return [x for x in words if x[0] == "e"]
"Given a list of strings, returns a new list containing only the words that start with the letter 'e'"
print(list_length([1,2,3,4,5]))
print(list_length([]))
print(list_length(["a", "b", "c"]))
print(words_start_with_e(["apple", "banana", "elephant", "dog", "exit", "cat", "excited"]))
print(words_start_with_e(["hello", "world", "bye"]))
print(words_start_with_e(["excellent"]))
