class SymbolTable:
    def __init__(self, size):
        self.identifier_table = HashTable(size)
        self.int_constant_table = HashTable(size)
        self.string_constant_table = HashTable(size)

    def add_identifier(self, name):
        return self.identifier_table.add(name, None)

    def add_int_constant(self, constant):
        return self.int_constant_table.add(constant, None)

    def add_string_constant(self, constant):
        return self.string_constant_table.add(constant, None)

    def has_identifier(self, name):
        return self.identifier_table.contains(name)

    def has_int_constant(self, constant):
        return self.int_constant_table.contains(constant)

    def has_string_constant(self, constant):
        return self.string_constant_table.contains(constant)

    def get_position_identifier(self, name):
        return self.identifier_table.get_position(name)

    def get_position_int_constant(self, constant):
        return self.int_constant_table.get_position(constant)

    def get_position_string_constant(self, constant):
        return self.string_constant_table.get_position(constant)

    def to_string(self):
        identifier_str = "Identifier Table:\n" + self.identifier_table.to_string()
        int_constant_str = "Integer Constant Table:\n" + self.int_constant_table.to_string()
        string_constant_str = "String Constant Table:\n" + self.string_constant_table.to_string()
        return identifier_str + "\n" + int_constant_str + "\n" + string_constant_str

class HashTable:
    """
    Separate Chaining:
     In separate chaining, each bucket (index) in the hash table maintains a list (or another data structure like a linked list)
     of key-value pairs that hash to the same index. When a collision occurs, the new key-value pair is appended to this list.
    """
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        if isinstance(key, str):
            sum_ascii = sum(ord(char) for char in key)
            return sum_ascii % self.size
        elif isinstance(key, int):
            return key % self.size

    def get_size(self):
        return self.size

    def get_hash_value(self, key):
        return self.hash(key)

    def add(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    raise Exception("Key already exists in the table")
            self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError("Key not found in the table")

    def contains(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for k, _ in self.table[index]:
                if k == key:
                    return True
        return False

    def get_position(self, key):
        index = self.hash(key)
        if self.contains(key):
            return index
        else:
            return -1

    def to_string(self):
        result = []
        for index, items in enumerate(self.table):
            if items is not None:
                result.append(f"{index}: {', '.join([f'{k}: {v}' for k, v in items])}")
            else:
                result.append(f"{index}: None")
        return "\n".join(result)


symbol_table = SymbolTable(10)
symbol_table.add_identifier("var1")
symbol_table.add_int_constant(42)
symbol_table.add_string_constant("hello")
print(symbol_table.to_string())
print(symbol_table.get_position_identifier("var1"))
print(symbol_table.get_position_int_constant(42))
print(symbol_table.get_position_string_constant("world"))
