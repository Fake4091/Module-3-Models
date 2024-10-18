from django.test import TestCase
from app import models

# Create your tests here.


class TestNotes(TestCase):
    def test_create_note(self):
        note = models.new_note("Test", "test")

        self.assertEqual(note.id, 1)
        self.assertEqual(note.title, "Test")
        self.assertEqual(note.description, "test")
        self.assertFalse(note.is_starred)

    def test_view_all_notes(self):
        notes_data = [
            {
                "title": "Test1",
                "description": "test",
                "is_starred": False,
            },
            {
                "title": "Test2",
                "description": "test",
                "is_starred": True,
            },
            {
                "title": "Test3",
                "description": "test",
                "is_starred": False,
            },
        ]

        for note in notes_data:
            models.new_note(note["title"], note["description"], note["is_starred"])

        notes = models.view_notes()

        notes_data = sorted(notes_data, key=lambda n: n["title"])
        notes = sorted(notes, key=lambda n: n.title)

        for data, note in zip(notes_data, notes):
            self.assertEqual(data["title"], note.title)
            self.assertEqual(data["description"], note.description)
            self.assertEqual(data["is_starred"], note.is_starred)

    def test_can_search_title(self):
        notes_data = [
            {
                "title": "Test1",
                "description": "test",
                "is_starred": False,
            },
            {
                "title": "Test2",
                "description": "huzzah",
                "is_starred": True,
            },
            {
                "title": "Test3",
                "description": "test",
                "is_starred": False,
            },
        ]

        for note in notes_data:
            models.new_note(note["title"], note["description"], note["is_starred"])

        self.assertIsNone(models.search_notes_by_title("aousnth"))

        note = models.search_notes_by_title("Test2")

        self.assertIsNotNone(note)
        self.assertEqual(note.description, "huzzah")

    def test_can_view_starred(self):
        notes_data = [
            {
                "title": "Test1",
                "description": "test",
                "is_starred": True,
            },
            {
                "title": "Test2",
                "description": "test",
                "is_starred": False,
            },
            {
                "title": "Test3",
                "description": "test",
                "is_starred": True,
            },
        ]

        for note_data in notes_data:
            models.new_note(
                note_data["title"],
                note_data["description"],
                note_data["is_starred"],
            )

        self.assertEqual(len(models.starred_notes()), 2)

    def test_can_star_unstar_note(self):
        note = models.new_note("Test", "test")
        note = models.star_unstar_note("Test")

        self.assertEqual(note.is_starred, True)

        note = models.star_unstar_note("Test")
        self.assertEqual(note.is_starred, False)

    def test_can_update_note(self):
        note = models.new_note("Test", "test")
        note = models.update_note("Test", "test2")

        self.assertEqual(note.description, "test2")

    def test_can_delete_note(self):
        notes_data = [
            {
                "title": "Test1",
                "description": "test",
                "is_starred": True,
            },
            {
                "title": "Test2",
                "description": "test",
                "is_starred": False,
            },
            {
                "title": "Test3",
                "description": "test",
                "is_starred": True,
            },
        ]

        for note_data in notes_data:
            models.new_note(
                note_data["title"],
                note_data["description"],
                note_data["is_starred"],
            )

        models.delete_note("Test1")

        self.assertEqual(len(models.view_notes()), 2)
