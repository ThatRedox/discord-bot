from typing import *

from imposter import *
import utils


TEST_FILES_IMAGES = [
    "test.jpg",
    "test.JPG",
    "test.jpeg",
    "test.JPEG",
    "test.png",
    "test.PNG",
    "test.tif",
    "test.TIF",
    "test.tiff",
    "test.TIFF",
    "test.webp",
    "test.WEBP",
    "test.gif",
    "test.GIF",
    "test.mp4",
    "test.MP4",
]
TEST_FILES_NOT_IMAGES = [
    "test.bitmap",
    "test.raw",
    "test.psd",
    "test.txt",
    "test.docx",
    "test.123213123123 1231231 23123 yes png",
    "test.not a jpeg",
]


def test_match_fname():
    for file in TEST_FILES_IMAGES:
        assert utils._match_fname(file)
    for file in TEST_FILES_NOT_IMAGES:
        assert not utils._match_fname(file)


def _create_message(attachments: List[ImposterAttachment], content: str) -> ImposterMessage:
    message = ImposterMessage()
    message.attachments = attachments
    message.content = content
    return message


def test_is_image():
    for file in TEST_FILES_IMAGES:
        message = _create_message([ImposterAttachment(file)], "")
        assert utils.is_image(message)
        message = _create_message([ImposterAttachment("Not an image")], f"http://test/{file}")
        assert utils.is_image(message)
        message = _create_message([ImposterAttachment("Not an image")], f"https://test/{file}")
        assert utils.is_image(message)

    for file in TEST_FILES_NOT_IMAGES:
        message = _create_message([ImposterAttachment(file)], "")
        assert not utils.is_image(message)
        message = _create_message([ImposterAttachment("Not an image")], f"http://test/{file}")
        assert not utils.is_image(message)
        message = _create_message([ImposterAttachment("Not an image")], f"https://test/{file}")
        assert not utils.is_image(message)

    # Test an invalid url
    message = _create_message([ImposterAttachment("Not an image")], "http://[test/yes.png")
    assert not utils.is_image(message)