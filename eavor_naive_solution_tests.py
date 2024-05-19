import unittest
import eavor_naive_solution as ns
class TestMethods(unittest.TestCase):
    def test_getInstructions_test_case_1(self):
        stateMap = [['#', '#', '#', '#', '#', '#'], 
                    ['#', '@', 'E', 'blank', '$', '#'], 
                    ['#', 'blank', 'N', 'blank', 'blank', '#'], 
                    ['#', 'x', 'blank', 'blank', 'blank', '#'], 
                    ['#', '#', '#', '#', '#', '#']]
        L = 5
        C = 6
        priorities = ['SOUTH', 'EAST', 'NORTH', 'WEST'] 
        isBoost = False
        position = [1,1]
        teleports = []
        direction = 'SOUTH'
        instructions = ['SOUTH','EAST', 'NORTH', 'EAST', 'EAST']
        self.assertEqual(ns.getInstructions(stateMap,L,C,priorities,isBoost,position,teleports,direction = 'SOUTH'),instructions)

    def test_getInstructions_test_case_1_1(self):
        # note we replace N with x
        stateMap = [['#', '#', '#', '#', '#', '#'], 
                    ['#', '@', 'E', 'blank', '$', '#'], 
                    ['#', 'blank', 'x', 'blank', 'blank', '#'], 
                    ['#', 'x', 'blank', 'blank', 'blank', '#'], 
                    ['#', '#', '#', '#', '#', '#']]
        L = 5
        C = 6
        priorities = ['SOUTH', 'EAST', 'NORTH', 'WEST'] 
        isBoost = False
        position = [1,1]
        teleports = []
        direction = 'SOUTH'
        instructions = ['LOOP']
        self.assertEqual(ns.getInstructions(stateMap,L,C,priorities,isBoost,position,teleports,direction = 'SOUTH'),instructions)

    def test_getInstructions_test_case_2(self):
        stateMap = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
                    ['#', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', '#'], 
                    ['#', 'blank', 'blank', 'S', 'blank', 'blank', 'blank', 'W', 'blank', '#'], 
                    ['#', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', '#'], 
                    ['#', 'blank', 'blank', '$', 'blank', 'blank', 'blank', 'blank', 'blank', '#'], 
                    ['#', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', '#'], 
                    ['#', '@', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', '#'], 
                    ['#', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', '#'], 
                    ['#', 'E', 'blank', 'blank', 'blank', 'blank', 'blank', 'N', 'blank', '#'], 
                    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']] 
        L = 10
        C = 10
        priorities = ['SOUTH', 'EAST', 'NORTH', 'WEST'] 
        isBoost = False
        position = [6,1]
        teleports = []
        direction = 'SOUTH'
        instructions = ['SOUTH', 'SOUTH', 'EAST', 'EAST', 'EAST', 'EAST', 'EAST', 'EAST', 'NORTH', 'NORTH', 'NORTH', 'NORTH', 'NORTH', 'NORTH', 'WEST', 'WEST', 'WEST', 'WEST', 'SOUTH', 'SOUTH']
        self.assertEqual(ns.getInstructions(stateMap,L,C,priorities,isBoost,position,teleports,direction),instructions)


if __name__ == '__main__':
    unittest.main()