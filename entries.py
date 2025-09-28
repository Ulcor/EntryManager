class Entry:
    def __init__(self, title:str, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"{self.title}"

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self # class as a parent work = Entry("Work") /n work.add_entry(work)
        # print(f'Added {entry}')
        # print(f'Entries: {self.entries}')

    def print_entries(self):
        print(self)
        for entry in self.entries:
            print(entry)
            # recursion below!
            # entry.print_entries()

# ???
    def print_reverse(self):
        while self.entry.parent:
            print(self.entry)
            entry = self.entry.parent

# Test
# new_entry = Entry("New Entry")
# print(new_entry)

# Work test
work = Entry("Work")
work.add_entry(work)
print(work)

jira_ticket = Entry("Jira Ticket")
work.add_entry(jira_ticket)

do_report = Entry("Do Report")
work.add_entry(do_report)
print(work.entries)

# Eat test
# entry = Entry('Продукты')
# entry.add_entry(Entry('Молоко'))
# entry.add_entry(Entry('Кофе'))
# entry.add_entry(Entry('Хлеб'))
# entry.add_entry(Entry('Яйца'))

# print(entry.entries)
# entry.print_entries()
# entry.print_reverse()