import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
import threading
import tkinter as tk
from DesktopApp import start_tkinter, on_closing, start_camera_with_delay


class TestCameraFunction(unittest.TestCase):
    @patch('time.sleep', return_value=None)
    @patch('camera.save_frame_camera_cycle')
    def test_start_camera_with_delay(self, mock_save_frame_camera_cycle, mock_sleep):
        # Call the function
        start_camera_with_delay(None)

        # Assert that time.sleep(1) was called
        mock_sleep.assert_called_once_with(1)

        # Assert that camera.save_frame_camera_cycle was called with the correct arguments
        mock_save_frame_camera_cycle.assert_called_once_with(0, '../data/temp', '1', 20)

    @patch('camera.release_camera')
    def test_on_closing(self, mock_release_camera):
        # Create a mock root object
        mock_root = MagicMock()

        # Call the function with the mock root object
        on_closing(mock_root)

        # Assert that camera.release_camera was called
        mock_release_camera.assert_called_once()

    @patch('threading.Thread')
    @patch('DesktopApp.admin.open_admin_page')
    def test_start_tkinter(self, mock_open_admin_page, mock_Thread):
        # Import and mock tkinter
        with patch.dict('sys.modules', {'tkinter': MagicMock(), 'tk': MagicMock()}):
            # Create a mock Tk instance
            mock_Tk_instance = MagicMock()

            # Patch tk.Tk() to return the mock instance
            tk.Tk = MagicMock(return_value=mock_Tk_instance)

            # Call the function
            start_tkinter()

            # Assertions
            mock_Tk_instance.protocol.assert_called_once_with("WM_DELETE_WINDOW",
                                                              mock.ANY)  # WM_DELETE_WINDOW protocol is set

            # Verify that camera thread is started
            mock_Thread.assert_called_once_with(target=mock.ANY, args=(mock_Tk_instance,))
            mock_Thread.return_value.start.assert_called_once()

if __name__ == '__main__':
    unittest.main()
