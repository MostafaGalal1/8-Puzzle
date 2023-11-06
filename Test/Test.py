# Import the unittest module for testing
import unittest

# Import the Algorithm_Factory and necessary classes
from Algorithms.Algorithm_Factory import *


# Define a test class that inherits from unittest.TestCase
class Test(unittest.TestCase):
    # Define a list of algorithms and heuristics for testing
    algorithms = [
        ("A-Star", "Manhattan"),
        ("A-Star", "Euclidean"),
        ("DFS", None),
        ("BFS", None)
    ]

    # Define a test method to check if a solvable puzzle is indeed solvable for different algorithms
    def Solvable(self, initial_state):
        for algorithm, heuristic in self.algorithms:
            print(f"\n{algorithm}{' with ' + heuristic if heuristic else ''}:")
            puzzle = get_algorithm(initial_state, algorithm, heuristic)
            solution = puzzle.solve()
            print("Cost:", solution.stringify())
            self.assertTrue(solution.solvable)

    # Define a test method to check if an unsolvable puzzle is indeed not solvable for different algorithms
    def notSolvable(self, initial_state, algorithm, heuristic=None):
        puzzle = get_algorithm(initial_state, algorithm, heuristic)
        solution = puzzle.solve()
        self.assertFalse(solution.solvable)

    # Define a test method to check solvability for various initial states
    def test_isSolvable(self):
        initial_states = [
            312045678,
            125340678,
            125348670,
            125348607,
            125308647,
            125038647,
            125638047,
            125638407,
            125638470,
            125630478,
            123406758,
            123456708,
            867254301,
            867254031,
            876543210,
            87654321,
            806547231,
            125340678,
            142658730,
            102754863
        ]

        for i, initial_state in enumerate(initial_states, 1):
            print(f'\n######## {i} ########')
            print(initial_state)
            self.Solvable(initial_state)

    # Define a test method to check non-solvability for various initial states
    def test_notSolvable(self):
        initial_states = [
            123456870,
            812043765,
            231054786,
            182453760
        ]
        for initial_state in initial_states:
            for algorithm, heuristic in self.algorithms:
                self.notSolvable(initial_state, algorithm, heuristic)

    def test_Optimality1(self):
        puzzle1 = get_algorithm(125340678, "BFS")
        puzzle2 = get_algorithm(125340678, "A-Star", "Manhattan")
        puzzle3 = get_algorithm(125340678, "A-Star", "Manhattan")
        solutions = [puzzle1.solve().cost, puzzle2.solve().cost, puzzle3.solve().cost]
        assert all(value == 3 for value in solutions)

    def test_Optimality2(self):
        puzzle1 = get_algorithm(125630478, "BFS")
        puzzle2 = get_algorithm(125630478, "A-Star", "Manhattan")
        puzzle3 = get_algorithm(125630478, "A-Star", "Manhattan")
        solutions = [puzzle1.solve().cost, puzzle2.solve().cost, puzzle3.solve().cost]
        assert all(value == 11 for value in solutions)

    def test_Optimality3(self):
        puzzle1 = get_algorithm(874562301, "BFS")
        puzzle2 = get_algorithm(874562301, "A-Star", "Manhattan")
        puzzle3 = get_algorithm(874562301, "A-Star", "Manhattan")
        solutions = [puzzle1.solve().cost, puzzle2.solve().cost, puzzle3.solve().cost]
        assert all(value == 27 for value in solutions)

    # Define test methods for Depth-First Search (DFS)
    def test_DFS1(self):
        puzzle = get_algorithm(125340678, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 61579)
        self.assertEqual(solution.nodes_expanded, 117959)
        self.assertEqual(solution.search_depth, 66743)

    def test_DFS2(self):
        puzzle = get_algorithm(312045678, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 1)
        self.assertEqual(solution.nodes_expanded, 181440)
        self.assertEqual(solution.search_depth, 67099)

    def test_DFS3(self):
        puzzle = get_algorithm(874562301, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 67427)
        self.assertEqual(solution.nodes_expanded, 95246)
        self.assertEqual(solution.search_depth, 67471)

    def test_DFS4(self):
        puzzle = get_algorithm(150273468, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 36652)
        self.assertEqual(solution.nodes_expanded, 150699)
        self.assertEqual(solution.search_depth, 66744)

    def test_DFS5(self):
        puzzle = get_algorithm(123456780, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 24336)
        self.assertEqual(solution.nodes_expanded, 25590)
        self.assertEqual(solution.search_depth, 24336)

    def test_DFS6(self):
        puzzle = get_algorithm(125630478, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 38047)
        self.assertEqual(solution.nodes_expanded, 149346)
        self.assertEqual(solution.search_depth, 66743)

    # Define test methods for Breadth-First Search (BFS)
    def test_BFS1(self):
        puzzle = get_algorithm(312045678, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 1)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 2)

    def test_BFS2(self):
        puzzle = get_algorithm(125340678, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 13)
        self.assertEqual(solution.search_depth, 4)

    def test_BFS3(self):
        puzzle = get_algorithm(874562301, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 27)
        self.assertEqual(solution.nodes_expanded, 176800)
        self.assertEqual(solution.search_depth, 28)

    def test_BFS4(self):
        puzzle = get_algorithm(150273468, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 18)
        self.assertEqual(solution.nodes_expanded, 26012)
        self.assertEqual(solution.search_depth, 19)

    def test_BFS5(self):
        puzzle = get_algorithm(123456780, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 22)
        self.assertEqual(solution.nodes_expanded, 83783)
        self.assertEqual(solution.search_depth, 23)

    def test_BFS6(self):
        puzzle = get_algorithm(125630478, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 11)
        self.assertEqual(solution.nodes_expanded, 861)
        self.assertEqual(solution.search_depth, 12)

    # Define test methods for A-Star with Manhattan heuristic
    def test_Manhattan1(self):
        puzzle = get_algorithm(125340678, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 3)

    def test_Manhattan2(self):
        puzzle = get_algorithm(142658730, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 8)
        self.assertEqual(solution.nodes_expanded, 11)
        self.assertEqual(solution.search_depth, 8)

    def test_Manhattan3(self):
        puzzle = get_algorithm(874562301, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 27)
        self.assertEqual(solution.nodes_expanded, 2410)
        self.assertEqual(solution.search_depth, 27)

    def test_Manhattan4(self):
        puzzle = get_algorithm(150273468, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 18)
        self.assertEqual(solution.nodes_expanded, 222)
        self.assertEqual(solution.search_depth, 18)

    def test_Manhattan5(self):
        puzzle = get_algorithm(123456780, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 22)
        self.assertEqual(solution.nodes_expanded, 769)
        self.assertEqual(solution.search_depth, 22)

    def test_Manhattan6(self):
        puzzle = get_algorithm(125630478, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 11)
        self.assertEqual(solution.nodes_expanded, 24)
        self.assertEqual(solution.search_depth, 11)

    # Define test methods for A-Star with Euclidean heuristic
    def test_Euclidean1(self):
        puzzle = get_algorithm(125340678, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 3)

    def test_Euclidean2(self):
        puzzle = get_algorithm(142658730, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 8)
        self.assertEqual(solution.nodes_expanded, 13)
        self.assertEqual(solution.search_depth, 8)

    def test_Euclidean3(self):
        puzzle = get_algorithm(874562301, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 27)
        self.assertEqual(solution.nodes_expanded, 11987)
        self.assertEqual(solution.search_depth, 27)

    def test_Euclidean4(self):
        puzzle = get_algorithm(150273468, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 18)
        self.assertEqual(solution.nodes_expanded, 253)
        self.assertEqual(solution.search_depth, 18)

    def test_Euclidean5(self):
        puzzle = get_algorithm(123456780, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 22)
        self.assertEqual(solution.nodes_expanded, 2174)
        self.assertEqual(solution.search_depth, 22)

    def test_Euclidean6(self):
        puzzle = get_algorithm(125630478, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 11)
        self.assertEqual(solution.nodes_expanded, 54)
        self.assertEqual(solution.search_depth, 11)


# Check if this script is being run as the main program
if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
