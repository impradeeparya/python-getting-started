class Solution:

    def words_diff(self, first_word, second_word):
        diff_count = 0

        for index in range(len(first_word)):
            if first_word[index] != second_word[index]:
                diff_count = diff_count + 1

        return diff_count

    def wordLadderLength(self, startWord, targetWord, wordList):
        # Code here
        n = len(wordList)

        target_index = -1
        for index in range(len(wordList)):
            if targetWord == wordList[index]:
                target_index = index
                break;

        if target_index == -1:
            return 0

        adjacency_matrix = [[0 for i in range(n)] for j in range(n)]

        for row in range(len(wordList)):
            for column in range(row + 1, len(wordList)):
                diff_count = self.words_diff(wordList[row], wordList[column])
                if diff_count == 1:
                    adjacency_matrix[row][column] = 1
                    adjacency_matrix[column][row] = 1
                elif diff_count > 1:
                    adjacency_matrix[row][column] = -1
                    adjacency_matrix[column][row] = -1

        adjacency_queue = []
        is_start_word_present = False
        for index in range(len(wordList)):
            diff_count = self.words_diff(startWord, wordList[index])
            if diff_count == 1:
                adjacency_queue.append(index)
            elif diff_count == 0:
                adjacency_queue.clear()
                adjacency_queue.append(index)
                is_start_word_present = True
                break;

        adjacency_queue.append(-1)
        # print(adjacency_queue, target_index)

        is_path_found = False
        distance = 1 if is_start_word_present else 2

        while len(adjacency_queue) > 0:
            # print("adjacency_queue : ", adjacency_queue, distance)
            index = adjacency_queue.pop(0)

            if index == target_index:
                is_path_found = True
                break
            elif index == -1:
                if len(adjacency_queue) == 0:
                    break
                adjacency_queue.append(-1)
                distance = distance + 1
            else:
                for column in range(n):
                    current_distance = adjacency_matrix[index][column]
                    if current_distance == 1:
                        adjacency_queue.append(column)
                        adjacency_matrix[column][index] = -1
                        adjacency_matrix[index][column] = distance

        return distance if is_path_found else 0


print(Solution().wordLadderLength("der", "dfs", ["des", "der", "dfr", "dgt", "dfs"]))
print(Solution().wordLadderLength("gedk", "geek", ["geek", "gefk"]))
print(Solution().wordLadderLength("toon", "plea", ["poon", "plee", "same", "poie", "plea", "plie", "poin"]))
