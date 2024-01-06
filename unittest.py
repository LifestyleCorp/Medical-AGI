import unittest
from Main import Character, EventManager

event_manager = EventManager()  # character_list is a list of Character objects.

class TestHospitalSimulation(unittest.TestCase):
    def test_character_creation(self):
        # Test that character is correctly created and initialized.
        character = Character('doctor', (1, 1))
        self.assertIsNotNone(character)
        self.assertEqual(character.role, 'doctor')

    def test_event_trigger(self):
        # Setup your characters and event manager.
        # character_list and event_manager would be created here.
        event_manager.trigger_event()  # Trigger an event.
        # Assert the expected changes due to the event.

# ... Define more test methods for each component and interaction.

if __name__ == '__main__':
    unittest.main()
