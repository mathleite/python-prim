from re import match


class NodeHandler:
    def __init__(self, file):
        self._graph = []
        self._file = file
        self._greatest_node = -1

    def node_roaming(self):
        for line in self._file:
            self.append_edge_if_not_comment(line)


    def create_node_dictionary(self, line_info):
        return {
            line_info[0] + "&" + line_info[1]: line_info[2].replace('\n', '')
        }

    def retrieve_greatest_node(self, first_node, last_node):
        if first_node > last_node:
            return first_node
        return  last_node

    def append_edge_if_not_comment(self, file_line):
        if not match("//", file_line):
            line_info = file_line.split(" ")
            self._greatest_node = self.retrieve_greatest_node(int(line_info[0]), int(line_info[1]))
            self._graph.append(self.create_node_dictionary(line_info))


    @property
    def greatest_node(self):
        return self._greatest_node

    @property
    def graph(self):
        return self._graph
