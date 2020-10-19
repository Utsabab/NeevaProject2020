class Node:
    def __init__(self,val, next):
        self.val = val
        self.next = next


class ImprovedEditor:
    def __init__(self, document):
        self.dictionary = set()
        with open("dictionary.txt") as input_dictionary:
            for line in input_dictionary:
                words = line.strip().split(" ")
                for word in words:
                    self.dictionary.add(word)

        self.document = list(document)
        self.pastehead = Node(None, None)
        self.root = Node("", None)
        temp = self.root
        for i in self.document:
            temp.next = Node(i, None)
            temp = temp.next

    def cut(self, i, j):
        temp = self.root
        prev = None
        pasteheadtemp = self.pastehead
        for ind in range(j+1):
            if ind == i+1:
                cutpoint = prev
            if (ind >= i+1) and (ind < j+1):
                pasteheadtemp.next = Node(temp.val, None)
                pasteheadtemp = pasteheadtemp.next
            prev = temp
            temp = temp.next
        cutpoint.next = temp
        pasteheadtemp.next = None

        return self.get_text()

    def copy(self, i, j):
        temp = self.root
        pasteheadtemp = self.pastehead
        for ind in range(j+1):
            if (ind >= i+1) and (ind < j+1):
                pasteheadtemp.next = Node(temp.val, None)
                pasteheadtemp = pasteheadtemp.next
            temp = temp.next
        pasteheadtemp.next = None

        return self.get_text()

    def paste(self, i):
        temp = self.root
        pastehead_dummy = self.pastehead.next
        new_pastehead = Node(pastehead_dummy.val, None)
        pastehead_temp = new_pastehead
        while pastehead_dummy:
            pastehead_dummy = pastehead_dummy.next
            if not pastehead_dummy:
                break
            pastehead_temp.next = Node(pastehead_dummy.val, None)
            pastehead_temp = pastehead_temp.next

        for ind in range(i+2):
            if ind == i:
                half = temp.next
                temp.next = new_pastehead
                while new_pastehead.next:
                    new_pastehead = new_pastehead.next
                continue
            if ind == i+1:
                new_pastehead.next = half
            temp = temp.next
        return self.get_text()

    def get_text(self):
        result = ""
        self.test_pointer = self.root.next
        while self.test_pointer:
            result += self.test_pointer.val
            self.test_pointer = self.test_pointer.next
        return result

    def misspellings(self):
        result = 0
        curr_str = ""
        temp = self.root.next

        while temp:
            if temp.val == " ":
                if curr_str not in self.dictionary:
                    result += 1
                temp = temp.next
                curr_str = ""
                continue
            curr_str += temp.val.lower()
            temp = temp.next
        if curr_str not in self.dictionary:
            result += 1
        return result


class SimpleEditor:
    def __init__(self, document):
        self.document = document
        self.dictionary = set()
        # On windows, the dictionary can often be found at:
        with open("dictionary.txt") as input_dictionary:
            for line in input_dictionary:
                words = line.strip().split(" ")
                for word in words:
                    self.dictionary.add(word)
        self.paste_text = ""

    def cut(self, i, j):
        self.paste_text = self.document[i:j]
        self.document = self.document[:i] + self.document[j:]
        # print(self.document)

    def copy(self, i, j):
        self.paste_text = self.document[i:j]
        # print(self.document)

    def paste(self, i):
        self.document = self.document[:i] + self.paste_text + self.document[i:]
        # print(self.document)

    def get_text(self):
        # print(self.document)
        return self.document

    def misspellings(self):
        # print(self.document)
        result = 0
        for word in self.document.split(" "):
            if word not in self.dictionary:
                result = result + 1
        return result


import timeit


class SimpleEditorBenchmarker:
    new_editor_case = """
from __main__ import SimpleEditor
s = SimpleEditor("{}")"""

    editor_cut_paste = """
for n in range({}):
    if n%2 == 0:
        s.cut(1, 3)
    else:
        s.paste(2)"""

    editor_copy_paste = """
for n in range({}):
    if n%2 == 0:
        s.copy(1, 3)
    else:
        s.paste(2)"""

    editor_get_text = """
for n in range({}):
    s.get_text()"""

    editor_mispellings = """
for n in range({}):
    s.misspellings()"""

    def __init__(self, cases, N):
        self.cases = cases
        self.N = N
        self.editor_cut_paste = self.editor_cut_paste.format(N)
        self.editor_copy_paste = self.editor_copy_paste.format(N)
        self.editor_get_text = self.editor_get_text.format(N)
        self.editor_mispellings = self.editor_mispellings.format(N)

    def benchmark(self):
        print("Default Benchmark")
        for case in self.cases:
            print("Evaluating case: {}".format(case))
            new_editor = self.new_editor_case.format(case)
            cut_paste_time = timeit.timeit(stmt=self.editor_cut_paste, setup=new_editor, number=1)
            print("{} cut paste operations took {} s".format(self.N, cut_paste_time))
            copy_paste_time = timeit.timeit(stmt=self.editor_copy_paste, setup=new_editor, number=1)
            print("{} copy paste operations took {} s".format(self.N, copy_paste_time))
            get_text_time = timeit.timeit(stmt=self.editor_get_text, setup=new_editor, number=1)
            print("{} text retrieval operations took {} s".format(self.N, get_text_time))
            mispellings_time = timeit.timeit(stmt=self.editor_mispellings, setup=new_editor, number=1)
            print("{} mispelling operations took {} s".format(self.N, mispellings_time))


class ImprovedEditorBenchmarker:
    new_editor_case = """
from __main__ import ImprovedEditor
s = ImprovedEditor("{}")"""

    editor_cut_paste = """
for n in range({}):
    if n%2 == 0:
        s.cut(1, 3)
    else:
        s.paste(2)"""

    editor_copy_paste = """
for n in range({}):
    if n%2 == 0:
        s.copy(1, 3)
    else:
        s.paste(2)"""

    editor_get_text = """
for n in range({}):
    s.get_text()"""

    editor_mispellings = """
for n in range({}):
    s.misspellings()"""

    def __init__(self, cases, N):
        self.cases = cases
        self.N = N
        self.editor_cut_paste = self.editor_cut_paste.format(N)
        self.editor_copy_paste = self.editor_copy_paste.format(N)
        self.editor_get_text = self.editor_get_text.format(N)
        self.editor_mispellings = self.editor_mispellings.format(N)

    def benchmark(self):
        print("Improved Benchmark")
        for case in self.cases:
            print("Evaluating case: {}".format(case))
            new_editor = self.new_editor_case.format(case)
            cut_paste_time = timeit.timeit(stmt=self.editor_cut_paste, setup=new_editor, number=1)
            print("{} cut paste operations took {} s".format(self.N, cut_paste_time))
            copy_paste_time = timeit.timeit(stmt=self.editor_copy_paste, setup=new_editor, number=1)
            print("{} copy paste operations took {} s".format(self.N, copy_paste_time))
            get_text_time = timeit.timeit(stmt=self.editor_get_text, setup=new_editor, number=1)
            print("{} text retrieval operations took {} s".format(self.N, get_text_time))
            mispellings_time = timeit.timeit(stmt=self.editor_mispellings, setup=new_editor, number=1)
            print("{} mispelling operations took {} s".format(self.N, mispellings_time))

if __name__ == "__main__":
    s = SimpleEditorBenchmarker(["Hello friend", open("lorem.txt").read()], 100)
    s.benchmark()
    i = ImprovedEditorBenchmarker(["Hello friend", open("lorem.txt").read()], 100)
    i.benchmark()