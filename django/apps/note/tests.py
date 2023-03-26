# tests.py
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .forms import NoteForm
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        """
        Setup for login user and one note data.
        """
        self.client = Client()
        self.user1 = User.objects.create_user(username='testuser1', 
                                             password='testpass1')
        self.user2 = User.objects.create_user(username='testuser2', 
                                             password='testpass2')
        self.note1 = Note.objects.create(title='Note A', content='Content A',\
                                         user=self.user1)
        self.note2 = Note.objects.create(title='Note B', content='Content B',\
                                         user=self.user2)

    def test_note_new_view(self):
        """
        Test that note_new view can be accessed only by authenticated 
        user and new note can be created.
        """
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.post(reverse('note_new'), 
                                    {'title': 'Note C', 'content': 'Content C'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.filter(user=self.user1).count(), 2)
        self.assertEqual(Note.objects.filter(user=self.user1).last().title, 'Note C')

    def test_note_edit_view(self):
        """
        Test that note_edit view can be accessed only by authenticated 
        user and note can be updated.
        """
        self.client.login(username='testuser2', password='testpass2')
        obj = Note.objects.get(id=self.note2.id)
        response = self.client.post(reverse(
                 'note_edit', args=[self.note2.id]), 
                 {'title': obj.title, 'content': 'Updated Content B'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.get(id=self.note2.id).content, 'Updated Content B')

    def test_note_edit_view_with_invalid_note_id(self):
        """
        Test that note_edit view returns 404 error when an invalid 
        note id is given.
        """
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('note_edit', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_edit_view_with_invalid_user(self):
        """
        Test that note_edit view returns 404 error when an invalid 
        user is accessed.
        """
        self.client.login(username='testuser1', password='testpass1')
        response = self.client.get(reverse('note_edit', args=[self.note2.id]))
        self.assertEqual(response.status_code, 404)

    def test_delete_note(self):
        """
        Test that note_delete view can be accessed only by authenticated 
        user and note can be deleted.
        Test that note_edit view returns 404 error when a deleted note
        id is given.
        """
        # log in as the test user
        self.client.login(username='testuser1', password='testpass1')

        # get the URL for the delete view of the first note
        url = reverse('note_delete', args=[self.note1.pk])

        # send a DELETE request to the URL
        response = self.client.delete(url)

        # check that the response has status code 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # check that the note was deleted from the database
        self.assertFalse(Note.objects.filter(pk=self.note1.pk).exists())

        # try to access the edit view of the deleted note
        url = reverse('note_edit', args=[self.note1.pk])
        response = self.client.get(url)

        # check that the response has status code 404 (not found)
        self.assertEqual(response.status_code, 404)

class NoteFormTestCase(TestCase):
    def test_note_form_valid(self):
        """
        Test NoteForm is valid.
        """
        form_data = {
            'title': 'Note A',
            'content': 'Content A',
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_note_form_invalid_with_title_empty(self):
        """
        Test  NoteForm is invalid because of title data is empty.
        """
        form_data = {
            'title': '',
            'content': 'Content B',
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_note_form_invalid_with_content_empty(self):
        """
        Test  NoteForm is invalid because of content data is empty.
        """
        form_data = {
            'title': 'Title Test',
            'content': '',
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_note_form_invalid_with_title_toolong(self):
        """
        Test  NoteForm is invalid with too long title.
        """
        form_data = {
            'title': 'A' * 201,
            'content': 'Content long',
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_note_form_invalid_with_content_toolong(self):
        """
        Test  NoteForm is invalid with too long content.
        """
        form_data = {
            'title': 'Test Title',
            'content': 'Content long' * 500,
        }
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())


