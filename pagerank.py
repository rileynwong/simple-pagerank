"""
Simple Python implementation of PageRank algorithm.
"""

def pagerank(graph, n_iterations=1):
    """
    graph: graph object as input
    n_iterations: optional, number of iterations before returning rankings.
        Default set to 1.

    Returns a dictionary where the keys are the node names and the values are
    the calculated pagerank score for that given node.

    Note: An improvement on this algorithm could use DFS to locate source nodes
    and obtain a more efficient ordering for traversing the graph.
    """

    # Initialize values for all nodes s.t. that add up to one
    n = len(graph.nodes)
    init_val = 1.0/n
    ranks = dict(zip(graph.get_nodes(), [init_val] * n))

    # Iterate through nodes and calculate ranking
    for i in range(n_iterations): # TODO: set delta/epsilon for converging
        new_ranks = ranks

        # Calculate new rank for each node
        for node, prev_rank in ranks.items():
            rank_sum = 0.0

            # Iterate through incoming nodes
            for incoming_node in node.inbound:
                numerator = ranks[incoming_node]
                denominator = len(incoming_node.outbound)
                transfer_amount = numerator / denominator

                # Transfer rank score
                new_ranks[incoming_node] = new_ranks[incoming_node] - transfer_amount
                rank_sum = rank_sum + transfer_amount

            new_ranks[node] = ranks[node] + rank_sum

        # Set ranks to the new ranks calculated in this iteration
        ranks = new_ranks

    return ranks

