class ContextFreeGrammar:
    def _init_(self):
        self.non_terminals = []
        self.terminals = []
        self.rules = {}
        self.start_symbol = None

    def terminals_list(self):
        """
        :return: List of terminal symbols.
        """
        return self.terminals

    def non_terminals_list(self):
        """
        :return: List of non-terminal symbols.
        """
        return self.non_terminals

    def start_sym(self):
        """
        :return: The start symbol.
        """
        return self.start_symbol

    def productions_for(self, non_terminal):
        """
        :param non_terminal: Non-terminal symbol to get productions for.
        :return: List of production rules for the given non-terminal.
        """
        return self.rules.get(non_terminal, [])

    def has_additional_production(self, non_terminal, production_number):
        """
        Checks if there is an additional production rule for a given non-terminal symbol.
        :param non_terminal: Non-terminal symbol to check.
        :param production_number: Current production number.
        :return: True if there is another production, False otherwise.
        """
        return self.rules[non_terminal][-1][1] != production_number

    def specific_production(self, non_terminal, production_number):
        """
        :param non_terminal: Non-terminal symbol to get the production for.
        :param production_number: The production number to retrieve.
        :return: Specific production rule if found, None otherwise.
        """
        for production in self.rules[non_terminal]:
            if production[1] == production_number:
                return production

    def load_grammar(self, file_path):
        """
        :param file_path: Path to the file containing the grammar.
        :raises ValueError: If the grammar is not a valid context-free grammar.
        """
        with open(file_path, 'r') as file:
            self.non_terminals = self._parse_line(file.readline())
            self.terminals = self._parse_line(file.readline())
            self.start_symbol = file.readline().split('=')[1].strip()
            file.readline()
            prod_rules = [line.strip() for line in file]
            self.rules = self._interpret_rules(prod_rules)

            if not self._is_valid_cfg(prod_rules):
                raise ValueError('The provided grammar is not a valid CFG')

    def display_non_terminals(self):
        """
        :return: String of non-terminal symbols.
        """
        return str(self.non_terminals)

    def display_terminals(self):
        """
        :return: String of terminal symbols.
        """
        return str(self.terminals)

    def display_start_symbol(self):
        """
        :return: String of the start symbol.
        """
        return str(self.start_symbol)

    def display_productions(self):
        """
        :return: String of production rules.
        """
        return str(self.rules)

    @staticmethod
    def _parse_line(line):
        """
        :param line: Line from the grammar file.
        :return: List of symbols extracted from the line.
        """
        parts = line.strip().split('=', 1)[1]
        if parts.strip()[-1] == ',':
            parts = [',']
        return [item.strip() for item in parts.split(',')]

    @staticmethod
    def _interpret_rules(rule_lines):
        """
        :param rule_lines: Lines from the grammar file representing the rules.
        :return: Dictionary of interpreted production rules.
        """
        productions = {}
        index = 1

        for rule in rule_lines:
            left_side, right_side = rule.split('->')
            left_side = left_side.strip()
            right_side = [val.strip() for val in right_side.split('|')]

            for production in right_side:
                if left_side in productions:
                    productions[left_side].append((production, index))
                else:
                    productions[left_side] = [(production, index)]
                index += 1
        return productions

    @staticmethod
    def _is_valid_cfg(rules):
        """
        Checks if the parsed grammar is a valid context-free grammar (CFG).
        Ensures that each production rule adheres to the format required for CFGs.
        check if the lhs of each production rule contains only a single non-terminal symbol
        :param rules: List of rules to be checked.
        :return: True if valid CFG, False otherwise.
        """
        for rule in rules:
            lhs, _ = rule.split('->')
            lhs = lhs.strip()
            if sum(element.strip() in lhs for element in lhs.split('|')) > 1:
                return False
        return True

    # Context free grammar : if the grammar is a context-free grammar by ensuring that every left-hand side
    # of a rule has the form of a single non-terminal symbol.

    """
        Terminals are the basic symbols or tokens that appear in the language generated by the grammar. These symbols are the
    fundamental building blocks that form the strings in the language. In a context-free grammar, terminals are symbols 
    that don't get replaced during the derivation process. They represent actual elements or tokens in the language being
    described. For instance, in a grammar for arithmetic expressions, terminals might include numbers (like 0, 1, 2, etc.),
    operators (+, -, *, /), and parentheses.

        Non-terminals are symbols used to represent groups of strings that can be derived from the grammar. They serve 
    as placeholders that can be replaced by other symbols or groups of symbols through production rules. Non-terminals 
    do not appear directly in the strings of the language; instead, they represent syntactic categories or structures.
    They provide a way to define the rules or patterns for generating valid strings in the language. For instance, in a 
    grammar for arithmetic expressions, non-terminals might include symbols like <expression>, <term>, <factor>, etc.


        The starting symbol (also known as the start variable) is a special non-terminal symbol from which the derivation of
    the entire language begins. It represents the initial point where the generation or derivation of strings starts 
    within the grammar. All valid strings in the language must be derivable from this starting symbol by applying 
    production rules. It acts as the root or the beginning point of the derivation process.


         Production rules, often referred to as production or rewrite rules, are fundamental components of formal grammars 
    (such as context-free grammars) used to generate valid strings in a language. These rules define how symbols or 
    strings of symbols can be replaced or rewritten by other symbols or strings of symbols in a grammar.

    In a context-free grammar (CFG), a production rule typically has the form:   A→β
    Where:
             A is a non-terminal symbol (also known as the left-hand side or LHS of the production rule). It represents a 
        syntactic category or a placeholder that can be replaced.
             β is a string of zero or more terminal and/or non-terminal symbols (also known as the right-hand side or RHS of 
        the production rule). It indicates what A can be replaced with in the derivation process.

    """