import unittest
import state_machine as sm  
class TestStringMethods(unittest.TestCase):
    def test_changeDirectionToWest(self):
        self.assertEqual(sm.changeDirectionToWest(), 'WEST')
    def test_changeDirectionToEast(self):
        self.assertEqual(sm.changeDirectionToEast(), 'EAST')
    def test_changeDirectionToNorth(self):
        self.assertEqual(sm.changeDirectionToNorth(), 'NORTH')
    def test_changeDirectionToSouth(self):
        self.assertEqual(sm.changeDirectionToSouth(), 'SOUTH')
    
    def test_reversePriorities(self):
        self.assertEqual(sm.reversePriorities(['s','b']),['b','s'])

    def test_toggleBoost(self):
        self.assertFalse(sm.toggleBoost(True))
        self.assertTrue(sm.toggleBoost(False))

    def test_toggleBoost(self):
        teleporter = [[1,1],[2,2]]
        position = [1,1]
        self.assertEqual(sm.teleport(position,teleporter),[2,2])

    def test_deleteBlocker(self):
        stateMap = [['$']]
        position = [0,0]
        sm.deleteBlocker(position,stateMap)
        self.assertEqual(stateMap[0][0],'blank')
    
    def test_transition_from_balnk_to_sharp(self):
        currentState = 'blank'
        nextState = '#'
        self.assertEqual(sm.transition(currentState,nextState,True),[sm.commandLookAround])
    
    def test_transition_from_blank_to_blank(self):
        currentState = 'blank'
        nextState = 'blank'
        self.assertEqual(sm.transition(currentState,nextState,True),[sm.commandMove])
    
    def test_transition_from_blank_to_x_with_boost(self):
        currentState = 'blank'
        nextState = 'x'
        self.assertEqual(sm.transition(currentState,nextState,True),[sm.commandMove, sm.commandDeleteBlocker])
    
    def test_transition_from_blank_to_x_without_boost(self):
        currentState = 'blank'
        nextState = 'x'
        self.assertEqual(sm.transition(currentState,nextState,False),[sm.commandLookAround])

if __name__ == '__main__':
    unittest.main()