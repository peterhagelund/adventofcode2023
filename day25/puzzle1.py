from networkx import Graph, connected_components, minimum_edge_cut


def main():
    """Application entry-point."""
    graph = Graph()
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            source, destinations = line.strip().split(":")
            for destination in destinations.strip().split(" "):
                graph.add_edge(source, destination)
    graph.remove_edges_from(minimum_edge_cut(graph))
    group1, group2 = connected_components(graph)
    print(f"group 1: {len(group1)}")
    print(f"group 2: {len(group2)}")
    print(f"product = {len(group1) * len(group2)}")


if __name__ == "__main__":
    main()
